CREATE OR REPLACE VIEW city_trips_data.gold.fact_trips_coimbatore
AS (
SELECT *
FROM city_trips_data.gold.fact_trips
WHERE city_id = 'TN01'
);