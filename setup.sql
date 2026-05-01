CREATE DATABASE IF NOT EXISTS snackify;
USE snackify;

CREATE TABLE IF NOT EXISTS menu (
    sno INT PRIMARY KEY,
    items VARCHAR(50),
    cost INT
);

CREATE TABLE IF NOT EXISTS staff (
    sno INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT
);
