import cv2
import numpy as np

img = cv2.imread("dilation.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
countours, hierarchy  = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of countours =" + str(len(countours)))
#print(countours[0])

cv2.drawContours(img, countours, 0, [0, 255, 255], 3)
cv2.imshow('image', img)
cv2.imshow('image gray', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()