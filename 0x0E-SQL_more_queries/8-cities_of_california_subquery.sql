-- list all cities of california

SELECT id, name FROM cities WHERE state_id =
	(
		SELECT id from states where name = 'California'
	)
	ORDER BY cities.id ASC;
