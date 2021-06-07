
from datetime import datetime, timedelta
from db import mysql_connection
from db import mysql_query

connection = mysql_connection.create_connection()
time2 = '2021-06-05'
time2 = datetime.strptime(time2, "%Y-%m-%d")
time2 += timedelta(days=1)
time2 = time2.date()
time2.strftime("%Y-%m-%d")
data = mysql_query.selectundertime(connection, str(time2))
for res in data:
    print(res)
