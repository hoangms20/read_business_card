import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "thongke.ui")

class ThongkeApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame1', master)
        builder.connect_callbacks(self)
    

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = ThongkeApp(root)
    app.run()

