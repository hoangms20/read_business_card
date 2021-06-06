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



if __name__ == "__main__":
    root = Tk()
  
    # fixing geometry of GUI
    root.geometry('800x600')        
    root.maxsize(1000, 600)
    root.minsize(600, 600)
    root.title('Visiting card scanner')
    
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

    #Frame other
    f9 = Frame()
    f9.config(bg='white')
    laddress = Label(f9,text="Other:",width=7, height='1', font=('Times', 13))
    laddress.pack(side='left')

    taddress = Text(f9, height='1', font=('Times', 13))
    taddress.pack(side='right', fill='x')
    f9.pack(side="bottom")

    #Frame address
    f8 = Frame()
    f8.config(bg='white')
    laddress = Label(f8,text="Address:",width=7, height='1', font=('Times', 13))
    laddress.pack(side='left')

    taddress = Text(f8, height='1', font=('Times', 13))
    taddress.pack(side='right', fill='x')
    f8.pack(side="bottom")

    #Frame website
    f7 = Frame()
    f7.config(bg='white')
    lwebsite = Label(f7,text="Website:",width=7, height='1', font=('Times', 13))
    lwebsite.pack(side='left')

    twebsite = Text(f7, height='1', font=('Times', 13))
    twebsite.pack(side='right', fill='x')
    f7.pack(side="bottom")

    #Frame phone
    f6 = Frame()
    f6.config(bg='white')
    lphone = Label(f6,text="Phone:",width=7, height='1', font=('Times', 13))
    lphone.pack(side='left')

    tphone = Text(f6, height='1', font=('Times', 13))
    tphone.pack(side='right', fill='x')
    f6.pack(side="bottom")

    #Frame email
    f5 = Frame()
    f5.config(bg='white')
    lemail = Label(f5,text="Email:",width=7, height='1', font=('Times', 13))
    lemail.pack(side='left')

    temail = Text(f5, height='1', font=('Times', 13))
    temail.pack(side='right', fill='x')
    f5.pack(side="bottom")

    #Frame company
    f4 = Frame()
    f4.config(bg='white')
    lcompany = Label(f4,text="Company:",width=7, height='1', font=('Times', 13))
    lcompany.pack(side='left')

    tcompany = Text(f4, height='1', font=('Times', 13))
    tcompany.pack(side='right', fill='x')
    f4.pack(side="bottom")

    #Frame job
    f3 = Frame()
    f3.config(bg='white')
    ljob = Label(f3,text="Job:",width=7, height='1', font=('Times', 13))
    ljob.pack(side='left')

    tjob = Text(f3, height='1', font=('Times', 13))
    tjob.pack(side='right', fill='x')
    f3.pack(side="bottom")

    #Frame name
    f2 = Frame()
    f2.config(bg='white')
    lname = Label(f2,text="Name:",width=7, height='1', font=('Times', 13))
    lname.pack(side='left')

    tname = Text(f2, height='1', font=('Times', 13))
    tname.pack(side='right', fill='x')
    f2.pack(side="bottom")

    #button convert
    Button(root, text='Scan and Convert', bg='#F58D4B', font=('Times', 15),
        width=70, command=convert).pack(pady='10', side='bottom')

    root.mainloop()


    

