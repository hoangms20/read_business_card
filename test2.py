from tkinter import *
from PIL import Image, ImageTk

class GUI:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        #status bar
        self.bar = Frame(root, relief=RIDGE, borderwidth=5)
        self.bar.pack(side=TOP)

        self.iconPath = 'r_13.jpg'
        self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
        self.icon_size = Label(self.bar)
        self.icon_size.image = self.icon  # <== this is were we anchor the img object
        self.icon_size.configure(image=self.icon)
        self.icon_size.pack(side=LEFT)

root = Tk()


app = GUI(root)

root.mainloop()