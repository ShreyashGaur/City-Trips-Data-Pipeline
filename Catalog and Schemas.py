# Databricks notebook source
dbutils.widgets.text("catalog_name", "city_trips_data", "Catalog Name")
catalog_name = dbutils.widgets.get("catalog_name")

# COMMAND ----------

spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog_name}")

# COMMAND ----------

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.bronze;")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.silver;")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.gold;")

# COMMAND ----------

#Dropping Catalog along with Schema
#spark.sql(f"DROP CATALOG {catalog_name} CASCADE")