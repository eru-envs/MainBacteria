#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:38:29 2019

@author: xam
"""
from PIL import Image
import recurve 
import cv2
import sys
import statistics

def getRads(blobs):
    radL = []
    for blob in blobs:
        for b in blob:  
            y,x,r = b
            radL.append(int(r))
    return radL 

def getRadishes(blobs):
    radL = []
    for blob in blobs:
        y,x,r = blob 
        radL.append(int(r))
    return radL    
def fuckSmallCircles(lyst,whole):
   newlyst = []
   rads = getRadishes(whole)
   x1 = statistics.mean(rads)
   y1 = statistics.pstdev(rads)
   
   for blobs in lyst:
      for blob in blobs:
         y,x,r = blob 
         if int(r) <= (x1-2*y1):
            print('888888888888888888888888888')
            print(r)
            print(x1-y1)
            print('888888888888888888888888888')
            print(blob)
            blobs.remove(blob)
         newlyst.append(blobs)
   return newlyst

#load files 

from os import listdir
from os.path import isfile, join
mypath = '/Users/shankin-clarke/Desktop/dect/uf'
#file identifier 
count = 0
fyleL = ['t.png']
for fyle in fyleL:
    whole = recurve.blobDetectorLog(fyle,False)
    #index value passed to make sure that you will never have the same number for cropped photos
    i = 1
    finalBlobList = []
    #number of recursions and the corresponding color for the printed circle
    colorL = []
    blobs = recurve.blobDetector(fyle, False)
    
    compareList =[]
    count += 1
    for blob in blobs:
        compareList =[]
        compareList.append([blob])
        blank2 = Image.new('RGB', (6000,6000), color = (255, 255, 255))
        blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))
        l = recurve.getBlobs(blob,i,fyle,blank,blank2)
        if l == []:
            finalBlobList.append([blob])
            colorL.append(1)
            continue
        i += 1      
        compareList.append(l)
        
        while True:
            i+=1  
            temp = []
            #d : list of blobs from last recursion
            #compareList = fuckSmallCircles(compareList,whole,True)
            whole = recurve.blobDetectorLog(fyle,False)
            compareList = fuckSmallCircles(compareList,whole)
            d = compareList[-1]
            
         
            if ((len(compareList[-1]) == len(compareList[-2])) or (len(compareList) >=2)):
                 finalBlobList.append(d)
                 colorL.append(len(compareList))
                 break
            for b in d:
                i+=1
                blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))
                blank2 =  Image.new('RGB', (6000,6000), color = (255, 255, 255)) 
                c =  recurve.getBlobs(b,i,fyle,blanki,blank2)
                if c == []:
                    temp.extend(b)
                    continue
                else:
                    temp.extend(c)
            if temp != []:        
                compareList.append(temp)    
    

    image = cv2.imread(fyle) 
    image2 = cv2.imread(fyle)
    RadL = getRads(finalBlobList)
    x1 = statistics.mean(RadL)
    y1 = statistics.pstdev(RadL)  
    for blobs, color in zip(finalBlobList, colorL):
        for blob in blobs:
           y,x,r = blob
           X = int(x)
           Y = int(y)
           R = int(r)
           #if int(R) <= (x1-y1):           
              #continue
           print(len(finalBlobList),x1,y1)
           if color == 1:   
               cv2.circle(image,(X, Y), R, (255,255,255))
           elif color == 2 :   
               cv2.circle(image,(X, Y), R, (255,0,255)) 
           elif color == 3 :   
               cv2.circle(image,(X, Y), R, (0,255,0))
               print("a")
           elif color == 4 :   
               cv2.circle(image,(X, Y), R, (0,255,255))  
               print("b")
           elif color == 5 :   
               cv2.circle(image,(X, Y), R, (255,255,0))   
               print("c")
           else:    
               cv2.circle(image,(X, Y), R, (0,0,0)) 
               print("d")
               print(color)
    print("final" + str(count) + ".jpg")
    cv2.imwrite("final" + str(count) + ".jpg", image)  
    blobs = recurve.blobDetector(fyle, False)
    for blob in blobs:
       y,x,r = blob
       cv2.circle(image2,(int(x),int(y)),int(r),(0,0,255))
    cv2.imwrite('finalrecurv1' + str(count) +  ".jpg",image2)
        

          
