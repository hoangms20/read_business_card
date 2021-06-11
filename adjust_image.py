import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import cv2
from PIL import Image, ImageTk, ImageDraw
from recognizer.info_image import Infoimage

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "adjust_image.ui")

class AdjustImageApp:
    def __init__(self, master, file_path=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame_root', master)
        builder.connect_callbacks(self)

        self.label_image = builder.get_object('label_image', master)
        self.scale1 = builder.get_object('scale1', master)
        self.scale2 = builder.get_object('scale2', master)

        self.file_path = file_path
        image = cv2.imread(file_path)
        self.unsaved_image = image
        self.saved_image = image

        img = Image.open("r_13.jpg")
        self.img = img
        self.info_img = Infoimage(file_path=file_path)
        
        self.show_image()

    def show_image(self):
        img_show = ImageTk.PhotoImage(self.img.resize((800, 800), Image.ANTIALIAS))
        self.label_image.image = img_show 
        self.label_image.configure(image=img_show)

    def process_image(self,var):
        self.info_img.threshold1 = int(self.scale1.get())
        self.info_img.threshold2 = int(self.scale2.get())
        print((self.info_img.threshold1, self.info_img.threshold2))
    
    def rotate_button(self):
        self.info_img.count_rotate += 1
        self.info_img.count_rotate = self.info_img.count_rotate % 4
        self.img = self.img.transpose(Image.ROTATE_90)
        self.show_image()

    def save_image(self):
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = AdjustImageApp(root)
    app.run()

