import cv2      					# import OpenCv lib
cap = cv2. VideoCapture(0)            	# create cap object 

if not cap.isOpened():                     	# check if the camera is opened
    print('Cannot open webcam')
else:
    while True:
        success, frame = cap. read()           # read frames 
        cv2.imshow(" Captured: " , frame)   # show frames in the window
        if cv2.waitKey(1) == 27:                   # check if the user press ESC or not  
            break
cap.release()                                            # stop 
cv2. destroyAllWindows()                        # destroy cv2 window
