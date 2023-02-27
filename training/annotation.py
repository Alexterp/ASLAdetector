import tkinter as tk
import os
from platform import system
import csv
from PIL import ImageTk
from PIL import Image 

class Annotate:
    def __init__(self):
        self.classWindow = tk.Tk()
        self.classWindow.title('ASLAd_annotation_tool')
        
        
        self.counter = -1
        self.images = []
        self.photo = None
        self.frame = tk.Frame(master = self.classWindow,width=1000,height=600, bg='#4d4d4d')
        self.main_frame = tk.Frame(master = self.classWindow,width=1000,height=500,bg='#4d4d4d')
        self.but_frame = tk.Frame(master = self.classWindow,width=1000,height=200,bg='#4d4d4d')
        self.txname=tk.StringVar(self.classWindow)
        self.txname.set("The letter names will apeare here as you insert them")
        self.names = tk.Label(master=self.frame,textvariable=self.txname)
        self.frame.pack()
        self.img_holder = tk.Label(self.main_frame,image=self.photo)
        self.expl = tk.Label(master=self.frame,text="Type the class names inside the box below \n"
                                    "After each name press + to add it to the list.")
        
        
        self.ls_start = tk.StringVar(self.classWindow)
        self.ls_start.set("")
        self.ls_end = tk.StringVar(self.classWindow)
        self.ls_end.set("")
        self.ls_name = tk.StringVar(self.classWindow)
        self.ls_name.set("")
        self.last_sgm_lb_start = tk.Label(self.but_frame,textvariable=self.ls_start)
        self.last_sgm_lb_end = tk.Label(self.but_frame,textvariable=self.ls_end)
        self.last_sgm_lb_name = tk.Label(self.but_frame,textvariable=self.ls_name) 

        self.total=tk.StringVar(self.classWindow)
        self.total.set("1348")
        self.total_label=tk.Label(self.main_frame,textvariable=self.total)

        self.num_holder=tk.StringVar(self.classWindow)
        self.num_holder.set("0")
        self.frame_num =tk.Label(self.main_frame,textvariable=self.num_holder)
        self.nav_label = tk.Label(self.main_frame, text = "You are looking at frame:")
        

        self.bl_seg=tk.StringVar(self.classWindow)
        self.bl_seg.set("To start a segment click the Start Segment button")
        self.segm = tk.Label(self.main_frame, textvariable=self.bl_seg)

        self.name = tk.Entry(self.frame) #use entry.get and delete(0,tk.END)
        self.add = tk.Button(self.frame,text="+",bg="green",command=self.inputWritter)
        self.sub = tk.Button(self.frame,text="-",bg="red",command=self.inputRemover)
        self.Done = tk.Button(self.frame,text="Done!",command=self.label_savior)
        
        self.next = tk.Button(self.but_frame,text="Next Frame",command=lambda  n="forward": self.click_listener(n))
        self.prev = tk.Button(self.but_frame,text="Previous Frame",command=lambda p="backward":self.click_listener(p))
        self.start = tk.Button(self.but_frame,text="Start segment",command=lambda s="start":self.click_listener(s))
        self.end = tk.Button(self.but_frame,text="End segment",command=lambda e="end":self.click_listener(e))
        self.remove = tk.Button(self.but_frame,text="Remove last segment",bg="#ff6633",command=lambda r="remove":self.click_listener(r))


        self.final_output=tk.StringVar(self.classWindow)
        self.final_output.set("")
        self.finale_label = tk.Label(self.but_frame,textvariable=self.final_output,bg='#00cc44')

        self.current_label = None
        self.labels = []
        self.letters = []
        self.segment_times_data=[]
        self.letter_value = tk.StringVar(self.classWindow)
        self.letter_value.set("Select an letter")
        self.submit_letter = tk.Button(self.main_frame,text="Submit letter",command=self.get_current_label)

        self.finale =tk.Button(self.but_frame,text="Finalize Annotation", command = self.finalize)

        self._path = os.path.dirname(os.path.realpath(__file__))
        self.path_label = ""
        self.path_label = self._path+"letters.txt"
        
        self.gui_init()
        
        

    def gui_init(self): 
        self.expl.place(x=320,y=0)
        self.name.place(x=100,y=320)
        self.add.place(x=190,y=350)
        self.sub.place(x=120,y=350)
        self.Done.place(x=155,y=400)
        self.names.place(x=500,y=200)
       
        
        
        tk.Label(self.frame).place(x=3,y=3)
        self.classWindow.mainloop()
        

    def inputWritter(self):
        typed_name = self.name.get()  
        if typed_name !=(""): #avoid blank lables
            self.labels.append(typed_name)
        self.name.delete(0,tk.END)
       # print (self.labels)
        str_act = "The letter names you given so far are:\n"
        for i in range(len(self.labels)):
            str_act+= str(self.labels[i]) +"\n"
        self.txname.set(str_act)
        self.classWindow.update_idletasks()

    def inputRemover(self):
        if len(self.labels) > 0:
            self.labels.pop(-1)
            str_act = "The letter names you given so far are:\n"
            for i in range(len(self.labels)):
                str_act+= str(self.labels[i]) +"\n"
            self.txname.set(str_act)
            self.classWindow.update_idletasks()

    def label_savior(self):
        ready_labels = []
        if not len(ready_labels)==0: #if not empty
            file = open(self.path_label,"a+")
            for label in self.labels:
                ready_labels.append(label + "\n")
            file.writelines(ready_labels)
            file.close()
        self.nextFrame()

    def click_listener(self,click):
        

        if click == "forward":
            self.counter += 1
            print(self.counter)
            
        if click == "backward":
            if self.counter > 0 :
                self.counter -= 1
            else:
                self.at_the_begining = True
        if click == "start":
            self.segment_times_data.append([-1, self.counter, 0])
            self.bl_seg.set("You started a segment")
        if click == "end":
            self.segment_times_data[-1][0] = self.current_label
            self.segment_times_data[-1][2] = self.counter

            self.ls_name.set(str(self.letters[self.segment_times_data[-1][0]]))
            self.ls_start.set(str(self.segment_times_data[-1][1]))
            self.ls_end.set(str(self.segment_times_data[-1][2]))
            self.bl_seg.set("Last segment ended.")
        if click =="remove":
            self.segment_times_data.pop(-1)
            if len(self.segment_times_data) > 1:
                self.ls_name.set(str(self.letters[self.segment_times_data[-1][0]]))
                self.ls_start.set(str(self.segment_times_data[-1][1]))
                self.ls_end.set(str(self.segment_times_data[-1][2]))
            else:
                self.ls_name.set("")
                self.ls_start.set("")
                self.ls_end.set("")
                
        self.image_update()
        

    def image_update(self):
        
        st = self._path+"\\dataset\\iset_0\\frame_"+str(self.counter)+'.png'
        self.photo = ImageTk.PhotoImage(Image.open(st))
        self.img_holder.configure(image=self.photo)
        self.img_holder.image=self.photo
        self.num_holder.set(str(self.counter))
        self.classWindow.update_idletasks()

    def get_current_label(self):
        print("You submited a label name")
        self.current_label = self.letters.index(str(self.letter_value.get()))
        #print(self.current_label)

    def nextFrame(self):
        self.frame.pack_forget()
        self.frame.destroy()
        self.main_frame.pack(side=tk.TOP)
        self.but_frame.pack(side=tk.BOTTOM)
        self.read_labels()
        self.next.place(x=220,y=20)
        self.prev.place (x=20,y=20)
        self.start.place (x=20,y=65)
        self.end.place (x=220,y=65)
        self.remove.place(x=100,y=105)
        self.finale.place(x=800,y=125)
        self.nav_label.place(x=0,y=400)
        tk.Label(self.main_frame,text="Out of total:").place(x=300,y=400)
        self.total_label.place(x=410,y=400)
        self.finale_label.place(x=50,y=150)
        self.frame_num.place(x=220,y=400)
        self.segm.place(x=2,y=430)
        
        tk.Label(self.but_frame,text="Your last segment started at frame:").place(x=450,y=25)
        self.last_sgm_lb_start.place(x=700,y=25)
        tk.Label(self.but_frame,text="and ended at frame:").place(x=450,y=50)
        self.last_sgm_lb_end.place(x=600,y=50)
        tk.Label(self.but_frame,text="with the label:").place(x=450,y=75)
        self.last_sgm_lb_name.place(x=550,y=75)

        self.letter_menu = tk.OptionMenu(self.main_frame,self.letter_value,*self.letters)
        self.letter_menu.place(x=700,y=40)
        self.submit_letter.place(x=720,y=75)
        self.img_holder.place(x=0,y=0)
        
        self.click_listener("forward")
        #self.main()



    def read_labels(self):
        label_list = open('.\\training\letters.txt')
        self.letter = []
        self.nums = []
        c = 0

        while True:
            line = label_list.readline()
            if not line:
                break
            self.letters.append(line.strip())
            c +=1
            #print(c)
            self.nums.append(str(c))
        label_list.close()
        return self.letters
        
    def finalize(self):
        csv_path = ".\\training\\letter_labels.csv"
        with open(csv_path, mode='w',newline='') as csv_file:
            
            csv_writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for segment_data in self.segment_times_data:
                for index in range(segment_data[1],segment_data[2]+1):
                    csv_writer.writerow([segment_data[0]])
                    
        self.final_output.set("THE RESULTS ARE SAVED AT results.csv YOU CAN CLOSE THE TOOL NOW")
        self.classWindow.update_idletasks()


if __name__ == "__main__":
    annotate = Annotate()