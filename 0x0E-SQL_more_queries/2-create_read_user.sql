-- create a database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED WITH mysql_native_password
BY 'user_0d_2_Pwd';

-- grant SELECT privilege to user_0d_2 in
-- database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';