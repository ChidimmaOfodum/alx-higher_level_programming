-- lists all records of a table

SELECT score, name FROM second_table
	WHERE name is not NULL
	ORDER BY score DESC
