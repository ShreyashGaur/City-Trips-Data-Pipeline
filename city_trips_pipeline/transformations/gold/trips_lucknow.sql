CREATE OR REPLACE VIEW city_trips_data.gold.fact_trips_lucknow
AS (
SELECT *
FROM city_trips_data.gold.fact_trips
WHERE city_id = 'UP01'
);