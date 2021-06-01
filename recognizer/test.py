import cv2

import numpy as np

img = cv2.imread('graimage.png') 

img = cv2.resize(img,(400,500))

gray = img.copy()

(thresh, im_bw) = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY )

derp,contours,hierarchy = cv2.findContours(im_bw,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))