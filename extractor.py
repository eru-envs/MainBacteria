import cv2 
import argparse 
import random as rand
from time import sleep
import pickle

def range1(start,end):
	return range(start,end+1)

  
# now let's initialize the list of reference point 
ref_point = []
tracker = []
colorList = []
crop = False
global color3 
color3 = 255 
global color2 
color2 = 0 
global color1
color1 = 0 

height = 472
width = 708
widthIterator = 12
heightIterator = 8
xs = 0 
ys = 0
xe = width
ye = 0
m = 0 
pointList = []
  
# construct the argument parser and parse the arguments 
ap = argparse.ArgumentParser() 
ap.add_argument("-i", "--image", required = True, help ="Path to the image") 
args = vars(ap.parse_args()) 
  
# load the image, clone it, and setup the mouse callback function 
image = cv2.imread(args["image"]) 
clone = image.copy()
cv2.namedWindow("image", cv2.WINDOW_NORMAL)  
#cv2.setMouseCallback("image", shape_selection) 
  
  
# keep looping until the 'q' key is pressed 
while True: 
    # display the image and wait for a keypress 
    cv2.imshow("image", image) 
    key = cv2.waitKey(0) & 0xFF
    
    if key == ord("l"):
       print("im in")
       for i in range(0,width,int(width/widthIterator)):
          cv2.line(image,(i,0),(i,height),(255,0,0),5)       
       for i in range(0,height,int(height/heightIterator)):
          cv2.line(image,(0,i),(width,i),(255,0,0),5)
       print('im in')   
    if key == ord("p"):
       count = 0 
       for x in range(0,width+1,int(width/widthIterator)):
          for y in range(0,height+1,int(height/heightIterator)):
             cv2.circle(image,(x,y), 5, (0,245,0), -1)  
             pointList = pointList + [x,y]
             # Its important to use binary mode
       print(pointList) 
       dbfile = open('pil', 'ab')              
      
       #source, destination 
       pickle.dump(pointList,dbfile)                      
       dbfile.close()     
             
    if key == ord("a"):
       image = cv2.imread(args["image"]) 
       widthIterator = widthIterator - 2 
       heightIterator = heightIterator - 2

       print("im in")
       for i in range(0,width,int(width/widthIterator)):
          cv2.line(image,(i,0),(i,height),(255,0,0),5)    
       for i in range(0,height,int(height/heightIterator)):
          cv2.line(image,(0,i),(width,i),(255,0,0),5)
       print('im in')              
    count = 0    
    if key == ord("b"):
       image = cv2.imread(args["image"]) 
       widthIterator = widthIterator  
       heightIterator = heightIterator  
       
       
      
       print("im in")
       m = m +40
       for i in range(0,width,int(width/widthIterator)):
          cv2.line(image,(i,0),(i,height),(255,0,0),5)
       for i in range(m,height,int(height/heightIterator)):
           
           cv2.line(image,(0,i),(width,i),(255,0,0),5)
       print('im in')
             
     
    # press 'r' to reset the window 
    if key == ord("r"): 
        image = clone.copy() 

    # if the 'c' key is pressed, break from the loop 
    elif key == ord("c"): 
        break
    cv2.resizeWindow('image', 600,600) 
    cv2.imshow('image',image)
    cv2.resizeWindow('image', 600,600) 
    cv2.waitKey(0) 
  
# close all open windows 
cv2.destroyAllWindows()



