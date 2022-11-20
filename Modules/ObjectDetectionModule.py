"""
Object detection Module
"""

import cv2

def findObject(img,objectCascade, scaleF = 1.1, minN = 4):
    imgObjects = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = objectCascade.detectMultiScale(imgGray, scaleF, minN)
    for (x,y,w,h) in objects:
        cv2.rectangle(imgObjects, (x,y), (x+w,y+h), (255, 0, 255), 2)

    return imgObjects, objects

def main():
    img = cv2.imread("../Resources/pessoa.jpeg")
    faceCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")
    imgObjects, objects = findObject(img, faceCascade)
    cv2.imshow("Image", imgObjects)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()