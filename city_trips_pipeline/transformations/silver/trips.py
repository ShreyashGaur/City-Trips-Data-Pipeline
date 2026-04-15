from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.view(
    name="trip_silver_staging",
    comment="Transformed trips data ready for CDC upsert"
)

@dp.expect("valid_date", "year(business_date) >= 2000")
@dp.expect("valid_driver_rating", "driver_rating BETWEEN 1 AND 10")
@dp.expect("valid_passenger_rating", "passenger_rating BETWEEN 1 AND 10")

def trips_silver():
    df_bronze = spark.readStream.table("city_trips_data.bronze.trips")

    df_silver = df_bronze.select(
        F.col("trip_id").alias("id"),
        F.col("date").cast("date").alias("business_date"),
        F.col("city_id").alias("city_id"),
        F.col("passenger_type").alias("passenger_category"),
        F.col("distance_travelled_km").alias("distance_kms"),
        F.col("fare_amount").alias("sales_amt"),
        F.col("passenger_rating").alias("passenger_rating"),
        F.col("driver_rating").alias("driver_rating"),
        F.col("ingest_datetime").alias("bronze_ingest_timestamp"),
    )

    df_silver = df_silver.withColumn(
        "silver_processed_timestamp", F.current_timestamp()
    )

    return df_silver

dp.create_streaming_table(
    name="city_trips_data.silver.trips",
    comment="Cleaned and validated orders with CDC upsert capability",
    table_properties={
        "quality": "silver",
        "layer": "silver",
        "delta.enableChangeDataFeed": "true",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true"
    },
)

#Auto CDC (Change Data Capture) flow
dp.create_auto_cdc_flow(
    target="city_trips_data.silver.trips",
    source="trip_silver_staging",
    keys=["id"],
    sequence_by=F.col("silver_processed_timestamp"),
    stored_as_scd_type=1
)