-- movies (DW)
CREATE TABLE IF NOT EXISTS movies (
  movie_id INTEGER PRIMARY KEY,
  title TEXT,
  year INTEGER,
  genre TEXT
);

CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  country TEXT
);

CREATE TABLE IF NOT EXISTS ratings (
  rating_id INTEGER PRIMARY KEY,
  user_id INTEGER REFERENCES users(user_id),
  movie_id INTEGER REFERENCES movies(movie_id),
  score REAL,
  timestamp TIMESTAMP
);