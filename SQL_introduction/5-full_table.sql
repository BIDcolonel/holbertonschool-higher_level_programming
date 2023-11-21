-- Prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server
SELECT CONCAT('Table: ', TABLE_NAME) AS 'Table',
        CONCAT('Create Table: ', CREATE_TABLE) AS 'Create Table'
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
    AND TABLE_NAME = 'first_table';
