import os
import tkinter as tk
from tkinter.constants import END
import tkinter.ttk as ttk
import tkinter.messagebox as tmsg
from datetime import datetime

# library for filedialog (For file selection)
from tkinter import filedialog

# Pillow library for importing images
from PIL import Image, ImageTk

#import modules
import jsonpickle
from recognizer.card_recognition import recognize_contact
from recognizer.contact import Contact

#import db
from db import mysql_connection
from db import mysql_query

#Scan GUI
class DetailApp:

    def __init__(self, master, val):

        self.master = master
        self.master.geometry('1000x360')        
        self.master.maxsize(1000, 600)
        self.master.minsize(800, 300)
        self.master.title('Detail')

        self.mainwindow = master
        
        #title
        tk.Label(self.master, text = 'Detail #' + val[0], bg = '#FAD2B8',
            fg = '#39322D', font = ('Times', 18, 'bold')).pack(fill = 'x')
        

        #Frame other
        f9 = tk.Frame(self.master)
        lother = tk.Label(f9,text="Others:",width=7, height='1', font=('Times', 13))
        lother.pack(side='left', pady= 5)

        self.tother = tk.Label(f9, text = val[9], height='1', font=('Times', 12))
        self.tother.pack(side='left', fill='x', pady= 5)
        f9.pack(side="bottom", fill = 'x')

        #Frame address
        f8 = tk.Frame(self.master)
        laddress = tk.Label(f8,text="Address:",width=7, height='1', font=('Times', 13))
        laddress.pack(side='left', pady= 5)

        self.taddress = tk.Label(f8, text = val[8], height='1', font=('Times', 12))
        self.taddress.pack(side='left', fill='x', pady= 5)
        f8.pack(side="bottom", fill = 'x')

        #Frame website
        f7 = tk.Frame(self.master)
        lwebsite = tk.Label(f7,text="Website:",width=7, height='1', font=('Times', 13))
        lwebsite.pack(side='left', pady= 5)

        self.twebsite = tk.Label(f7, text = val[7], height='1', font=('Times', 12))
        self.twebsite.pack(side='left', fill='x', pady= 5)
        f7.pack(side="bottom", fill = 'x')

        #Frame phone
        f6 = tk.Frame(self.master)
        lphone = tk.Label(f6,text="Phone:",width=7, height='1', font=('Times', 13))
        lphone.pack(side='left', pady= 5)

        self.tphone = tk.Label(f6, text = val[6], height='1', font=('Times', 12))
        self.tphone.pack(side='left', fill='x', pady= 5)
        f6.pack(side="bottom", fill = 'x')

        #Frame email
        f5 = tk.Frame(self.master)
        lemail = tk.Label(f5,text="Email:",width=7, height='1', font=('Times', 13))
        lemail.pack(side='left', pady= 5)

        self.temail = tk.Label(f5, text = val[5], height='1', font=('Times', 12))
        self.temail.pack(side='left', fill='x', pady= 5)
        f5.pack(side="bottom", fill = 'x')

        #Frame company
        f4 = tk.Frame(self.master)
        lcompany = tk.Label(f4,text="Company:",width=7, height='1', font=('Times', 13))
        lcompany.pack(side='left', pady= 5)

        self.tcompany = tk.Label(f4, text = val[4], height='1', font=('Times', 12))
        self.tcompany.pack(side='left', fill='x', pady= 5)
        f4.pack(side="bottom", fill = 'x')

        #Frame job
        f3 = tk.Frame(self.master)
        ljob = tk.Label(f3,text="Job:",width=7, height='1', font=('Times', 13))
        ljob.pack(side='left', pady= 5)

        self.tjob = tk.Label(f3, text = val[3], height='1', font=('Times', 12))
        self.tjob.pack(side='left', fill='x', pady= 5)
        f3.pack(side="bottom", fill = 'x')

        #Frame name
        f2 = tk.Frame(self.master)
        lname = tk.Label(f2,text="Name:",width=7, height='1', font=('Times', 13))
        lname.pack(side='left', pady= 5)

        self.tname = tk.Label(f2, text = val[2], height='1', font=('Times', 12))
        self.tname.pack(side='left', fill='x', pady= 5)
        f2.pack(side="bottom", fill = 'x')

        #Frame time
        f11 = tk.Frame(self.master)
        lname = tk.Label(f11,text="Time:",width=7, height='1', font=('Times', 13))
        lname.pack(side='left', pady= 5)

        self.tname = tk.Label(f11, text = val[1], height='1', font=('Times', 12))
        self.tname.pack(side='left', fill='x', pady= 5)
        f11.pack(side="bottom", fill = 'x')


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = DetailApp(root)
    app.run()