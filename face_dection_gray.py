#! /usr/bin/python
# python2

import cv2 
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
myFace = cv2.imread('./images/ahmed.jpg')
gray_img = cv2.cvtColor(myFace, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5, minSize=(30,30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
print(faces)
for (x,y,w,h) in faces:
    cv2.rectangle(gray_img, (x, y), (x + w, y + h), (255, 255 , 0), 5)
cv2.imwrite('ahmed_face_gray.jpg', gray_img)







