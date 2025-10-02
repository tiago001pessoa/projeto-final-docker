from flask import Blueprint, jsonify
from .models import db, Movie, User, Rating

bp = Blueprint("api", __name__)


@bp.route("/movies")
def get_movies():
    movies = Movie.query.all()
    return jsonify(
        [
            {"id": m.id, "title": m.title, "year": m.year, "genre": m.genre}
            for m in movies
        ]
    )


@bp.route("/users")
def get_users():
    users = User.query.all()
    return jsonify(
        [
            {"id": u.id, "name": u.name, "age": u.age, "country": u.country}
            for u in users
        ]
    )


@bp.route("/ratings")
def get_ratings():
    ratings = Rating.query.all()
    return jsonify(
        [
            {"id": r.id, "user_id": r.user_id, "movie_id": r.movie_id, "score": r.score}
            for r in ratings
        ]
    )
