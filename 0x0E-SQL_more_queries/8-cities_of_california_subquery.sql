-- list all cities of california

SELECT * FROM cities WHERE state_id =
	(
		SELECT id from states where name = 'California'
	);
