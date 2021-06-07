import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import tkinter.messagebox as tmsg
import login

#import db
from db import mysql_connection
from db import mysql_query

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI_CHANGE_PASS = os.path.join(PROJECT_PATH, "doimk.ui")

#change password          
class DoimkApp:
    def __init__(self, master,  user_name, password):
        self.user_name = user_name
        self.password = password
        print("*"*30)
        print((self.user_name, self.password))
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI_CHANGE_PASS)
        self.mainwindow = builder.get_object('change_pass', master)
        self.master = master
        builder.connect_callbacks(self)
    
    def submit_change_pass(self):
        self.old_pass = self.builder.get_object('old_pass', self.master)
        old_pass = self.old_pass.get()
        self.new_pass = self.builder.get_object('new_pass', self.master)
        new_pass = self.new_pass.get()
        self.confirm_pass = self.builder.get_object('confirm_pass', self.master)
        confirm_pass = self.confirm_pass.get()

        print((confirm_pass,new_pass))

        if(old_pass == self.password):
            if(confirm_pass == new_pass):
                val = (new_pass, self.user_name)
                connection = mysql_connection.create_connection()
                mysql_query.update_pass(connection, val)
                tmsg.showwarning(title = 'Alert!', message = 'Change Password Successfully!')
                self.master.destroy()
            else:
                tmsg.showwarning(title = 'Alert!', message = 'Password does not match!')
        else:
            tmsg.showwarning(title = 'Alert!', message = 'Wrong Password!')
    def run(self):
        self.mainwindow.mainloop() 

if __name__ == '__main__':
    root = tk.Tk()
    app = DoimkApp(root)
    app.run()
