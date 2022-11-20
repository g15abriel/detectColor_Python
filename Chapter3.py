import cv2
import numpy as np

img = cv2.imread("Resources/cao.jpeg")
print(img.shape)

imgResize1 = cv2.resize(img, (2*img.shape[1],2*img.shape[0]))
imgResize2 = cv2.resize(img, (0,0),None,0.5,0.5)

imgCrop = img[50:100,100:150]

cv2.imshow("Image", img)
cv2.imshow("Image Quadruplicada", imgResize1)
cv2.imshow("Image Reduzida", imgResize2)
cv2.imshow("Image Crop", imgCrop)

cv2.waitKey(0)