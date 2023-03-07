import numpy as np
from hand_model import Hand_Model
from google.protobuf.json_format import MessageToDict
from mediapipe import solutions
import math

mp_hands = solutions.hands


class Hand:
    def __init__(self,landmark_struct) -> None:
        
        self.landmark_data = self.__parse_struct(landmark_struct)
        #self.processed_cords
        #print(self.landmark_data) 
        
        return
    
    def __parse_struct(self,hand_landmarks) -> np.array: 
        
        cleaned_cords = np.empty(shape=[0,3])
        for region in mp_hands.HandLandmark:
            #print("wrist:",hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y)
            d = MessageToDict(hand_landmarks.landmark[region])
            result = d.items()
            data = list(result)
            x_px = min(math.floor(data[0][1] * 640), 640 - 1)
            y_px = min(math.floor(data[1][1] * 480), 480 - 1)
            temp=np.array([x_px,y_px,data[2][1]])
            
            #temp=np.array([data[0][1] * 640, data[1][1] * 480,data[2][1]])

            cleaned_cords = np.append(cleaned_cords, [temp], axis=0)
            
        
        processed_cords = self.process_cords(cleaned_cords)
        return processed_cords
    
    
    def process_cords(self,cords_array):
        
        trimmed_cords = np.empty(shape=[0,2])
        
        #get base cordinates. The rest of them will be associated with them
        base_x, base_y = cords_array[0][0],cords_array[0][1] #wrist x,y 
        
        # replace x,y of every value with the distance from the base
        for landmark in range(len(cords_array)):
            cords_array[landmark][0] = cords_array[landmark][0] - base_x     
            cords_array[landmark][1] = cords_array[landmark][1] - base_y

            trimmed_cords = np.append(trimmed_cords,
                                      [[cords_array[landmark][0],cords_array[landmark][1]]],
                                      axis=0) 
        
        #print(trimmed_cords[8][0],trimmed_cords[8][1])
        trimmed_cords=trimmed_cords.reshape(1,42)
        #print("trimmed",trimmed_cords.shape)
            
        #get the biggest distance value, iow: the bigest abs value
        #max_value = abs(max(trimmed_cords ,key = abs)) 
        max_value =  np.max(np.abs(trimmed_cords))
        #print("max value:",max_value)
        
        #normalize all values to the max value
        def _normalize (value):
        # for i in range(len(trimmed_cords)):
        #     return trimmed_cords[i]  =  trimmed_cords[i]/max_value
            return value/max_value
        trimmed_cords = list(map(_normalize,trimmed_cords))
        
        print("normalized", trimmed_cords[0][24],trimmed_cords[0][25])
        
        return trimmed_cords
    
    def get_finger_coords(finger, point, coord):
        return None
    
   # def get_reduced_size_representation
    
    
# if __name__ == "__main__":
#     hand = Hand(a_struct)
#     #hand.landmark_data