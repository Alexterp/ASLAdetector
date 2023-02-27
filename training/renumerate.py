import os
from natsort import os_sorted

IMAGE_FILES = []
path = "C:\\Users\\Alex\\Desktop\\Πτυχιακή\\ASLAdetector\\image_set\\annotated_image_set\\"

os.chdir(path)

for content in os_sorted(os.listdir(path)):     #get image names
  if content.endswith(".png"):
    IMAGE_FILES.append(content)

print (IMAGE_FILES)
c = 0
for f in IMAGE_FILES:
    os.rename(f,"frame_"+ str(c) +".png")
    c +=1
    