
from db import mysql_connection
from db import mysql_query

connection = mysql_connection.create_connection()

list_item = mysql_query.select_user(connection)

mysql_query.insert_query(connection)
