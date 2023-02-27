import cv2
import os
print("file exists?", os.path.exists('f1.mp4'))
capture = cv2.VideoCapture('f1.mp4')
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'.\\training\\out\\frame_{frameNr}.jpg', frame)
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()