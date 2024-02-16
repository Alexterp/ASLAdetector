import cv2
import os

letter = 'complete'
print("file exists?", os.path.exists(letter+'.mp4'))
capture = cv2.VideoCapture(letter+'.mp4')
frameNr = 0

while (True):
    success, frame = capture.read()
    if success:
        cv2.imwrite(f'.\\image_set\\complete\\{frameNr}.jpg', frame)
 
    else:
        break
 
    frameNr = frameNr+1
capture.release()