CREATE DATABASE carmax;
SHOW DATABASES;
USE carmax;
CREATE TABLE cars (
    vin VARCHAR(20),
    type VARCHAR(10),
    brand VARCHAR(20),
    model VARCHAR(20),
    year INT,
    mileage INT,
    price INT,
    color VARCHAR(1),
    feature VARCHAR(20),
    is_available TINYINT(1)
);
INSERT INTO cars VALUES ('CD555SA72', 'Sedan', 'Toyota', 'Camry', 2010, 11000, 7000, 'S', ' ', 1);
INSERT INTO cars VALUES ('AB234KL34', 'Sedan', 'Honda', 'Civic', 2009, 15000, 4000, 'R', 'Hybrid', 0);
INSERT INTO cars VALUES ('XX55JKA31', 'Minivan', 'Honda', 'Odyssey', 2018, 500, 5000, 'B', 'Sliding Door', 1);
INSERT INTO cars VALUES ('FF2HHKL94', 'Sedan', 'BMW', '535i', 2011, 12000, 9000, 'W', ' ', 1);
INSERT INTO cars VALUES ('4TX8875VD', 'Truck', 'RAM', '2500', 2023, 2000, 10000, 'R', 'Off Road', 0);

SELECT * FROM cars;

DELETE FROM cars;
DROP DATABASE IF EXISTS carmax;


