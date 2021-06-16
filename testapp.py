import cv2 
import pytesseract
from PIL import Image, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def adjust_sharpness(input_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Sharpness(image)
    out = enhancer_object.enhance(factor)
    return out

img = cv2.imread('card.jpg')
im = adjust_sharpness('card.jpg', 1.7)
im.show()
imgg = Image.open('card.jpg')
imgg.show()


# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(im, config=custom_config)
print(text)