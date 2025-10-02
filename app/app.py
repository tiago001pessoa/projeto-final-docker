from flask import Flask, request, jsonify, render_template_string
from models import init_db, db, Movie, User, Rating
from .views import bp

app = Flask(__name__)
app.config.from_mapping(
    {
        "SQLALCHEMY_DATABASE_URI": "postgresql://postgres:postgres@db:5432/movieflix",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
)
init_db(app)
app.register_blueprint(bp)

INDEX_HTML = """
<!doctype html>
<title>MovieFlix</title>
<h1>MovieFlix - Cadastro</h1>
<form action="/movies" method="post">
  Title: <input name="title"><br>
  Year: <input name="year"><br>
  Genre: <input name="genre"><br>
  <button type="submit">Add movie</button>
</form>
<hr>
<form action="/ratings" method="post">
  User ID: <input name="user_id"><br>
  Movie ID: <input name="movie_id"><br>
  Score (0-10): <input name="score"><br>
  <button type="submit">Rate</button>
</form>
"""


@app.route("/")
def index():
    return render_template_string(INDEX_HTML)


@app.route("/movies", methods=["POST"])
def create_movie():
    data = request.form or request.get_json()
    m = Movie(title=data.get("title"), year=data.get("year"), genre=data.get("genre"))
    db.session.add(m)
    db.session.commit()
    return jsonify({"id": m.id, "title": m.title}), 201


@app.route("/ratings", methods=["POST"])
def create_rating():
    data = request.form or request.get_json()
    r = Rating(
        user_id=int(data["user_id"]),
        movie_id=int(data["movie_id"]),
        score=float(data["score"]),
    )
    db.session.add(r)
    db.session.commit()
    return jsonify({"id": r.id}), 201


@app.route("/health")
def health():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
