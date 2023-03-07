from enum import Enum

class Hand_Model (Enum):
    wrist = 0  #0,1,2
    thumb_cmc = 1  # 3,4,5
    thumb_mcp = 2  # 6,7,8
    thumb_ip = 3   
    thumb_tip = 4
    index_finger_mcp = 5 #
    index_finger_pip = 6
    index_finger_dip = 7
    index_finger_tip = 8 #24,25,26
    middle_finger_mcp = 9
    middle_finger_pip = 10
    middle_finger_dip = 11
    middle_finger_tip = 12
    ring_finger_mcp = 13
    ring_finger_pip = 14
    ring_finger_dip = 15
    ring_finger_tip = 16
    pinky_mcp = 17
    pinky_pip = 18
    pinky_dip = 19
    pinky_tip = 20
    
# for finger in Hand_Model:
#     print(finger.value)

 