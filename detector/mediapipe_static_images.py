import cv2
import csv
import mediapipe as mp
from hand_model import Hand_Model
from hand_class import Hand
from google.protobuf.json_format import MessageToDict
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
final_data = np.empty(shape=[0,21,3])

# For static images:
IMAGE_FILES = ['.\detector\what.jpg','.\detector\wht2.jpg']

#myhand = HAND()

#def save_to_csv(final_array):
  
  

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.flip(cv2.imread(file), 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    # Print handedness and draw hand landmarks on the image.
    print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    
    
    
    for hand_landmarks in results.multi_hand_landmarks:
      #print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z })'
      )
      
      current_ =  Hand(idx,hand_landmarks)
      #print(current_.landmark_data.ndim)
      #print(final_data.ndim)
      final_data = np.append(final_data,[current_.landmark_data], axis =0)      
        
      #print (current_.landmark_data)
      
      
      mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
      
    
        
    cv2.imwrite(
        'annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))
  
  #print('Final data',final_data)
  
  with open("result.csv", mode='w+') as csv_file:
    
    for index, per_image_result in enumerate(final_data):
      per_image_result=per_image_result.reshape(1,63)
      np.savetxt(csv_file, per_image_result,delimiter=',')
    
    # csv_writer = csv.writer(
    #   csv_file, delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # for index, per_image_result in enumerate(final_data):
    #   per_image_result=per_image_result.reshape(1,63)
    #   print (per_image_result.shape)
    #   csv_writer.writerow([index,per_image_result]) 
  
  # for index, per_image_result in enumerate(final_data):
  #   per_image_result=per_image_result.reshape(1,63)
  #   #per_image_result = np.asarray(per_image_result)
    
  #   print(per_image_result)
  #   np.savetxt('data.csv', per_image_result,delimiter=',')
  
  #save_to_csv(final_data)
  

    