import cv2 
# create cap object      					        
cap = cv2. VideoCapture(0)            	    
# check if the camera is opened
if not cap.isOpened():                     	
    print('Cannot open webcam')
else:
    while True:
        # read frames
        success, frame = cap. read()
        # show frames in the window         
        cv2.imshow("Captured: " , frame)
        # check if the user press ESC or not   
        if cv2.waitKey(1) == 27:             
            break
# stop         
cap.release()
# destroy cv2 window                              
cv2.destroyAllWindows()                 