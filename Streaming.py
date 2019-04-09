import cv2
cap = cv2. VideoCapture(-1)

if not cap.isOpened():
    print('Cannot open webcam')
else:
    while True:
        success, frame = cap. read()
        cv2.imshow(" Captured: " , frame)
        if cv2.waitKey(1) == 27:
            break
cap.release()
