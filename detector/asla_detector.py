import sys
import time
import mediapipe as mp
import cv2 as cv
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf


tf.config.run_functions_eagerly(True)

sys.path.append('.\\training\\')
from hand_class import Hand


class Detector:
    
    def __init__(self) -> None:
        self._weight_path = '.\\training\\model\\model_0.h5'
        self.model = load_model(self._weight_path)
        
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        
        self.cap = cv.VideoCapture(1)
        
        self.runner()
        
     
    def runner(self):
        buffer = np.empty([1,63])
        
        with self.mp_hands.Hands(
            model_complexity=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7) as hands:
        
            while self.cap.isOpened():
                success, image = self.cap.read()
                
                image.flags.writeable = False
                image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                results = hands.process(image)
                
                image.flags.writeable = True
                image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        
                        #print(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x,hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
                        
                        current_ =  Hand(hand_landmarks)
                        current_data = current_.landmark_data
                        
                        current_data = current_data.reshape(1,63)
                        #print('array:',current_data[0][0],current_data[0][1])
                        #print(current_data[-1])
                        
                        if len(buffer) < 3:
                            buffer = np.append(buffer,current_data, axis=0)
                        
                        elif len(buffer) == 3:
                            
                            # print(buffer[1:3])
                            # print(buffer[1:3].shape)
                            
                            self.asla_detect(buffer[1:3])
                            
                            del buffer
                            buffer = np.empty([1,63])    
                        
                        
                        self.mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style())
                            
                cv.imshow('MediaPipe Hands', cv.flip(image, 1))
                if cv.waitKey(5) & 0xFF == 27:
                    break
                
    def asla_detect(self,last_md_data):
        last_md_data = last_md_data.reshape(1,2,63)
        results = self.model.predict(last_md_data, verbose=0)
        #predicted_class = np.argmax(results, axis=-1)
        
        temp = []
        
        for i in range(27):
            temp.append(results[0][-1][i]) 
        
        max_confidence = max(temp)
        predicted_class_id = temp.index(max_confidence)
                  
          
        
        #print(results.shape)
        print(predicted_class_id)
        
        #time.sleep(1)
                               
if __name__ == "__main__":
    detector = Detector()