import lookup
import thongkeapp
import login
import doimk
import scanapp
import list_search
import tkinter as tk
import tkinter.ttk as ttk


#dash board GUI
class DashboardApp:
    def __init__(self, master, user_name, password):
        # build ui
        self.dashboard = ttk.Frame(master)
        self.user_name = user_name
        self.password = password

        self.button_scan = ttk.Button(self.dashboard)
        self.cardicon_png = tk.PhotoImage(file='scanapp.png')
        self.button_scan.configure(image=self.cardicon_png)
        self.button_scan.grid(column='0', row='0')
        self.button_scan.configure(command=self.scan)

        self.button_list = ttk.Button(self.dashboard)
        self.list = tk.PhotoImage(file='list_search.png')
        self.button_list.configure(image=self.list)
        self.button_list.grid(column='1', row='0')
        self.button_list.configure(command=self.search_list)

        self.button_lookup = ttk.Button(self.dashboard)
        self.Business_icon = tk.PhotoImage(file='lookup.png')
        self.button_lookup.configure(image=self.Business_icon)
        self.button_lookup.grid(column='2', row='0')
        self.button_lookup.configure(command=self.look_up)

        self.button_thongke = ttk.Button(self.dashboard)
        self.metric = tk.PhotoImage(file='metric.png')
        self.button_thongke.configure(image=self.metric)
        self.button_thongke.grid(column='0', row='1')
        self.button_thongke.configure(command=self.thong_ke)

        self.button_doimk = ttk.Button(self.dashboard)
        self.doimk = tk.PhotoImage(file='doimk.png')
        self.button_doimk.configure(image=self.doimk)
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
        self.new_scan = tk.Toplevel(self.master)
        app = scanapp.ScanApp(self.new_scan)
        app.run

    def look_up(self):
        self.new_scan = tk.Toplevel(self.master)
        self.new_scan.title("Lookup")
        app = lookup.LookupApp(self.new_scan)
        app.run

    def search_list(self):
        self.new_scan = tk.Toplevel(self.master)
        self.new_scan.title("List")
        app = list_search.ListSearchApp(self.new_scan)
        app.run

    def thong_ke(self):
        self.new_scan = tk.Toplevel(self.master)
        self.new_scan.title("Thong ke Bao cao")
        app = thongkeapp.ThongkeApp(master= self.new_scan)
        app.run

    def doi_mk(self):
        self.new_scan = tk.Toplevel(self.master)
        self.new_scan.title("Change Password")
        app = doimk.DoimkApp(master= self.new_scan, user_name= self.user_name,password= self.password)
        app.run

    def exit(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.master.title("Login")
        self.app = login.LoginApp(self.master)
        self.app.run()

    def run(self):
        self.mainwindow.mainloop()

    
if __name__ == '__main__':
    root = tk.Tk()
    app = DashboardApp(root)
    app.run()