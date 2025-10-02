import os
import csv
import psycopg2
from psycopg2 import sql
from datetime import datetime

DB_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/movieflix"
)


def connect():
    return psycopg2.connect(DB_URL)


def clean_movie(row):
    try:
        movie_id = int(row["movie_id"].strip())
        title = row["title"].strip() if row["title"] else None
        year = int(row["year"].strip()) if row["year"].isdigit() else None
        genre = row["genre"].strip() if row["genre"] else None
        if not title or not year:
            return None
        return (movie_id, title, year, genre)
    except Exception:
        return None


def clean_user(row):
    try:
        user_id = int(row["user_id"].strip())
        name = row["name"].strip() if row["name"] else None
        age = int(row["age"].strip()) if row["age"].isdigit() else None
        country = row["country"].strip() if row["country"] else None
        if not name or not age or not country:
            return None
        return (user_id, name, age, country)
    except Exception:
        return None


def clean_rating(row):
    try:
        rating_id = int(row["rating_id"].strip())
        user_id = int(row["user_id"].strip())
        movie_id = int(row["movie_id"].strip())
        score = float(row["score"].strip())
        if not (0 <= score <= 10):
            return None
        try:
            timestamp = datetime.fromisoformat(row["timestamp"].replace("Z", "+00:00"))
        except Exception:
            return None
        return (rating_id, user_id, movie_id, score, timestamp)
    except Exception:
        return None


def load_csv(conn, csv_path, table, columns, cleaner):
    seen = set()
    with open(csv_path, newline="", encoding="utf-8") as f, conn.cursor() as cur:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            cleaned = cleaner(row)
            if not cleaned:
                continue
            if cleaned[0] in seen:  # deduplicar pelo ID
                continue
            seen.add(cleaned[0])
            rows.append(cleaned)
        if rows:
            args_str = b",".join(
                cur.mogrify("(" + ",".join(["%s"] * len(columns)) + ")", r)
                for r in rows
            )
            insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ").format(
                sql.Identifier(table), sql.SQL(",").join(map(sql.Identifier, columns))
            )
            cur.execute(insert_query + sql.SQL(args_str.decode("utf-8")))
    conn.commit()


def main():
    conn = connect()
    try:
        load_csv(
            conn,
            "etl/data_lake/movies.csv",
            "movies",
            ["movie_id", "title", "year", "genre"],
            clean_movie,
        )
        load_csv(
            conn,
            "etl/data_lake/users.csv",
            "users",
            ["user_id", "name", "age", "country"],
            clean_user,
        )
        load_csv(
            conn,
            "etl/data_lake/ratings.csv",
            "ratings",
            ["rating_id", "user_id", "movie_id", "score", "timestamp"],
            clean_rating,
        )
    finally:
        conn.close()


if __name__ == "__main__":
    main()
