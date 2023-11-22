-- Create project testing database with the name: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user name hbnb_test with password hbnb_test_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Granting the SELECT privilege for the new user hbnb_test on the database performance_scheme
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Granting all privileges for the new user on db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply the changes 
FLUSH PRIVILEGES;
