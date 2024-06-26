CREATE DATABASE carmax;
SHOW DATABASES;
USE carmax;
CREATE TABLE cars 
(vin VARCHAR(5), 
brand VARCHAR(20),
model VARCHAR(20), 
year INT, 
mileage INT, 
price INT,
color VARCHAR(20)
);
SHOW TABLES;
INSERT INTO cars VALUES ('GT123', 'Toyota', 'Camry', 2008, 70000, 8000, 'Black');
INSERT INTO cars VALUES ('AB382', 'Honda', 'Accord',2014, 10000,18000, 'White');
INSERT INTO cars VALUES ('Y3829', 'Hyundai','Sonata',2013, 20000,17000, 'Silver');
INSERT INTO cars VALUES ('P3726', 'BMW', 'E350', 2009, 60000,25000, 'Silver');
INSERT INTO cars VALUES ('4TX88', 'Ford', 'F150', 2017, 12,38500, 'Red');
