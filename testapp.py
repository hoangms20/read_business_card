import os
import tkinter as tk
from tkinter.constants import LEFT
import tkinter.ttk as ttk
import pygubu
from PIL import Image, ImageTk

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "testapp.ui")

class TestApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame_root', master)
        builder.connect_callbacks(self)
        self.master = master

        img = Image.open("r_13.jpg")
        self.img = img
        
        self.show_image()

    def show_image(self):
        img_show = ImageTk.PhotoImage(Image.open("r_13.jpg").resize((800, 800), Image.ANTIALIAS))
        fra = tk.Frame(self.master)
        label = tk.Label(fra)
        label.imge = img_show
        label.configure(image=img_show)
        label.pack(side=LEFT)
    

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = TestApp(root)
    app.run()

