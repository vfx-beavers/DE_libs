SELECT COUNT(*) FROM stg_parking;

-- Get column names and data types

SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'stg_parking';

-- Determine number of null values for each column

SELECT COUNT(*) - COUNT("ID") ID,
 COUNT(*) - COUNT("Name") "Name",
 COUNT(*) - COUNT(global_id) global_id,
 COUNT(*) - COUNT("Photo") Photo,
 COUNT(*) - COUNT("AdmArea") AdmArea,
 COUNT(*) - COUNT("District") District,
 COUNT(*) - COUNT("DepartmentalAffiliation") DepartmentalAffiliation,
 COUNT(*) - COUNT("Address") Address,
 COUNT(*) - COUNT("Capacity") Capacity,
 COUNT(*) - COUNT("ObjectOperOrgName") ObjectOperOrgName,
 COUNT(*) - COUNT("ObjectOperOrgPhone") ObjectOperOrgPhone,
 COUNT(*) - COUNT("Longitude_WGS84") Longitude_WGS84,
 COUNT(*) - COUNT("Latitude_WGS84") Latitude_WGS84,
 COUNT(*) - COUNT("geoData") geoData,
 COUNT(*) - COUNT(geodata_center) geodata_center,
 COUNT(*) - COUNT("Unnamed: 15") "Unnamed: 15"
FROM public.stg_parking;

-- Checking for duplicates based on ride_id
SELECT COUNT("ID") - COUNT(DISTINCT("ID")) AS duplicate_rows
FROM public.stg_parking;


-- ride_id - all have length of 16

SELECT LENGTH("ID") AS length_id, COUNT("ID") AS no_of_rows
FROM public.stg_parking
GROUP BY length_id;

-- rideable_type - 3 unique types of bikes

SELECT DISTINCT rideable_type, COUNT(rideable_type) AS no_of_trips
FROM `2022_tripdata.combined_data`
GROUP BY rideable_type;

-- started_at, ended_at - TIMESTAMP - YYYY-MM-DD hh:mm:ss UTC

SELECT started_at, ended_at
FROM `2022_tripdata.combined_data`
LIMIT 10;

SELECT COUNT(*) AS longer_than_a_day
FROM `2022_tripdata.combined_data`
WHERE (
  EXTRACT(HOUR FROM (ended_at - started_at)) * 60 +
  EXTRACT(MINUTE FROM (ended_at - started_at)) +
  EXTRACT(SECOND FROM (ended_at - started_at)) / 60) >= 1440;   -- longer than a day - total rows = 5360

SELECT COUNT(*) AS less_than_a_minute
FROM `2022_tripdata.combined_data`
WHERE (
  EXTRACT(HOUR FROM (ended_at - started_at)) * 60 +
  EXTRACT(MINUTE FROM (ended_at - started_at)) +
  EXTRACT(SECOND FROM (ended_at - started_at)) / 60) <= 1;      -- less than a minute - total rows = 122283

-- start_station_name, start_station_id - total 833064 rows with both start station name and id missing

SELECT DISTINCT start_station_name
FROM `2022_tripdata.combined_data`
ORDER BY start_station_name;

SELECT COUNT(ride_id) AS rows_with_start_station_null          -- return 833064 rows
FROM `2022_tripdata.combined_data`
WHERE start_station_name IS NULL OR start_station_id IS NULL;

-- end_station_name, end_station_id - total 892742 rows with both end station name and id missing

SELECT DISTINCT end_station_name
FROM `2022_tripdata.combined_data`
ORDER BY end_station_name;

SELECT COUNT(ride_id) AS rows_with_null_end_station          -- return 892742 rows
FROM `2022_tripdata.combined_data`
WHERE end_station_name IS NULL OR end_station_id IS NULL;

-- end_lat, end_lng - total 5858 rows with both missing

SELECT COUNT(ride_id) AS rows_with_null_end_loc
FROM `2022_tripdata.combined_data`
WHERE end_lat IS NULL OR end_lng IS NULL;

-- member_casual - 2 unique values - member and casual riders

SELECT DISTINCT member_casual, COUNT(member_casual) AS no_of_trips
FROM `2022_tripdata.combined_data`
GROUP BY member_casual;