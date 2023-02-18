import numpy as np
from hand_model import Hand_Model
from google.protobuf.json_format import MessageToDict
from mediapipe import solutions

mp_hands = solutions.hands

class Hand:
    def __init__(self, landmark_struct) -> None:
        self.landmark_data = self.__parse_struct(landmark_struct) 
        #print('landmarkdata: ',self.landmark_data)
        #pass
        return
    
    def __parse_struct(self,hand_landmarks) -> np.array:
        # TODO: Create a 21x3 array and populate from input struct
        
        cleaned_cords = np.empty(shape=[0,3])
        for region in mp_hands.HandLandmark:
            #print(region)
            d = MessageToDict(hand_landmarks.landmark[region])
           # print ('d',d)
            result = d.items()
            #print ('result',result)
            data = list(result)
            #print(data)
            
            #temp = []
            
            # for cord in range(3):
            #     temp.append(data[cord][1])
                
            temp=np.array([data[0][1] * 640, data[1][1] *480 ,data[2][1]])
            #print ('TEMP:',temp)
            #print(temp)

            cleaned_cords = np.append(cleaned_cords, [temp], axis=0)
        
        #print (cleaned_cords[0])
        return cleaned_cords
    
    def get_finger_coords(finger, point, coord):
        return None
    
   # def get_reduced_size_representation
    
    
# if __name__ == "__main__":
#     hand = Hand(a_struct)
#     #hand.landmark_data