# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:53:22 2020

@author: dell
"""

import cv2
import os


base_dir = os.path.dirname(__file__)
print(base_dir)

cam=cv2.VideoCapture("E:/FAMILY/highlights.mp4")

#create folder to store images

try:
    if not os.path.exists('E:/Image_video'):
        os.makedirs('E:/Image_video')
except OSError:
    print('Error: creating folder')
    
currentframe=0
i=0
while(True):
    ret,frame=cam.read();
    if ret:
        if(currentframe==i):
            name="E:/Image_video/frame"+str(currentframe)+".jpg"
            print("creating..." +name)
            cv2.imwrite(name,frame)
            i+=30
        currentframe+=1
    else:
        break
cam.release()
cv2.destroyAllWindows()