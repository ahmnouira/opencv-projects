#! /usr/bin/python 
#python


import cv2      					        # import OpenCV lib
cap = cv2. VideoCapture(0)            	        # create cap object : 0 ID of the camera
# sets the Classifier
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')

if not cap.isOpened():                     	        # check if the camera is opened
    print('Cannot open webcam')

else:
    while True:                                                   # loop for ever
        success, frame = cap. read()                  # read frames
# detect faces  
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3,minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

        for (x,y,w,h) in faces:                              # for all faces in the frame          
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255 , 255), 5)   # draw  yellow  rectangle
# (x, y) coordinates, w : width, h:height   

        cv2.imshow(" Captured: " , frame)         # show frames in the window
        if cv2.waitKey(1) == 27:                         # check if the user press ESC or not  
            break
cap.release()                                                  # stop 
cv2. destroyAllWindows()                              # destroy cv2 Allwindows
