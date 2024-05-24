-- Lists all records with the same score in desc order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
HAVING number > 0
ORDER BY number DESC
