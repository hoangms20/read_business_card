from .info_image import Infoimage
import cv2
import numpy as np
from . import utlis
from skimage.filters import threshold_local
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
 
heightImg = 900
widthImg  = 550
si = 2048


def extract_text(info_image):
 
    #read image
    img = cv2.imread(info_image.file_path)
    img = cv2.resize(img,(si,si))

    for i in range(0,info_image.count_rotate):
        img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) # ADD GAUSSIAN BLUR
    imgThreshold = cv2.Canny(imgBlur,info_image.threshold1,info_image.threshold2) # APPLY CANNY BLUR
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations=2) # APPLY DILATION
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1)  # APPLY EROSION

    ## FIND ALL COUNTOURS
    imgBigContour = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # FIND ALL CONTOURS

    # FIND THE BIGGEST COUNTOUR
    biggest, maxArea = utlis.biggestContour(contours) # FIND THE BIGGEST CONTOUR
    print(biggest)
    if biggest.size != 0:
        biggest=utlis.reorder(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 255, 0), 20) # DRAW THE BIGGEST CONTOUR
        imgBigContour = utlis.drawRectangle(imgBigContour,biggest,2)

        pts1 = np.float32(biggest) # PREPARE POINTS FOR WARP
        pts2 = np.float32([[0, 0],[heightImg, 0], [0, widthImg],[heightImg, widthImg]]) # PREPARE POINTS FOR WARP
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (heightImg, widthImg))
 
        #REMOVE 20 PIXELS FORM EACH SIDE
        imgWarpColored=imgWarpColored[20:imgWarpColored.shape[0] - 20, 10:imgWarpColored.shape[1] - 10]
        #imgWarpColored = cv2.resize(imgWarpColored,(heightImg,widthImg))
 
        # APPLY ADAPTIVE THRESHOLD
        grayimg = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
        imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
        # imgAdaptiveThre= cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
        # imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
        # imgAdaptiveThre=cv2.medianBlur(imgAdaptiveThre,3)
        T = threshold_local(imgWarpGray, 21, offset = 10, method = "gaussian")
        imgWarpGray = (imgWarpGray > T).astype("uint8") * 255
        pil_img = Image.fromarray(imgWarpColored)
        txt = pytesseract.image_to_string(pil_img, lang='eng')
    else: 
        pil_img = Image.fromarray(imgGray)
        txt = pytesseract.image_to_string(pil_img, lang='eng')

    lines = txt.split("\n")
    tokens = []
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            tokens.append(line)

    for token in tokens:
        print(token)

    return tokens

if __name__ == "__main__":
    ifo = Infoimage("r_13.jpg")
    tokens = extract_text(ifo)