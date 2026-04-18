CREATE OR REPLACE VIEW city_trips_data.gold.fact_trips_surat
AS (
SELECT *
FROM city_trips_data.gold.fact_trips
WHERE city_id = 'GJ01'
);