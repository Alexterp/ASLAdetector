import numpy as np
from hand_model import Hand_Model

class Hand:
    def __init__(self, landmark_struct) -> None:
        self.landmark_data = self.__parse_struct(landmark_struct) 
        print(self.landmark_data)
        pass
    
    def __parse_struct(struct) -> np.array:
        # TODO: Create a 21x3 array and populate from input struct
        
        data = np.empty(shape=[0,3]) #creating empty array
        
        for finger in Hand_Model:
            data = np.append(data, [struct[finger.value]], axis = 0)
        
        return np.array()
    
    def get_finger_coords(finger, point, coord):
        return None
    
   # def get_reduced_size_representation
    
    
# if __name__ == "__main__":
#     hand = Hand(a_struct)
#     #hand.landmark_data