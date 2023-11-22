-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost)

-- Get privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Create user user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Grant privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Get privileges for user_0d_1 again to verify
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Create user user_0d_2 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges to user_0d_2
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Get privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
