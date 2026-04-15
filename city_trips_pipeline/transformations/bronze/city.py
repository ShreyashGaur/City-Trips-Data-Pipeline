from pyspark import pipelines as dp
from pyspark.sql.functions import col, current_timestamp
from pyspark.sql.functions import md5, sha2, concat_ws

#Configuration of source
SOURCE_PATH = "s3://citytrips-sg28/data-store/city"

@dp.materialized_view(
    name="city_trips_data.bronze.city",
    comment="City raw data processing from S3",
    table_properties={
        "quality": "bronze",
        "layer": "bronze",
        "source_format": "csv",
        "delta.enablechangeDataFeed": "true",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true",
    }
)

#Reading data from S3
def city_bronze():
    df = spark.read.format("csv")\
        .option("header", "true")\
        .option("inferSchema", "true")\
        .option("mode", "PERMISSIVE")\
        .option("mergeSchema", "true")\
        .option("columnNameOfCorrupt", "true")\
        .load(SOURCE_PATH)

#Adding Metadata column
    df = df.withColumn("file_name", col("_metadata.file_path"))\
        .withColumn("ingestdatetime", current_timestamp())
    
#Returning the data
    return df