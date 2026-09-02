#Create a database:
database={}
def insert_record(db,record):
    database[db]=record
    return database
def delete_record(db,record):
    del database[db]
    
    return database
def update_database(db,index,var):
    database[db][index]=var
    return database

insert_record(101,["mayur","pune",778899])
insert_record(102,["mayur","pune",778899])
insert_record(103,["mayur","pune",778899])
delete_record(101,["mayur","pune",778899])
update_database(102,0,"Mythri")
update_database(102,1,"Hyderabad")