# UPDATE COMMMAND:
# update students set age = 20 where name = "Pranshu";\
# DELETE COMMAND:
# delete from table_name where id = 10;

# Once commited you cannot rollback and if rolled back then commit has no use
# commit; ALL COMMANDS PREVIOUSLY SAVED AND COMMITED TO DATABASE
# rollback; ONE PREVIOUS COMMAND IF NOT COMMITED IN UNDONE

# Primary key always contain unique values
# CANNOT BE NULL & ONLY ONE ATTRIBUTE CAN BE PRIMARY IN A TABLE
# Foreign key in one table (child table) is used to point/refer to primary key of parent table 

# create table table_name(
#     attr1 int not null unique,
#     attr2 varchar(100) not null,
#     ........,
#     PRIMARY KEY(attr1)
#     FOREIGN KEY(attr2) REFERENCES table2_name (primary key of that parent table)
# )