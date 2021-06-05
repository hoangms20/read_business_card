
import mysql.connector
import jsonpickle
from . import mysql_connection


def select_query(connection):
    
    cur = connection.cursor()
    
    query = "SELECT * FROM card_scaner;"
    
    cur.execute(query)
    result_set = cur.fetchall()
    item_list = []

    for result in result_set:
        item_list.append(result)
        print(result)

    #print (jsonpickle.encode(item_list))

    return item_list
    

def update_query(connection):
    print ("Start")
    cur = connection.cursor()

    query = "UPDATE image_info SET image_title = 'Test', number_of_view = number_of_view + 1 WHERE image_id = 2"
    
    cur.execute(query)
    connection.commit()
    print ("Finish")

def insert_query(connection):
    print ("Start")
    cur = connection.cursor()
    query = "INSERT INTO image_category(`cate_id`, `category_name`) VALUES (5, 'Gifs')";
    
    cur.execute(query)
    connection.commit()
    print ("Finish")


# if __name__ == "__main__":
#     connection = mysql_connection.create_connection()
# #     select_query(connection)
# #    update_query(connection)
#     select_query(connection)

    