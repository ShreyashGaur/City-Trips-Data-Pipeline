CREATE OR REPLACE VIEW city_trips_data.gold.fact_trips
AS (
SELECT 
t.id,
t.business_date,
t.city_id,
c.city_name,
t.passenger_category,
t.distance_kms,
t.sales_amt,
t.passenger_rating,
t.driver_rating,
ca.month,
ca.day_of_month,
ca.day_of_week,
ca.month_name,
ca.month_year,
ca.quarter,
ca.quarter_year,
ca.week_of_year,
ca.is_weekday,
ca.is_weekend,
ca.is_holiday as national_holiday
FROM 
city_trips_data.silver.trips t
JOIN city_trips_data.silver.city c ON t.city_id = c.city_id
JOIN city_trips_data.silver.calendar ca ON t.business_date = ca.date
);