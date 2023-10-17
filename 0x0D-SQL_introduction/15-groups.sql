-- list number of records with the same score

SELECT score, count(score) AS "number" FROM second_table
	GROUP BY score
	HAVING count(score) > 1

