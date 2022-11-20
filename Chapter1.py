###Importing an image
#import cv2
#img = cv2. imread("Resources/cao.jpeg")
#cv2.imshow("Output", img)
#cv2.waitKey(0)

###Import Video
#import cv2

#cap = cv2.VideoCapture("Resources/girafa.mp4")

#while True:
#    sucess, img = cap.read()
#    cv2.imshow("Result", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

###Run Webcam

import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)

while True:
    sucess, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break