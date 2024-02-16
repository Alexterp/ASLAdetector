import sys
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

        self._weight_path = '.\\training\\model\\model_03_10.h5'
        
        self.model = load_model(self._weight_path)
        
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        
        self.cap = cv.VideoCapture(1)
        
        
        
        self.runner()
        
     
    def runner(self):
        buffer = np.empty([1,42])
        
        with self.mp_hands.Hands(
            model_complexity=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7) as hands:
        
            while self.cap.isOpened():
                success, image = self.cap.read()
                
                image = cv.flip(image,1)
                
                image.flags.writeable = False
                image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                results = hands.process(image)
                
                image.flags.writeable = True
                image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

                
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                                                
                        current_ =  Hand(hand_landmarks)
                        current_data = np.asarray(current_.landmark_data)                        
                        current_data = current_data.reshape(1,42)
                        
                        #print('pinky tip',current_data[-2],current_data[-1])
                        #print('array:',current_data[0][0],current_data[0][1])
                        #print(current_data[-1])
                        
                        if len(buffer) < 3:
                            buffer = np.append(buffer,current_data, axis=0)
                        
                        elif len(buffer) == 3:
                            predicted_letter, confq = self.asla_detect(buffer[-1])
                            
                            del buffer
                            buffer = np.empty([1,42])    
                        
                        
                        self.mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style())
                            
                        if 'predicted_letter' in locals():  
                            cv.putText(image,predicted_letter,(50,50), cv.FONT_HERSHEY_SIMPLEX,1.7,(255,255,255),2,cv.LINE_4)
                            cv.putText(image,str(confq),(450,50), cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv.LINE_4)
                else:
                    cv.putText(image,'No hand',(50,50), cv.FONT_HERSHEY_SIMPLEX,1.7,(255,255,255),2,cv.LINE_4 )         
                cv.imshow('ASLA detector',image)
                if cv.waitKey(5) & 0xFF == 27:
                    break
                
    def asla_detect(self,last_md_data):
        last_md_data = last_md_data.reshape(1,1,42)
        results = self.model.predict(last_md_data, verbose=0)
        #predicted_class = np.argmax(results, axis=-1)
             
        # predicted_class_id = np.argmax(results, axis=-1)
        # predicted_class_id = predicted_class_id.flatten()[0]

        temp = []
        
        for i in range(27):
            temp.append(results[0][-1][i]) 
        
        max_confidence = max(temp)
        predicted_class_id = temp.index(max_confidence)
        class_name = self.get_class_name(predicted_class_id)
        print(class_name,max_confidence)
        return class_name, max_confidence
        
        
        
    def get_class_name(self,predicted_class_id):
        match predicted_class_id:
            case 0:
                predicted_class = 'No Letter' 
            case 1:
                predicted_class = 'A'
            case 2:
                predicted_class = 'B'
            case 3:
                predicted_class = 'C'
            case 4:
                predicted_class = 'D'
            case 5:
                predicted_class = 'E'
            case 6:
                predicted_class = 'F'
            case 7:
                predicted_class = 'G'
            case 8:
                predicted_class = 'H'
            case 9:
                predicted_class = 'I'
            case 10:
                predicted_class = 'J'
            case 11:
                predicted_class = 'K'
            case 12:
                predicted_class = 'L'
            case 13:
                predicted_class = 'M'
            case 14:
                predicted_class = 'N'
            case 15:
                predicted_class = 'O'
            case 16:
                predicted_class = 'P'
            case 17:
                predicted_class = 'Q'
            case 18:
                predicted_class = 'R'    
            case 19:
                predicted_class = 'S'
            case 20:
                predicted_class = 'T'
            case 21:
                predicted_class = 'U'
            case 22:
                predicted_class = 'V'
            case 23:
                predicted_class = 'w'
            case 24:
                predicted_class = 'X'
            case 25:
                predicted_class = 'Y'
            case 26:
                predicted_class = 'Z'
        return predicted_class
                
        
        
                               
if __name__ == "__main__":
    detector = Detector()