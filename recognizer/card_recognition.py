import cv2
import jsonpickle
import pytesseract
import re

from .pattern_recognition import common_name_recognition as name_recog
from .pattern_recognition.address_name_recognition import *
from .pattern_recognition.email_recognition import is_email
from .pattern_recognition.job_title_recognition import is_job_title
from .pattern_recognition.phone_recognition import is_phone
from .pattern_recognition.website_recognition import is_website
from .pattern_recognition.company_name_recognition import is_company_name
from . import card_region_detector as region_detector


from PIL import Image

from .contact import Contact
from array import *

DEBUG = False

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def recognize_contact(img_path):
    txt = extract(img_path)
    tokens = tokenizer(txt)
    contact = Contact()

    mask = array('i', [])

    for token in tokens:
        mask.append(0)
        print(token)

    

    print("****find****")
    #contact.name = name_recog.find_best_guessed_name(tokens)[2]
    i = -1
    l = len(mask)

    for token in tokens:
        i += 1

        if mask[i] != 0 :
            continue

        if is_website(token):
            mask[i] = 1
            contact.website = token
            continue

        if is_email(token):
            mask[i] = 2
            contact.emails.append(token)
            continue

        if is_phone(token):
            mask[i] = 3
            contact.phones.append(token)
            continue

        if is_job_title(token):
            mask[i] = 4
            contact.job_title.append(token)
            continue

        if is_address(token):
            mask[i] = 5
            contact.addr.append(token)
            continue

        if is_company_name(token):
            mask[i] = 6
            contact.company = token
            continue

        if name_recog.is_en_name(token) or name_recog.is_jp_name(token) or name_recog.is_vn_name(token):
            mask[i] = 7
            contact.name = token
            continue
        
        j = i - 1
        if(j >= 0 and j <= l - 1):
            if mask[j] == 4 or mask[j] == 7:
                mask[i] = 4
                contact.job_title.append(token)
                continue
            
            if mask[j] == 5 and tokens[j][len(tokens[j]) - 1] == ',':
                mask[i] = 5
                lengcon = len(contact.addr)
                contact.addr[lengcon - 1] += token
                continue

            if mask[j] == 6:
                mask[i] = 5
                contact.addr.append(token)
                continue

        contact.other_info.append(token)
        
    print("****finished****")
    print(tokens)
    i = -1
    for token in tokens:
        i+=1
        print(token +"-------" + str(mask[i]))
    return contact



# Extract business card border, then recognize text
def extract(img_path):
    image_size = 500

    # Read
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    orig_width, orig_height = img.shape

    # Make image smaller for faster processing
    scale = orig_width / image_size
    resized_img = cv2.resize(img, (image_size, int(orig_height / scale + 1)), None)

    #Crop text region
    cropped = region_detector.crop_text_region(resized_img)

    # Restore Original region
    orig_crop = [int(round(x * scale)) for x in cropped]
    text_region = img[orig_crop[1]: orig_crop[3], orig_crop[0]: orig_crop[2]]


    # Convert to Image object to make tesseract happy
    pil_img = Image.fromarray(text_region)
    txt = pytesseract.image_to_string(pil_img, lang='eng')

    global DEBUG
    if DEBUG:
        pil_img.show()
        print('txt', txt)
        cv2.rectangle(resized_img, (cropped[0], cropped[1]), (cropped[2], cropped[3]), (0, 255, 0), 1)
        cv2.imshow('resized', resized_img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return txt


def tokenizer(txt):
    lines = txt.split("\n")
    tokens = []
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            tokens.append(line)

    return tokens

if __name__ == '__main__':
    # sample_path = 'business_cards/Reference/011.jpg'
    # sample_path = '010.jpg'
    sample_path = 'samples/bc_ref/r_1.jpg'
    # extract_2(sample_path)
    # sample_path = 'samples/BC_5.jpg'

    # sample_path = 'business_cards/Droid/010.jpg'
    contact = recognize_contact(sample_path)
    print((' ' * 30))
    print((' * ' * 30))
    print((jsonpickle.encode(contact)))

