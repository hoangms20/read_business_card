
from db import mysql_connection
from db import mysql_query

connection = mysql_connection.create_connection()

name = "fuka"
data = mysql_query.selectbyname(connection, name)
for res in data:
    print(res)
