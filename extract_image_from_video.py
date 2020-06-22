import cv2
import os


base_dir = os.path.dirname(__file__) #it will print project folder name
print(base_dir)

cam=cv2.VideoCapture(your video file path) #write your video file path here

#create folder to store images

try:
    if not os.path.exists('E:/Image_video'): #give any folder name
        os.makedirs('E:/Image_video')
except OSError:
    print('Error: creating folder')
    
currentframe=0
i=0
while(True):
    ret,frame=cam.read();
    if ret:
        if(currentframe==i): #store one image for one second (30fps system)
            name="E:/Image_video/frame"+str(currentframe)+".jpg"
            print("creating..." +name)
            cv2.imwrite(name,frame)
            i+=30
        currentframe+=1
    else:
        break
cam.release()
cv2.destroyAllWindows()
