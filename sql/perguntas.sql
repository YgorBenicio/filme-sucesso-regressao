SELECT
    COUNT(*)            AS total_filmes,
    ROUND(AVG(budget))  AS orcamento_medio,
    ROUND(AVG(revenue)) AS receita_media,
    MIN(release_year)   AS ano_mais_antigo,
    MAX(release_year)   AS ano_mais_recente
FROM filmes;

SELECT
    title,
    budget,
    revenue,
    (revenue - budget) AS lucro
FROM filmes
ORDER BY revenue DESC
LIMIT 10;

SELECT
    title,
    budget,
    revenue,
    (revenue - budget) AS lucro
FROM filmes
WHERE budget > 0 AND revenue > 0
ORDER BY lucro DESC
LIMIT 10;

SELECT
    release_year        AS ano,
    COUNT(*)            AS total_filmes
FROM filmes
WHERE release_year >= 1980
GROUP BY release_year
ORDER BY release_year;


SELECT
    original_language   AS idioma,
    COUNT(*)            AS total_filmes,
    ROUND(AVG(revenue)) AS receita_media
FROM filmes
GROUP BY original_language
ORDER BY receita_media DESC
LIMIT 8;


SELECT
    title,
    vote_average        AS nota,
    vote_count          AS votos,
    revenue
FROM filmes
WHERE vote_count > 500
ORDER BY vote_average DESC
LIMIT 10;



SELECT
    CASE
        WHEN revenue > (SELECT AVG(revenue) FROM filmes) THEN 'Acima da média'
        ELSE 'Abaixo da média'
    END                     AS faixa_receita,
    COUNT(*)                AS total_filmes,
    ROUND(AVG(budget))      AS orcamento_medio,
    ROUND(AVG(vote_average)) AS nota_media
FROM filmes
GROUP BY faixa_receita;


SELECT
    (release_year / 10) * 10    AS decada,
    COUNT(*)                    AS total_filmes,
    ROUND(AVG(revenue))         AS receita_media
FROM filmes
WHERE release_year IS NOT NULL
GROUP BY decada
ORDER BY decada;
