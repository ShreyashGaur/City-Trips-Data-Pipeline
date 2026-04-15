CREATE OR REPLACE VIEW city_trips_data.gold.fact_trips_kochi
AS (
SELECT *
FROM city_trips_data.gold.fact_trips
WHERE city_id = 'KL01'
);