CREATE DATABASE Cars;
USE Cars;

SHOW VARIABLES LIKE "secure_file_priv";

CREATE TABLE used_cars (
    Brand VARCHAR(50),
    Model_Name VARCHAR(50),
    Model_Variant VARCHAR(50),
    Car_Type VARCHAR(20),
    Transmission VARCHAR(20),
    Fuel_Type VARCHAR(20),
    Year INT,
    Kilometers INT,
    Buyer VARCHAR(10),
    State VARCHAR(50),
    Accidental VARCHAR(10),
    Price INT
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Cars_dataset.csv'
INTO TABLE used_cars
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' 
IGNORE 1 ROWS;

-- Total Rows
SELECT COUNT(*) AS total_rows FROM used_cars;

-- Total Columns
SELECT COUNT(*) AS total_columns
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'Cars' AND TABLE_NAME = 'used_cars';

-- Preview First 10 Rows
SELECT * FROM used_cars LIMIT 10;

-- Total Cars
SELECT COUNT(*) AS total_cars
FROM used_cars;

-- No. of Cars by Brand 
SELECT Brand, COUNT(*) AS total
FROM used_cars
GROUP BY Brand
ORDER BY total DESC;

-- Distribution of Car by Fuel Type
SELECT Fuel_Type, COUNT(*) AS count
FROM used_cars
GROUP BY Fuel_Type;

-- Manual vs Automatic Transmission Count
SELECT Transmission, COUNT(*) AS count
FROM used_cars
GROUP BY Transmission;

--  Average Kilometers by Car Type
SELECT Car_Type, ROUND(AVG(Kilometers), 2) AS avg_km
FROM used_cars
GROUP BY Car_Type
ORDER BY avg_km DESC;

-- Average Price by Fuel Type
SELECT Fuel_Type, ROUND(AVG(Price), 2) AS avg_price
FROM used_cars
GROUP BY Fuel_Type
ORDER BY avg_price DESC;

-- Top States by Number of Cars
SELECT State, COUNT(*) AS total
FROM used_cars
GROUP BY State
ORDER BY total DESC;

-- Cars Grouped by Year
SELECT Year, COUNT(*) AS total
FROM used_cars
GROUP BY Year
ORDER BY Year DESC;

-- Number of Cars by Ownership Type
SELECT Owner, COUNT(*) AS count
FROM used_cars
GROUP BY Owner;

-- Top 5 Most Expensive Cars
SELECT Brand, Model_Name, Model_Variant, Price
FROM used_cars
ORDER BY Price DESC
LIMIT 5;

-- Cars with More than 100,000 Kilometers
SELECT Brand, Model_Name, Kilometers, Year
FROM used_cars
WHERE Kilometers > 100000
ORDER BY Kilometers DESC;

-- Accident-Free Cars Count
SELECT COUNT(*) AS accident_free
FROM used_cars
WHERE Accidental = 'No';

-- Cars Cheaper Than ₹5 Lakhs
SELECT Brand, Model_Name, Price
FROM used_cars
WHERE Price < 500000
ORDER BY Price ASC;

-- Fuel Type vs Transmission Cross Table
SELECT Fuel_Type, Transmission, COUNT(*) AS count
FROM used_cars
GROUP BY Fuel_Type, Transmission
ORDER BY count DESC;

-- Average Price and Kilometers by Buyer Type
SELECT Buyer, ROUND(AVG(Price)) AS avg_price, ROUND(AVG(Kilometers)) AS avg_km
FROM used_cars
GROUP BY Buyer;


