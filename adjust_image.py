import os
from recognizer import utlis
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import cv2
from PIL import Image, ImageTk, ImageDraw
from recognizer.info_image import Infoimage
import numpy as np

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
        self.cv2image = cv2.imread(self.file_path)
        self.cv2image = cv2.resize(self.cv2image, (800, 800)) # RESIZE IMAGE


        img = Image.open(file_path)
        self.img = img.resize((800, 800), Image.ANTIALIAS)
        self.info_img = Infoimage(file_path=file_path)
        self.master = master
        
        self.process_image(1)

    def show_image(self):
        img_show = ImageTk.PhotoImage(self.img)
        self.label_image.image = img_show 
        self.label_image.configure(image=img_show)

    def process_image(self,var):
        self.info_img.threshold1 = int(self.scale1.get())
        self.info_img.threshold2 = int(self.scale2.get())
        print((self.info_img.threshold1, self.info_img.threshold2))

        #process image
        self.cv2imgGray = cv2.cvtColor(self.cv2image, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE
        self.cv2imgBlur = cv2.GaussianBlur(self.cv2imgGray, (5, 5), 1) # ADD GAUSSIAN BLUR
        imgThreshold = cv2.Canny(self.cv2imgBlur,self.info_img.threshold1,self.info_img.threshold2) # APPLY CANNY BLUR
        kernel = np.ones((5, 5))
        imgDial = cv2.dilate(imgThreshold, kernel, iterations=2) # APPLY DILATION
        imgThreshold = cv2.erode(imgDial, kernel, iterations=1)  # APPLY EROSION
    
        ## FIND ALL COUNTOURS
        imgContours = self.cv2image.copy() # COPY IMAGE FOR DISPLAY PURPOSES
        contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # FIND ALL CONTOURS
        cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10) # DRAW ALL DETECTED CONTOURS

        self.img = Image.fromarray(imgContours)
        self.show_image()
    
    
    def rotate_button(self):
        self.info_img.count_rotate += 1
        self.info_img.count_rotate = self.info_img.count_rotate % 4
        self.cv2image = cv2.rotate(self.cv2image, cv2.ROTATE_90_COUNTERCLOCKWISE)
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

