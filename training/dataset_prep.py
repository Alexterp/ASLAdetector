import numpy as np
from pandas import read_csv
import csv

letter = "d"

class Prepare:
    
    def __init__(self) -> None:
        self.load_md_data()
    
        # self.mediapipe_data
        # self.label_data
        
    
    def load_md_data(self):        
        #--- Getting mediapipe data
        self.mediapipe_data = np.loadtxt(".\\training\\unprepared_data\\"+letter+".csv", delimiter=",")    
        #--- Getting letter labels 
        self.label_data = np.loadtxt(".\\training\\unprepared_data\\"+letter+"_letter_labels.csv", delimiter=",")
        
        
        assert  len(self.label_data) ==  len(self.mediapipe_data)    
        # self.label_data = self.label_data.reshape(1,3)
        # self.label_data = self.label_data.astype(int)
        self.combine_data(self.mediapipe_data,self.label_data)
    
    
    def combine_data(self,md_data,lbl_data):
        self.combined_data = np.empty(shape=[0,43],dtype= object) # 63 md data + 1 label id
        
        for frame in range(len(md_data)):
            temp = np.empty(64,dtype=object)
            temp = np.insert(md_data[frame],0,int(lbl_data[frame]))
            
            #print(temp)
            self.combined_data = np.append(self.combined_data,[temp],axis=0)
        
        self.save_dataset(self.combined_data)
     
     
            
    def save_dataset(self,combined_data):
        
        with open(".\\training\\"+letter+"_final_dataset.csv", mode='w+') as csv_file: #saving line per frame in csv
    
            for index, per_image_result in enumerate(combined_data):
                per_image_result=per_image_result.reshape(1,43)
                np.savetxt(csv_file, per_image_result,delimiter=',')
        
        
if __name__ == "__main__":
    prepare=Prepare()
    
    print(prepare.combined_data)
    