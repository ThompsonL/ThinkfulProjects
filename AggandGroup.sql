/* Problem 1 */
SELECT
	maxtemperaturef,
	zip
FROM
	weather
ORDER BY maxtemperaturef DESC;
/* Hottest = 134 Location = 94063 */

/* Problem 2 */
SELECT COUNT(trip_id),
	start_station
FROM
	trips
GROUP BY
	start_station
ORDER BY COUNT(trip_id) DESC;

/* PROBLEM 3 */
SELECT
	duration,
	start_station,
	end_station
FROM
	trips
ORDER BY duration ASC;

/*Problem 4*/
SELECT DISTINCT
	end_station,
	AVG(duration)
FROM
	trips
GROUP BY end_station;
