SELECT primarytitle, titletype, startyear, averagerating, numvotes
FROM title_basics AS b
JOIN title_ratings AS r
    ON b.tconst = r.tconst
WHERE numvotes > 50000
ORDER BY averagerating DESC
LIMIT 50;


SELECT genres, COUNT(*) AS title_count, AVG(averagerating), AVG(numvotes) AS avg_votes
FROM title_basics AS b
JOIN title_ratings AS r
    ON b.tconst = r.tconst
WHERE genres IS NOT NULL AND numvotes >= 10000
GROUP BY genres
HAVING COUNT(primarytitle) >= 50
ORDER BY AVG(averagerating) DESC
LIMIT 15;


SELECT titletype, COUNT(*) AS title_count, AVG(averagerating) AS avg_rating, AVG(numvotes) AS avg_votes
FROM title_basics AS b
JOIN title_ratings AS r
    ON b.tconst = r.tconst
WHERE numvotes >= 10000 AND titletype IN ('movie', 'tvSeries', 'tvMiniSeries')
GROUP BY titletype;


SELECT startyear, COUNT(*) AS title_count, AVG(averagerating) AS avg_rating
FROM title_basics AS b
JOIN title_ratings AS r
    ON b.tconst = r.tconst
WHERE startyear IS NOT NULL AND numvotes >= 10000 AND startyear BETWEEN 1980 AND 2025
GROUP BY startyear
HAVING COUNT(*) >= 100;


SELECT COUNT(*) AS title_count, AVG(averagerating) AS avg_rating,
       CASE
           WHEN runtimeminutes < 60 THEN '<60'
           WHEN runtimeminutes BETWEEN 60 AND 89 THEN '60-89'
           WHEN runtimeminutes BETWEEN 90 AND 119 THEN '90-119'
           WHEN runtimeminutes BETWEEN 120 AND 149 THEN '120-149'
           WHEN runtimeminutes >= 150 THEN '150+'
       END AS runtime_bucket
FROM title_basics AS b
JOIN title_ratings AS r
    ON b.tconst = r.tconst
WHERE titletype = 'movie' AND runtimeminutes IS NOT NULL AND numvotes >= 10000
GROUP BY runtime_bucket;


SELECT COUNT(p.tconst) AS appearances, primaryname
FROM title_principals AS p
JOIN title_ratings AS r
    ON p.tconst = r.tconst
JOIN name_basics AS n
    ON p.nconst = n.nconst
WHERE category IN ('actor', 'actress') AND r.averagerating >= 8.5 AND r.numvotes >= 50000
GROUP BY primaryname
ORDER BY COUNT(p.tconst) DESC
LIMIT 20;


SELECT n.primaryname,
       COUNT(*) AS appearances,
       ROUND(AVG(r.averagerating), 2) AS avg_rating
FROM title_principals p
JOIN title_ratings r ON p.tconst = r.tconst
JOIN title_basics b ON p.tconst = b.tconst
JOIN name_basics n ON p.nconst = n.nconst
WHERE p.category IN ('actor', 'actress')
  AND r.numvotes >= 100000
  AND b.titletype = 'movie'
GROUP BY n.primaryname
HAVING COUNT(*) >= 5
ORDER BY appearances DESC
LIMIT 15;
