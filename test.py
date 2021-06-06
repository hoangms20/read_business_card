from tkinter import *

root = Tk()
root.geometry('300x400+100+50')

some_widget = Toplevel(root)

top = some_widget.winfo_toplevel()
