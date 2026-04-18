# This is the guide to the Project
-------------------------------------------------------------------------
# Step 01 - Setting-up Catalog and Schemas:
# 1. Create Project Directory
# 2. Create a Setup Notebook inside the Directory
# 3. Create a Catalog using CREATE CATALOG SQL Query
# 4. Create Schemas (Bronze, Silver, Gold) using CREATE SCHEMAS SQL Query
-------------------------------------------------------------------------
# Step 02 - Create a S3 Bucket:
# 1. Create a S3 Bucket with Unique name
# 2. Create a folder to store dataset
# 3. Create dataset perticular folder
# 4. Upload City and Trips data in their respective folders
-------------------------------------------------------------------------
# Step 03 - Dataset view in Catalog:
# 1. Go to Catalog > Settings > External Data
# 2. Create External Location > Enter Bucket name
# 3. Generate new tocken > Copy the token > Launch
# 4. Enter token in "Databricks personal access token" > Acknowledge and Create Stack
-------------------------------------------------------------------------
# Step 04 - Create ETL Pipeline:
# 1. Go to Jobs & Pipelines > ETL Pipeline > enter pipeline name
# 2. Select the Workspace and Bronze schema > Keep Pipeline Editor ON
# 3. Start with an Empty file > Select Project directory
# 4. Create Separate folders for Bronze, Silver, and Gold inside default generaed "transformations" folder
# 5. Move the "transformation.py" file inside bronze folder, and rename it to "City"
-------------------------------------------------------------------------
# Step 05 - City file code: (Bronze.city)
# 1. Import neccessary libraries
# 2. Read data from Source path (S3 bucket)
# 3. Load the dataset from Source path to Bronze table
# 4. Create metadata columns for "File path" and "Ingestion timestamp"
# 5. Return the dataframe 
# 6. Define Materialized view for Bronze table
# 7. Dry run the pipeline
-------------------------------------------------------------------------
# Step 06 - City file code: (Silver.city)
# 1. Import neccessary libraries
# 2. Read data from Bronze table
# 3. Rename the required Columns using alias
# 4. Create new column for "Silver Ingestion timestamp"
# 5. Return the dataframe
# 6. Define Materialized view for Silver table
# 7. Dry run the pipeline
-------------------------------------------------------------------------
# Step 07 - Calendar file code: (Silver.calendar)
# 1. Import neccessary libraries
# 2. Setup start and end date configurations
# 3. Create new columns for "Date", "Year", "Month", "Day", "Day of Week", "Day of Year", "Week of Year",...
# 4. Return the dataframe
# 5. Define Materialized view for Calendar table
# 6. Dry run the pipeline
# 7. Go to settings > add configurations for start and end date
-------------------------------------------------------------------------
# Step 08 - Trips file code: (Bronze.trips)
# 1. Import neccessary Libraries
# 2. Read data from Source path (S3 bucket)
# 3. Read the Streaming data in Bronze table using Autoloader
# 4. Rename the problematic column "distance_travelled_km"
# 5. Define a Table view for Bronze table
# 6. Dry run the pipeline
-------------------------------------------------------------------------
# Step 09 - Trips file code: (Silver.trips)
# 1. Import neccessary Libraries
# 2. Read data from Bronze table
# 3. Change names of required column
# 4. Create a column for "Silver Ingestion timestamp"
# 5. Return the dataframe
# 6. Define View for Silver table
# 7. Define Expects for Silver table
# 8. Define a Streaming table
# 9. Create auto cdc (change Data Capture) flow
# 10. Dry run the pipeline
-------------------------------------------------------------------------
# Step 10 - Trips_gold file SQL code: (Gold.trips)
# 1. Create and Replace the view with fetched data
# 2. Join the Silver.city and Silver.calendar table with Silver.trips
-------------------------------------------------------------------------
# Step 11 - City View Code: (Gold.fact_trips)
# Create City specific views and fetch trips data using the city id
# Run the pipeline
-------------------------------------------------------------------------
# Schedule the pipeline using the Schedule feature based on requirement.
# If you want to run the pipeline as soon as new data is dropped: then go to Setting > Pipeline mode: "Continue"
-------------------------------------------------------------------------
# Step 12 - Incremental load:
# 1. Add new data in Trips folder of S3 bucker
# 2. Observe that pipeline runs automatically as there is update in the bucket
-------------------------------------------------------------------------
# Step 13 - Access Permission:
# 1. Go to Settings > Identity and access > add people / group
# 2. Go to Catalog > any Schema > Permissions > Grant > select people / group