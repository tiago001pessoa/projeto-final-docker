-- Top 10 filmes por média ponderada (mais avaliações)
CREATE OR REPLACE VIEW datamart_top10_by_avg AS
SELECT m.movie_id, m.title, m.genre, COUNT(r.*) AS n_ratings, AVG(r.score) AS avg_score
FROM movies m
JOIN ratings r ON r.movie_id = m.movie_id
GROUP BY m.movie_id, m.title, m.genre
ORDER BY avg_score DESC, n_ratings DESC
LIMIT 10;

-- Nota média por faixa etária (cria buckets)
CREATE OR REPLACE VIEW datamart_avg_by_age_bucket AS
SELECT
  CASE
    WHEN u.age < 18 THEN '<18'
    WHEN u.age BETWEEN 18 AND 24 THEN '18-24'
    WHEN u.age BETWEEN 25 AND 34 THEN '25-34'
    WHEN u.age BETWEEN 35 AND 49 THEN '35-49'
    ELSE '50+' END AS age_bucket,
  AVG(r.score) AS avg_score,
  COUNT(r.*) AS n_ratings
FROM users u
JOIN ratings r ON r.user_id = u.user_id
GROUP BY age_bucket
ORDER BY age_bucket;

-- Número de avaliações por país
CREATE OR REPLACE VIEW datamart_ratings_by_country AS
SELECT u.country, COUNT(r.*) AS n_ratings
FROM users u
JOIN ratings r ON r.user_id = u.user_id
GROUP BY u.country
ORDER BY n_ratings DESC;