/* Problem 1 */
SELECT
	name,
	neighbourhood,
	room_type,
	price,
	minimum_nights,
	number_of_reviews,
	availability_365
FROM
	sfo_listings
ORDER BY price DESC;

/*Problem 2*/
SELECT
	neighbourhood,
	number_of_reviews,
	reviews_per_month,
	availability_365
FROM
	sfo_listings
GROUP BY
	neighbourhood, number_of_reviews, reviews_per_month, availability_365
ORDER BY number_of_reviews DESC;

/*Problem 3*/
SELECT
	calender_date,
	price
FROM
	sfo_calendar
GROUP BY calender_date, price
ORDER BY 1, 2 ASC
Limit 10;

/* Problem 4 */
SELECT 
	calendar.calender_date, listings.name, listings.availability_365
FROM 
	sfo_listings listings
JOIN
	sfo_calendar calendar
ON
	listings.id = calendar.listing_id
GROUP BY 1, 2, 3
ORDER BY availability_365;
