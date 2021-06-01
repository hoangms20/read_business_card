import cv2

import numpy as np

img = cv2.imread('samples/bc_ref/r_1.jpg') 

img = cv2.resize(img,(400,500))

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

(thresh, im_bw) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY )

contours,hierarchy = cv2.findContours(im_bw,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))