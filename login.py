import dashboard
import os
import tkinter as tk
from tkinter.constants import END
import tkinter.ttk as ttk
import pygubu
import tkinter.messagebox as tmsg  

#import db
from db import mysql_connection
from db import mysql_query

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "login.ui")

#login GUI
class LoginApp:
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('login', master)
        builder.connect_callbacks(self)
        #load user
        global connection
        connection = mysql_connection.create_connection()
        load_user()
    
    def login(self):
        global user_name
        global password
        self.user = self.builder.get_object('entry_user', self.master)
        user_name = self.user.get()
        self.passwd = self.builder.get_object('entry_pass', self.master)
        password = self.passwd.get()
        
        for user in list_user:
            if(user_name == user[0]):
                if(password == user[1]):
                    self.master.destroy()
                    self.master = tk.Tk()
                    self.master.title("Dash Board")
                    self.app = dashboard.DashboardApp(master= self.master, user_name= user_name, password= password)
                    self.app.run()
                    return
                else:
                    tmsg.showwarning(
                        title = 'Alert!', message = 'Wrong Password!')
                    return
        
        tmsg.showwarning(
            title = 'Alert!', message = "Do not exit this User!")
        return

    def run(self):
        self.mainwindow.mainloop()
      

#load user
def load_user():
    global list_user
    list_user = mysql_query.select_user(connection)


if __name__ == '__main__':
    
    #run login
    root = tk.Tk()
    root.title("Login")
    app = LoginApp(root)
    app.run()


    

