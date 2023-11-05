# Constraints : 
# NOT NULL
# UNIQUE
# DEFAULT
# CHECK
# FOREIGN KEY
# PRIMARY KEY
# We can use these constraints while creating a table to give column/attribute constraints like:
# create table users(
#     email varchar(100) not null unique
# );
# and, or and not operators are used to compare and give booleans to 2 expressions
# select * from table_name where col1 = val1 and col2 = val2 or col3 = val3 and not col4 = val4;
# Multiple and and or's can be used in a single query
# IN operator: 
# Used for mutiple or conditions
# select * from table_name where age in(21,22,23,24,25); // Multiple or nor needed
# select * from table_name where name like "a%"; {There are many like symbols please refer the like.png}
# BETWEEN operator: 
# Used for a particular range
# select * from table_name where age betweeen 20 and 25;
# select * from table_name where name between "Ashish" and "Vivek";
# ORDER BY: ASC | DESC -> Order a table in ascending or descending based on a attribute
# select * from table_name order by col1 asc;
# select * from table_name order by col1 desc;
# IS NULL and IS NOT NULL -> 
# select * from table_name where col is null;
# select * from table_name where col2 is not null;
# LIMIT AND OFFSET : 
# select * from table_name limit 10; -> 10 rows displayed
# selct * from table_name limit 10 offset 5; -> 10 rows displayed but from 6th row leaving 5 rows offset
# count() , sum() , avg() , min() , max() are built-in functions that can be used
# select sum(age) from users;
# select avg(fees) as 'avgFees' from users;