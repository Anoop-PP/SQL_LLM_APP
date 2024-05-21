import sqlite3
# connect to sqlite
connection=sqlite3.connect("EMPLOYEE.db")


## Create a cursor object to insert record, create table,retrieve
cursor=connection.cursor()

## create the table
table_info="""
Create table EMPLOYEE(NAME VARCHAR(25),DESIGNATION VARCHAR(25),
LOCATION VARCHAR(25),SALARY INT);

"""

cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into EMPLOYEE values('Krish','Data Scientist','NOIDA',90000)''')
cursor.execute('''Insert Into EMPLOYEE values('Sanjay','Devops Engineer','Bangalore',80000)''')
cursor.execute('''Insert Into EMPLOYEE values('Vinay','Data Analtics','Kochi',70000)''')
cursor.execute('''Insert Into EMPLOYEE values('Vikash','Network Engineer','Chennai',95000)''')
cursor.execute('''Insert Into EMPLOYEE values('Ajay','Python Developer','Hyderabad',60000)''')


## Display all records
print('The Inserted records are')


data=cursor.execute('''Select * From EMPLOYEE''')

for row in data:
    print(row)



 ## Close the connection


connection.commit()
connection.close()