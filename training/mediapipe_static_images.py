import cv2
import mediapipe as mp
from hand_model import Hand_Model
from hand_class import Hand
import numpy as np
import os
from natsort import natsorted,ns,os_sorted

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

letter = "z"

final_data = np.empty(shape=[0,42])
_image_set_path = ".\\image_set\\" + letter+"\\"

IMAGE_FILES = []

for content in os_sorted(os.listdir(_image_set_path)):     #get image names
  if content.endswith(".jpg"):
    IMAGE_FILES.append(_image_set_path + content)


print(IMAGE_FILES)

#IMAGE_FILES = ['.\\training\\test_images\\hand_1.jpg','.\\training\\test_images\\no_hand.jpg','.\\training\\test_images\\hand_2.jpg']

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handed output 
    image = cv2.flip(cv2.imread(file), 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    print('Handedness:', results.multi_handedness)
    
    
    if not results.multi_hand_landmarks: #handle no hand case
      # current_data = np.empty(shape=[21,3])
      # current_data[:] = np.nan
      continue
    
    else: 
      for hand_landmarks in results.multi_hand_landmarks:
        current_ =  Hand(hand_landmarks)
        current_data = np.asarray(current_.landmark_data)
        print("SHAPE:",current_data.shape)
      
      image_height, image_width, _ = image.shape
      annotated_image = image.copy()
      mp_drawing.draw_landmarks(
        annotated_image,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_drawing_styles.get_default_hand_landmarks_style(),
        mp_drawing_styles.get_default_hand_connections_style())
      
      
      if not cv2.imwrite(
        ".\\training\\dataset\\"+letter+"\\annotated_image_" + str(idx) + ".png", cv2.flip(annotated_image, 1)):
        raise Exception("Could not write images")
    final_data = np.append(final_data,[current_data[0]], axis =0)
      
    print(final_data)      


  with open(".\\training\\unprepared_data\\"+letter+".csv", mode='w+') as csv_file: #saving line per frame in csv
    
    for index, per_image_result in enumerate(final_data):
      per_image_result=per_image_result.reshape(1,42)
      np.savetxt(csv_file, per_image_result,delimiter=',')
      

    

  

    