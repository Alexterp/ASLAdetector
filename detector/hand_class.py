import numpy as np
from hand_model import Hand_Model
from google.protobuf.json_format import MessageToDict
from mediapipe import solutions

mp_hands = solutions.hands


class Hand:
    def __init__(self, index,landmark_struct) -> None:
        
        self.landmark_data = self.__parse_struct(index,landmark_struct)
        #print(self.landmark_data) 
        
        return
    
    def __parse_struct(self,index,hand_landmarks) -> np.array: 
        print ('index:', index)
        cleaned_cords = np.empty(shape=[0,3])
        for region in mp_hands.HandLandmark:
            d = MessageToDict(hand_landmarks.landmark[region])
            result = d.items()
            data = list(result)
            temp=np.array([data[0][1] * 640, data[1][1] *480 ,data[2][1]])

            cleaned_cords = np.append(cleaned_cords, [temp], axis=0)
            
        #cleaned_cords = np.insert(cleaned_cords,0,index)
        #cleaned_cords = ([index] + [cleaned_cords])
        
        #print (cleaned_cords[0])
        return cleaned_cords
    
   
        
        
    
    def get_finger_coords(finger, point, coord):
        return None
    
   # def get_reduced_size_representation
    
    
# if __name__ == "__main__":
#     hand = Hand(a_struct)
#     #hand.landmark_data