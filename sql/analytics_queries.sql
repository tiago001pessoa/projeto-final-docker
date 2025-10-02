-- Quais os 5 filmes mais populares? (por número de avaliações)
SELECT m.movie_id, m.title, COUNT(r.*) AS n_ratings
FROM movies m
JOIN ratings r ON r.movie_id = m.movie_id
GROUP BY m.movie_id, m.title
ORDER BY n_ratings DESC
LIMIT 5;

-- Qual gênero tem a melhor avaliação média?
SELECT genre, AVG(score) AS avg_score, COUNT(*) AS n_ratings
FROM movies m JOIN ratings r ON r.movie_id = m.movie_id
GROUP BY genre
HAVING COUNT(*) >= 5
ORDER BY avg_score DESC
LIMIT 1;

-- Qual país assiste mais filmes? (por número de avaliações)
SELECT u.country, COUNT(r.*) AS n_ratings
FROM users u JOIN ratings r ON r.user_id = u.user_id
GROUP BY u.country
ORDER BY n_ratings DESC
LIMIT 1;