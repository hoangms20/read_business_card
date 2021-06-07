
import mysql.connector
import jsonpickle
from . import mysql_connection


def select_all(connection):
    
    cur = connection.cursor()
    
    query = "SELECT * FROM card_scaner;"
    
    cur.execute(query)
    result_set = cur.fetchall()
    item_list = []

    for result in result_set:
        item_list.append(result)
        print(result)

    return item_list
    
def select_user(connection):
    
    cur = connection.cursor()
    
    query = "SELECT * FROM user;"
    
    cur.execute(query)
    result_set = cur.fetchall()
    item_list = []

    for result in result_set:
        item_list.append(result)
        print(result)

    return item_list

def selectbyname(connection, name):
    
    cur = connection.cursor()
    
    sql = "SELECT * FROM card_scaner WHERE Name LIKE '%" +  name + "%';"
    cur.execute(sql)
    result_set = cur.fetchall()
    item_list = []

    for result in result_set:
        item_list.append(result)
        print(result)

    return item_list

def selectbycompany(connection, company):
    
    cur = connection.cursor()
    
    sql = "SELECT * FROM card_scaner WHERE Company LIKE '%" +  company + "%';"
    cur.execute(sql)
    result_set = cur.fetchall()
    item_list = []

    for result in result_set:
        item_list.append(result)
        print(result)

    return item_list

def selectbyjob(connection, job):
    
    cur = connection.cursor()
    
    sql = "SELECT * FROM card_scaner WHERE Job LIKE '%" +  job + "%';"
    cur.execute(sql)
    result_set = cur.fetchall()
    item_list = []

    for result in result_set:
        item_list.append(result)
        print(result)

    return item_list

def update_pass(connection, val):
    print ("Start")
    cur = connection.cursor()

    sql = "UPDATE user SET Password = %s WHERE User = %s"
    
    cur.execute(sql, val)
    connection.commit()
    print ("Finish update")

def insert_query(connection, val):
    print ("Start")
    cur = connection.cursor()

    sql = "INSERT INTO card_scaner ( `Name`, `Job`, `Company`, `Email`, `Phone`, `Website`, `Address`, `Other`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    #sql = "INSERT INTO user (`User`, `Password`) VALUES (%s, %s)"
    cur.execute(sql, val)
    
    connection.commit()
    print ("Finish insert")


if __name__ == "__main__":
    connection = mysql_connection.create_connection()
#     select_query(connection)
#    update_query(connection)
    select_all(connection)

    