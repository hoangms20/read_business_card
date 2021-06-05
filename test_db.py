
from db import mysql_connection
from db import mysql_query

connection = mysql_connection.create_connection()

list_item = mysql_query.select_query(connection)

for result in list_item:
    for i in result:
        if(i != None):
            print(i)

    print("**"*30)