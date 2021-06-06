import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "dashboard.ui")

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
    
    def scan(self):
        pass

    def look_up(self):
        pass

    def search_list(self):
        pass

    def thong_ke(self):
        pass

    def doi_mk(self):
        pass

    def exit(self):
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = DashboardApp(root)
    app.run()

