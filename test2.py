import cv2

img = cv2.imread("r_13.jpg")
img = cv2.resize(img,(1000,1000))
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("aa",img)
cv2.waitKey(0)