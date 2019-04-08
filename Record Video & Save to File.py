#!/usr/bin/env python
# coding: utf-8

# OpenCV Record Video & Save to File




import cv2                          			 					 # import OpenCV
cameraCapture = cv2.VideoCapture(0)   					 # start the capture from then webcam
fps = 9                            			 					 # set the fps an assumption 

size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),  # gets the size
int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print("size", size)                       							# print the size
print("fps", fps)                         							# print fps

videoWriter = cv2.VideoWriter(            					        # write the file 
'OutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), 			#..._fourcc : codec type
fps, size)
success, frame = cameraCapture.read()    					# start recording
time_rec = 10 * fps             								# record for 10 seconds 
while success and time_rec > 0:
    videoWriter.write(frame)       							# write each frame
    success, frame = cameraCapture.read()   
    time_rec -= 1    										
cameraCapture.release()








# In[ ]:




