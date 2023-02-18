import cv2
import mediapipe as mp
from hand_model import Hand_Model
from hand_class import Hand
from google.protobuf.json_format import MessageToDict
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
IMAGE_FILES = ['.\detector\what.jpg']

#myhand = HAND()



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
    
    cleaned_cords = np.empty(shape=[0,3])
    
    for hand_landmarks in results.multi_hand_landmarks:
      #print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z })'
      )
      
      current_ =  Hand(hand_landmarks)
            
        
      print (current_.landmark_data)
      
      #print (type(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]))
      mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
      
    #   for i in range(2):
    #     print(f'{mp_hands.HandLandmark(i).name}:')
    #     print(f'{hand_landmarks.landmark[mp_hands.HandLandmark(i).value]}')
        
    cv2.imwrite(
        'annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))