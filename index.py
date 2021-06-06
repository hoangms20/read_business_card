# coding=utf-8
import os
import sys

import jsonpickle
from recognizer.card_recognition import recognize_contact
from recognizer.contact import Contact

# Visiting Card scanner GUI
  
# imported tkinter library
from tkinter import *
import tkinter.messagebox as tmsg    
  
# Pillow library for importing images
from PIL import Image, ImageTk
  
# library for filedialog (For file selection)
from tkinter import filedialog
  
# Pytesseract module importing
import pytesseract        
import os.path

#OpenCV
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#upload file
def upload_file():
    global filename, img
    global start, last
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
        title="Select Image File", 
        filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All File", "*.*")))

    if filename == "":
        t.delete(1.0, END)
        tmsg.showwarning(title = 'Alert!', message = 'Please provide proper formatted image')
        return
    else:
        image_size = 800
        img = Image.open(filename)
        orig_width, orig_height = img.size
        scale = (orig_height / orig_width) * image_size
        img = ImageTk.PhotoImage(img.resize((image_size, int(scale)), Image.ANTIALIAS))
        root1 = Toplevel()
        root1.geometry('800x800')        
        root1.title("Image upload")
        Label(root1, image=img).pack()
        p_label_var.set("Image uploaded successfully")
        l.config(fg = '#0CDD19')

    return


def convert():
    contact = recognize_contact(filename)
    print((' ' * 30))
    print((' * ' * 30))
    print((jsonpickle.encode(contact)))
    t.delete(1.0, END)
    t.insert(1.0, (jsonpickle.encode(contact)))



if __name__ == "__main__":
    root = Tk()
  
    # fixing geometry of GUI
    root.geometry('800x500')        
    root.maxsize(1000, 500)
    root.minsize(600, 500)
    root.title('Visiting card scanner')

    # Menu bar and navigation tab creation
    mainmenu = Menu(root)
    mainmenu.config(font = ('Times', 29))
    
    m1 = Menu(mainmenu, tearoff = 0)
    m1.add_command(label = 'Scan/Upload Visiting or Bussiness cards and get all the text of cards',
                font = ('Times', 13))
    root.config(menu = mainmenu)
    mainmenu.add_cascade(label = 'Aim', menu = m1)
    
    #title
    Label(text = 'Visiting card scanner', bg = '#FAD2B8',
        fg = '#39322D', font = ('Times', 18)).pack(fill = 'x')
    Label(text = 'Python GUI', bg = '#FAD2B8', fg ='#39322D', font=(
        'Times New Roman', 12, 'italic')).pack(fill='x')
    
    # create frame
    f1 = Frame()
    f1.config(bg='white')
    Label(f1, text='Browse photo to upload', width=20,
        font=('Times', 15), bg='white').pack(side='left')
    Label(f1, text='format: png/jpeg', bg='white',
        width=30).pack(side='right', padx=5)

    #button upload
    Button(f1, text='Upload card', bg='#F58D4B', font=('Times', 15),
        width=70, command=upload_file).pack(side='right')
    f1.pack(pady=10, fill='x')

    #label upload
    p_label_var = StringVar()
    p_label_var.set('Please upload an image to scan')
    l = Label(textvariable=p_label_var, fg='red', bg='white')
    l.pack()
    
    #show result
    t = Text(root, height='2', font=('Times', 13))
    t.pack(side='bottom', fill='x')
    t.insert(1.0, 'Text of converted card will be shown here...', END)

    #convert lablel
    c_label_var = StringVar()
    c_label_var.set('Ready for conversion')
    c_label = Label(textvariable=c_label_var)
    c_label.pack(side='bottom', anchor='w')

    #button convert
    Button(root, text='Scan and Convert', bg='#F58D4B', font=('Times', 15),
        width=70, command=convert).pack(pady='10', side='bottom')
    root.mainloop()


    

