import os
import numpy as np

class Combine:
    def __init__(self) -> None:
        self.classes = ['no_words','a','b','c','d','e','f','g','h','i','j','k','l',
                        'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        self.load_data()
        
    def load_data(self):
        data = np.empty([0,43])
        for letter in self.classes:
            temp = np.loadtxt(".\\training\\letter_csvs\\"+letter+"_final_dataset.csv", delimiter=",")
            data = np.append(data,temp,axis=0)
        self.save_to_final(data)
        
    def save_to_final(self,data):
        with open(".\\training\\letter_csvs\\_final_.csv", mode='w+') as csv_file: #saving line per frame in csv
    
            for index, per_image_result in enumerate(data):
                per_image_result=per_image_result.reshape(1,43)
                np.savetxt(csv_file, per_image_result,delimiter=',')
                

combine = Combine()
        
    