from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer)
    genre = db.Column(db.String(100))


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    age = db.Column(db.Integer)
    country = db.Column(db.String(100))


class Rating(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
    score = db.Column(db.Float, nullable=False)
