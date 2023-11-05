# ONLY APPLICABLE FOR TABLES THAT HAVE RELATIONSHIPS

# Inner Join is used to get data from tables that match
# select * from table_1 INNER JOIN table_2 ON students.city_id = citites.cid;

# Left join means to get all data from left table but only matching data from right table
# Right join means vice versa
# select * from table_1 LEFT JOIN table_2 ON student.city = cities.id;

# Cross join -> Cartesian Product of table 
# Each Joined with each 
# (Total rows = table1 rows * table2 rows)
# (Total columns = (table1_col + table2_col) - 1)
# select * from table_1 CROSS JOIN table_2; BASED ON TABLE 1
# select * from table_2 CROSS JOIN table_1; BASED ON TABLE 2

# Multiple joins like 2 inner joins or 1 left and 1 inner, etc. can be made according to needs.

# SUB QUERY -> A QUERY INSIDE A QUERY
# select * from table_1 where col1 = (select age from users where age > 20);

# Exists : Similar as above but checks true or false, if true returns value and if false returns null
# select * from table_1 where exists (select age from users where age > 20);
# Not Exists : INVERSE of exists
# select * from table_1 where exists (select age from users where age > 20);

# GROUP_BY : Make group with attributes , HAVING : condition for group by
# select cid, name from students group by (name) having cid > 5;
