import os
import tkinter as tk
from tkinter.constants import END
import tkinter.ttk as ttk
import pygubu
import tkinter.messagebox as tmsg  

#import db
from db import mysql_connection
from db import mysql_query

# Pillow library for importing images
from PIL import Image, ImageTk
  
# library for filedialog (For file selection)
from tkinter import Frame, StringVar, Toplevel, filedialog

#import modules
import jsonpickle
from recognizer.card_recognition import recognize_contact
from recognizer.contact import Contact

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "login.ui")
PROJECT_UI_CHANGE_PASS = os.path.join(PROJECT_PATH, "doimk.ui")

#login GUI
class LoginApp:
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('login', master)
        builder.connect_callbacks(self)
    
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
                    self.app = DashboardApp(self.master)
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

#dash board GUI
class DashboardApp:
    def __init__(self, master):
        # build ui
        self.dashboard = ttk.Frame(master)

        self.button_scan = ttk.Button(self.dashboard)
        self.cardicon_png = tk.PhotoImage(file='cardicon_png.png')
        self.button_scan.configure(image=self.cardicon_png)
        self.button_scan.grid(column='0', row='0')
        self.button_scan.configure(command=self.scan)

        self.button_list = ttk.Button(self.dashboard)
        self.list = tk.PhotoImage(file='list.png')
        self.button_list.configure(image=self.list)
        self.button_list.grid(column='1', row='0')
        self.button_list.configure(command=self.search_list)

        self.button_lookup = ttk.Button(self.dashboard)
        self.Business_icon = tk.PhotoImage(file='Business_icon.png')
        self.button_lookup.configure(image=self.Business_icon)
        self.button_lookup.grid(column='2', row='0')
        self.button_lookup.configure(command=self.look_up)

        self.button_thongke = ttk.Button(self.dashboard)
        self.metric = tk.PhotoImage(file='metric.png')
        self.button_thongke.configure(image=self.metric)
        self.button_thongke.grid(column='0', row='1')
        self.button_thongke.configure(command=self.thong_ke)

        self.button_doimk = ttk.Button(self.dashboard)
        self.password = tk.PhotoImage(file='password.png')
        self.button_doimk.configure(image=self.password)
        self.button_doimk.grid(column='1', row='1')
        self.button_doimk.configure(command=self.doi_mk)

        self.button_exit = ttk.Button(self.dashboard)
        self.exit_png = tk.PhotoImage(file='exit_png.png')
        self.button_exit.configure(image=self.exit_png)
        self.button_exit.grid(column='2', row='1')
        self.button_exit.configure(command=self.exit)
		
        self.dashboard.configure(height='200', width='200')
        self.dashboard.grid(column='0', row='0')

        # Main widget
        self.mainwindow = self.dashboard
        self.master = master
    
    def scan(self):
        self.new_scan = Toplevel(self.master)
        app = ScanApp(self.new_scan)
        app.run

    def look_up(self):
        pass

    def search_list(self):
        pass

    def thong_ke(self):
        pass

    def doi_mk(self):
        self.new_scan = Toplevel(self.master)
        self.new_scan.title("Change Password")
        app = DoimkApp(self.new_scan)
        app.run

    def exit(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.title("Login")
        self.app = LoginApp(self.master)
        self.app.run()

    def run(self):
        self.mainwindow.mainloop()

#Scan GUI
class ScanApp:

    def __init__(self, master):

        self.master = master
        self.master.geometry('800x600')        
        self.master.maxsize(1000, 600)
        self.master.minsize(600, 600)
        self.master.title('Visiting card scanner')
        
        #title
        tk.Label(self.master, text = 'Visiting card scanner', bg = '#FAD2B8',
            fg = '#39322D', font = ('Times', 18)).pack(fill = 'x')
        tk.Label(self.master, text = 'Python GUI', bg = '#FAD2B8', fg ='#39322D', font=(
            'Times New Roman', 12, 'italic')).pack(fill='x')
        
        # create frame
        f1 = tk.Frame(self.master)
        f1.config(bg='white')
        tk.Label(f1, text='Browse photo to upload', width=20,
            font=('Times', 15), bg='white').pack(side='left')
        tk.Label(f1, text='format: png/jpeg', bg='white',
            width=30).pack(side='right', padx=5)

        #button upload
        self.button_upload_file = tk.Button(f1)
        self.button_upload_file.configure(text="Upload card")
        self.button_upload_file.configure(bg='#F58D4B')
        self.button_upload_file.configure(font=('Times', 15))
        self.button_upload_file.configure(width=70)
        self.button_upload_file.pack(side='right')
        self.button_upload_file.configure(command=self.upload_file)
        f1.pack(pady=10, fill='x')

        #label upload
        global p_label_var
        global l
        p_label_var = StringVar()
        p_label_var.set('Please upload an image to scan')
        l = tk.Label(self.master,textvariable=p_label_var, fg='red', bg='white')
        l.pack()

        #button save
        self.button_save = tk.Button(self.master)
        self.button_save.configure(text="Save")
        self.button_save.configure(bg='#F58D4B')
        self.button_save.configure(font=('Times', 15))
        self.button_save.configure(width=70)
        self.button_save.pack(pady='10', side='bottom')
        self.button_save.configure(command=self.save_data)

        #Frame other
        f9 = tk.Frame(self.master)
        f9.config(bg='white')
        lother = tk.Label(f9,text="Other:",width=7, height='1', font=('Times', 13))
        lother.pack(side='left')

        self.tother = tk.Text(f9, height='1', font=('Times', 13))
        self.tother.pack(side='right', fill='x')
        f9.pack(side="bottom")

        #Frame address
        f8 = tk.Frame(self.master)
        f8.config(bg='white')
        laddress = tk.Label(f8,text="Address:",width=7, height='1', font=('Times', 13))
        laddress.pack(side='left')

        self.taddress = tk.Text(f8, height='1', font=('Times', 13))
        self.taddress.pack(side='right', fill='x')
        f8.pack(side="bottom")

        #Frame website
        f7 = tk.Frame(self.master)
        f7.config(bg='white')
        lwebsite = tk.Label(f7,text="Website:",width=7, height='1', font=('Times', 13))
        lwebsite.pack(side='left')

        self.twebsite = tk.Text(f7, height='1', font=('Times', 13))
        self.twebsite.pack(side='right', fill='x')
        f7.pack(side="bottom")

        #Frame phone
        f6 = tk.Frame(self.master)
        f6.config(bg='white')
        lphone = tk.Label(f6,text="Phone:",width=7, height='1', font=('Times', 13))
        lphone.pack(side='left')

        self.tphone = tk.Text(f6, height='1', font=('Times', 13))
        self.tphone.pack(side='right', fill='x')
        f6.pack(side="bottom")

        #Frame email
        f5 = tk.Frame(self.master)
        f5.config(bg='white')
        lemail = tk.Label(f5,text="Email:",width=7, height='1', font=('Times', 13))
        lemail.pack(side='left')

        self.temail = tk.Text(f5, height='1', font=('Times', 13))
        self.temail.pack(side='right', fill='x')
        f5.pack(side="bottom")

        #Frame company
        f4 = tk.Frame(self.master)
        f4.config(bg='white')
        lcompany = tk.Label(f4,text="Company:",width=7, height='1', font=('Times', 13))
        lcompany.pack(side='left')

        self.tcompany = tk.Text(f4, height='1', font=('Times', 13))
        self.tcompany.pack(side='right', fill='x')
        f4.pack(side="bottom")

        #Frame job
        f3 = tk.Frame(self.master)
        f3.config(bg='white')
        ljob = tk.Label(f3,text="Job:",width=7, height='1', font=('Times', 13))
        ljob.pack(side='left')

        self.tjob = tk.Text(f3, height='1', font=('Times', 13))
        self.tjob.pack(side='right', fill='x')
        f3.pack(side="bottom")

        #Frame name
        f2 = tk.Frame(self.master)
        f2.config(bg='white')
        lname = tk.Label(f2,text="Name:",width=7, height='1', font=('Times', 13))
        lname.pack(side='left')

        self.tname = tk.Text(f2, height='1', font=('Times', 13))
        self.tname.pack(side='right', fill='x')
        f2.pack(side="bottom")

        #button convert
        self.button_convert = tk.Button(self.master)
        self.button_convert.configure(text="Scan and Convert")
        self.button_convert.configure(bg='#F58D4B')
        self.button_convert.configure(font=('Times', 15))
        self.button_convert.configure(width=70)
        self.button_convert.pack(pady='10', side='bottom')
        self.button_convert.configure(command=self.convert)
        self.mainwindow = self.master

    def run(self):
        self.mainwindow.mainloop()

    #upload file
    def upload_file(self):
        global filename, img
        global start, last
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
            title="Select Image File", 
            filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All File", "*.*")))

        if filename == "":
            tmsg.showwarning(title = 'Alert!', message = 'Please provide proper formatted image')
            return
        else:
            image_size = 800
            img = Image.open(filename)
            orig_width, orig_height = img.size
            scale = (orig_height / orig_width) * image_size
            img = ImageTk.PhotoImage(img.resize((image_size, int(scale)), Image.ANTIALIAS))
            root1 = tk.Toplevel()
            root1.geometry('800x800')        
            root1.title("Image upload")
            tk.Label(root1, image=img).pack()
            p_label_var.set("Image uploaded successfully")
            l.config(fg = '#0CDD19')

        return

    def convert(self):
        contact = recognize_contact(filename)
        print((' ' * 30))
        print((' * ' * 30))
        print((jsonpickle.encode(contact)))
        self.tname.delete(1.0, END)
        self.tname.insert(1.0, contact.name)

        self.tjob.delete(1.0, END)
        self.tjob.insert(1.0, contact.job_title)

        self.tcompany.delete(1.0, END)
        self.tcompany.insert(1.0, contact.company)

        self.temail.delete(1.0, END)
        self.temail.insert(1.0, contact.emails)

        self.tphone.delete(1.0, END)
        self.tphone.insert(1.0, contact.phones)

        self.twebsite.delete(1.0, END)
        self.twebsite.insert(1.0, contact.website)

        self.taddress.delete(1.0, END)
        self.taddress.insert(1.0, contact.addr)
        
    def save_data(self):
        # get data
        getname = self.tname.get("1.0", END)
        getjob = self.tjob.get("1.0", END)
        getcompany = self.tcompany.get("1.0", END)
        getemail = self.temail.get("1.0", END)
        getphone = self.tphone.get("1.0", END)
        getweb = self.twebsite.get("1.0", END)
        getaddr = self.taddress.get("1.0", END)
        getother = self.tother.get("1.0", END)

        # Insert Into Table
        val = (getname[:len(getname) - 1], getjob[:len(getjob) - 1], getcompany[:len(getcompany) - 1], getemail[:len(getemail) - 1],
                 getphone[:len(getphone) - 1], getweb[:len(getweb) - 1], getaddr[:len(getaddr) - 1], getother[:len(getother) - 1])
        print("**************val*****************")
        print(val)
        mysql_query.insert_query(connection, val)
        # Commit Changes
        tmsg.showinfo(title = 'Alert!', message = 'Save Successfully!') 

#change password          
class DoimkApp:
    def __init__(self, master):
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

        if(old_pass == password):
            if(confirm_pass == new_pass):
                val = (new_pass, user_name)
                mysql_query.update_pass(connection, val)
                tmsg.showwarning(title = 'Alert!', message = 'Change Password Successfully!')
                self.master.destroy()
            else:
                tmsg.showwarning(title = 'Alert!', message = 'Password does not match!')
        else:
            tmsg.showwarning(title = 'Alert!', message = 'Wrong Password!')
    def run(self):
        self.mainwindow.mainloop()           

#load user
def load_user():
    global list_user
    list_user = mysql_query.select_user(connection)

    # for result in list_user:
    #     for i in result:
    #         if(i != None):
    #             print(i)

    #     print("**"*30)

if __name__ == '__main__':
    #load user
    global connection
    connection = mysql_connection.create_connection()
    load_user()
    
    #run login
    root = tk.Tk()
    root.title("Login")
    app = LoginApp(root)
    app.run()

    # root.title("Dash Board")
    # app = DashboardApp(root)
    # app.run()

    

