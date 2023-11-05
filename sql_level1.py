# MySQL is a relational database management system (RDBMS) developed by Oracle
# It is based on SQL (Structured Query Language)
# Database is an organized collection of data (structured information)\
# DBMS (Database Management Systems) are software systems used to store, retrieve and run queries on data.
# Rows are horizontal data and columns and attributes are vertical arrangements.
# CRUD Operations : 
# C -> CREATE
# R -> READ
# U -> UPDATE
# D -> DELETE
# Relational Database are those which have predefined relationships between them, stored as table, rows and columns
# List of SQL using databases : MySQL, PostgreSQL, Oracle, MariaDB, etc.

# Basic queries ( C AND R )
# IMPORTANT : USE OF CAPITAL LETTERS FOR SELECT, CREATE, FROM, WHERE, AND, OR, ETC. is not mandatory but is preffered in MySQL workbench;

# show databases;
# create database database_name;
# use database_name;
# create table table_name(
#     column1 datatype,
#     column2 datatype, .... 
# );
# datatype can be of 3 types only : string, numeric and data & time
# select * from table_name; or select * from database.table_name;
# insert into table_name(
# col1, col2, ...
# ) values(
# val1, val2);
# insert into table_name(col1, col2..) values(val1, val2..), (val3, val4);
# select col1, col2 from table_name;
# select * from table_name where age > 20;  (Or any condition like : col + operator + value) 
# select * from table_name where name = "Pranshu";