from export_excel import export_file
from detail import DetailApp
from tkinter.constants import CENTER, E, NO, W
from db import mysql_connection, mysql_query
import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import tkinter.messagebox as tmsg  

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "lookup.ui")

class LookupApp:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('toplevel_lookup', master)
        builder.connect_callbacks(self)

        self.label_soluong = builder.get_object('soluong', master)
        self.combobox = builder.get_object('title_search', master)
        self.combobox['values'] = ['Show All'] + ['Name'] + ['Company'] + ['Job']
        self.combobox.current(0)

        self.enter_here = builder.get_object('enter_here', master)

        self.treeview_lookup = builder.get_object('treeview_lookup', master)

        # Add some style
        style = ttk.Style()
        #Pick a theme
        style.theme_use("default")
        # Configure our treeview colors

        style.configure("Treeview", 
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3"
            )
        # Change selected color
        style.map('Treeview', 
            background=[('selected', 'blue')])

        # Define Our Columns
        my_tree = self.treeview_lookup
        my_tree['columns'] = ("#", "Time", "Name", "Job", "Company", "Email", "Phone", "Website", "Address", "Other")

        # Formate Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("#", anchor=W, width=30)
        my_tree.column("Time", anchor=W, width=120)
        my_tree.column("Name", anchor=W, width=100)
        my_tree.column("Job", anchor=W, width=60)
        my_tree.column("Company", anchor=W, width=150)
        my_tree.column("Email", anchor=W, width=150)
        my_tree.column("Phone", anchor=W, width=150)
        my_tree.column("Website", anchor=W, width=150)
        my_tree.column("Address", anchor=W, width=700)
        my_tree.column("Other", anchor=W, width=200)

        # Create Headings 
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("#", text="#", anchor=W)
        my_tree.heading("Time", text="Time", anchor=W)
        my_tree.heading("Name", text="Name", anchor=W)
        my_tree.heading("Job", text="Job", anchor=W)
        my_tree.heading("Company", text="Company", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Phone", text="Phone", anchor=W)
        my_tree.heading("Website", text="Website", anchor=W)
        my_tree.heading("Address", text="Address", anchor=W)
        my_tree.heading("Other", text="Other", anchor=W)

        # Create striped row tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="lightblue")

        self.Lookup()


    def Lookup(self):
        column = self.combobox.get()
        val = self.enter_here.get()
        connection = mysql_connection.create_connection()

        if(column == 'Show All'):
            data = mysql_query.select_all(connection)
        else:
            if(column == "Name"):
                data = mysql_query.selectbyname(connection, val)
            else:
                if(column == "Company"):
                    data = mysql_query.selectbycompany(connection, val)
                else:
                    data = mysql_query.selectbyjob(connection, val)
        
        self.list_data = data
            
        self.remove_all()
        count=0

        for record in data:
            if count % 2 == 0:
                self.treeview_lookup.insert(parent='', index='end', iid=count, text="", values=(str(count), record[9], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow'))                
            else:
                self.treeview_lookup.insert(parent='', index='end', iid=count, text="", values=(str(count), record[9], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow'))

            count += 1
        
        self.label_soluong.configure(text="Tong so: " + str(count))

    # Remove all records
    def remove_all(self):
        records = self.treeview_lookup.get_children()
        for record in records:
            self.treeview_lookup.delete(record)

    def show_detail(self):
        # Grab record number
        selected = self.treeview_lookup.focus()
        # Grab record values
        values = self.treeview_lookup.item(selected, 'values')

        self.new_window = tk.Toplevel(self.mainwindow)
        app = DetailApp(master= self.new_window, val= values)
        app.run()

    def export_file(self):
        export_file(self.list_data)
        tmsg.showinfo(
            title = 'Alert!', message = "Export Successfully!")

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = LookupApp(root)
    app.run()

