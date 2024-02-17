-- create database hbtn_0d_usa in MySQL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create a table unique_id
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL);