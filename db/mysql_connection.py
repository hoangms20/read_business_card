#!/usr/bin/python
import mysql.connector
from . import config

def create_connection():
    try:
        conn = mysql.connector.connect(host=config.mysql_host,    # your host, usually localhost
                     port=config.mysql_port,
                     user=config.mysql_user,         # your username
                     password=config.mysql_pass,  # your password
                     database=config.mysql_db)        # name of the data base
        return conn
    except:
        print ("Can't connect to database!")
        return None

