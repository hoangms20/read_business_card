from db import mysql_connection, mysql_query
import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from datetime import datetime, timedelta

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "thongke.ui")

class ThongkeApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame1', master)
        builder.connect_callbacks(self)
        self.master = master

        self.label2 = builder.get_object('label2', master)
        self.label3 = builder.get_object('label3', master)
        self.label4 = builder.get_object('label4', master)
        self.label5 = builder.get_object('label5', master)

        self.tk()


    def tk(self):
        connection = mysql_connection.create_connection()

        data = mysql_query.select_all(connection)
        tongso = data.__len__()
        self.label2.configure(text="Tổng số đã quét là: "+str(tongso))

        #get datetime
        fromday = datetime.now()
        today = fromday + timedelta(days=1)
        today = today.date()
        fromday = fromday.date()
        today_string = today.strftime("%Y-%m-%d")
        fromday_string = fromday.strftime("%Y-%m-%d")
        print(fromday_string+"-------1-------"+today_string)
        valtime = (str(fromday_string), str(today_string))
        data = mysql_query.selectbytime(connection, valtime)
        tongso = data.__len__()
        self.label3.configure(text="Số đã quét ngày hôm nay: "+str(tongso))

        #get datetime
        fromday = datetime.now()
        today = fromday
        today = today.date()
        month = today.month
        year = today.year
        if(month < 12):
            month += 1
        else: 
            year += 1
            month = 1

        fromday = fromday.date()
        fromday = fromday.replace(day=1)
        today = today.replace(month=month, day=1, year=year)
        today_string = today.strftime("%Y-%m-%d")
        fromday_string = fromday.strftime("%Y-%m-%d")
        print(fromday_string+"-------2-------"+today_string)
        valtime = (str(fromday_string), str(today_string))
        data = mysql_query.selectbytime(connection, valtime)
        tongso = data.__len__()
        self.label5.configure(text="Số đã quét trong tháng này: "+str(tongso))

        #get datetime
        fromday = datetime.now()
        today = fromday
        s = today.weekday()
        today = today + timedelta(days= 7 - s)
        fromday = fromday - timedelta(days=s)
        today = today.date()
        fromday = fromday.date()
        today_string = today.strftime("%Y-%m-%d")
        fromday_string = fromday.strftime("%Y-%m-%d")
        print(fromday_string+"-------3-------"+today_string)
        valtime = (str(fromday_string), str(today_string))
        data = mysql_query.selectbytime(connection, valtime)
        tongso = data.__len__()
        self.label4.configure(text="Số đã quét trong tuần này: "+str(tongso))
    

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = ThongkeApp(root)
    app.run()

