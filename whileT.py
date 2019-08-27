#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:38:29 2019

@author: xam
"""
import recurve 
import cv2

fyleL = ['12.png', '13.png']
for fyle in fyleL:
    i = 1
    finalBlobList = []
    blobs = recurve.blobDetector(fyle, False)
    compareList =[]   
    for blob in blobs:
        compareList =[]
        compareList.append([blob]) 
        a = blob
        print('a')
        print(a)
        l = recurve.getBlobs(a,i) 
        print('l')
        print(l) 
        i+=1      
        compareList.append(l)
        while True:
            i+=1  
            temp = []
            d = compareList[-1]
            print('d')
            print(d)
            if ((len(compareList[-1]) == len(compareList[-2])) or (len(compareList) >= 6)):
                finalBlobList.append(d)
                break
            for b in d:
                i+=1  
                c =  recurve.getBlobs(b,i)
                if c == []:
                    if temp != []:
                        compareList.append(temp)
                        break
                    else:
                        compareList.append(d)
                        break
                    print('c')
                    print(c)
                    temp.append(c)
            
            compareList.append(temp)    
        
image = cv2.imread('Gg.png')       
for blobs in finalBlobList:
    for blob in blobs:
       try: 
           y,x,r = blob
           Y = int(y)
           X = int(x)
           R = int(r)
       except:
           y,x,r = blob[0]
           Y = int(y)
           X = int(x)
           R = int(r)
       cv2.circle(image,(X, Y), R, (0,255,0)) 
cv2.imshow('Test image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
        
        
        
        