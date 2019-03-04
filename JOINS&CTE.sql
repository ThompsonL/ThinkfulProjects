/* Problem 1 */
WITH rainy as 
(
SELECT 
	DATE(date) rain_date
FROM
	weather
WHERE 
	events = 'Rain'
GROUP BY 1
) 

SELECT
	t.trip_id,
	t.duration,
	DATE(t.start_date)
FROM 
	trips t
JOIN
	rainy r
on 
	DATE(t.start_date) = r.rain_date
ORDER BY duration DESC
LIMIT 3;

/* Problem 2 */
SELECT
	status.station_id,
	stations.name,
	COUNT(CASE WHEN docks_available=0 then 1 END) empty_count
FROM 
	status
JOIN 
	stations
on 
	stations.station_id = status.station_id
GROUP BY 1,2
ORDER BY empty_count DESC;

/* Problem 3 */
SELECT
	start_station,
	dockcount,
	COUNT(*)
FROM
	trips
JOIN
	stations
ON 
	stations.name=trips.start_station
GROUP BY 1, 2
ORDER BY 2 DESC;

/* Problem 4 */
WITH rainy as 
(
SELECT 
	DATE(date) weather_date
FROM 
	weather
WHERE 
	events = 'Rain'
GROUP BY 1
),
rain_trips as (
SELECT
	trip_id,
	duration,
	DATE(trips.start_date) rain_trips_date
FROM 
	trips
JOIN
	rainy
on 
	rainy.weather_date = DATE(trips.start_date)
ORDER BY duration DESC
)
SELECT 
	rain_trips_date,
	max(duration) max_duration
FROM 
	rain_trips
GROUP BY 1
ORDER BY max_duration DESC;
