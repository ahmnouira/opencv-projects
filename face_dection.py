#! /usr/bin/python
# python2

import cv2
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
original_image_path = './images/people.jpg'
image = cv2.imread(original_image_path)
faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=3,minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
print(faces)
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0 , 255), 5)
cv2.imwrite('people_faces.jpg', image)
