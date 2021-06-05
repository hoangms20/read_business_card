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


root = Tk()
  
# fixing geometry of GUI
root.geometry('800x500')        
root.maxsize(1000, 500)
root.minsize(600, 500)
root.title('Visiting card scanner')

#upload file
def upload_file():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
        title="Select Image File", 
        filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All File", "*.*")))
    img = ImageTk.PhotoImage(Image.open(filename))
    root1 = Toplevel()
    root1.title("Image")
    print(filename)
    img2 = cv2.imread(filename)
    gray = cv2.cvtColor(img2, code = cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    t.delete(1.0, END)
    t.insert(1.0, text)
    Label(root1, image=img).pack()
    root1.mainloop() 


    #if	filename == '':

def convert():
    # gray = cv2.cvtColor(src = filename, code = cv2.COLOR_BGR2GRAY)
	# text = pytesseract.image_to_string(filename)
	# t.delete(1.0, END)
	# t.insert(1.0, text)
	# root1 = Toplevel()
	# root1.title('Uploaded image')
	# img1 = ImageTk.PhotoImage(Image.open(filename))
	# Label(root1, image=img1).pack()
	# root1.mainloop()
    return


# Menu bar and navigation tab creation
mainmenu = Menu(root)
mainmenu.config(font = ('Times', 29))
  
m1 = Menu(mainmenu, tearoff = 0)
m1.add_command(label = 'Scan/Upload Visiting or Bussiness cards and get all the text of cards',
               font = ('Times', 13))
root.config(menu = mainmenu)
mainmenu.add_cascade(label = 'Aim', menu = m1)
  
Label(text = 'Visiting card scanner', bg = '#FAD2B8',
      fg = '#39322D', font = ('Times', 18)).pack(fill = 'x')
Label(text = 'Python GUI', bg = '#FAD2B8', fg ='#39322D', font=(
    'Times New Roman', 12, 'italic')).pack(fill='x')
  
f1 = Frame()
f1.config(bg='white')
Label(f1, text='Browse photo to upload', width=20,
      font=('Times', 15), bg='white').pack(side='left')
Label(f1, text='format: png/jpeg', bg='white',
      width=30).pack(side='right', padx=5)
Button(f1, text='Upload card', bg='#F58D4B', font=('Times', 15),
       width=70, command=upload_file).pack(side='right')
f1.pack(pady=10, fill='x')
p_label_var = StringVar()
p_label_var.set('Please upload an image to scan')
l = Label(textvariable=p_label_var, fg='red', bg='white')
l.pack()
  
t = Text(root, height='9', font=('Times', 13))
t.pack(side='bottom', fill='x')
t.insert(1.0, 'Text of converted card will be shown here...', END)
c_label_var = StringVar()
c_label_var.set('Ready for conversion')
c_label = Label(textvariable=c_label_var)
c_label.pack(side='bottom', anchor='w')
Button(root, text='Scan and Convert', bg='#F58D4B', font=('Times', 15),
       width=70, command=convert).pack(pady='10', side='bottom')
root.mainloop()


# if __name__ == "__main__":
#     # app.run()
#     sample_path = 'samples/bc_ref/r_13.jpg'
#     #sample_path = 'card.png'
#     # extract_2(sample_path)
#     # sample_path = 'samples/BC_5.jpg'

#     # sample_path = 'business_cards/Droid/010.jpg'
#     contact = recognize_contact(sample_path)
#     print((' ' * 30))
#     print((' * ' * 30))
#     print((jsonpickle.encode(contact)))
#     print((' * ' * 30))

