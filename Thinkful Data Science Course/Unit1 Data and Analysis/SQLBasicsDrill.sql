/* Problem 1 */
SELECT
	trip_id,
	duration
FROM
	trips
WHERE
	duration > 500
ORDER BY duration DESC; 

/* Problem 2 */
SELECT 
	*
FROM
	stations
WHERE
	station_id = 84;

/* Problem 3 */
SELECT
	mintemperaturef
FROM
	weather
WHERE
	zip = 94301;
