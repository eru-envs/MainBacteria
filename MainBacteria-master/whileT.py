#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:38:29 2019

@author: xam
"""
import recurve 
import cv2
fyleL = ['test.png','test.png']
for fyle in fyleL:
    print(fyle)
    i = 1
    finalBlobList = []
    colorL = []
    blobs = recurve.blobDetector(fyle, False)
    print('blobs')
    print(blobs)
    ddd = 0
    compareList =[]   
    for blob in blobs:
        compareList =[]
        compareList.append([blob]) 
        a = blob
        l = recurve.getBlobs(a,i,fyle,ddd) 
        ddd += 1 
        print('l')
        print(l)  
        compareList.append(l)
        while True:
            i+=1  
            temp = []
            d = compareList[-1]
            print('d')
            print(d)
            if ((len(compareList[-1]) == len(compareList[-2])) or (len(compareList) >= 6)):
                if len(d) ==1:
                    finalBlobList.append(compareList[-2])
                    colorL.append(len(compareList))
                    break
                else:    
                    finalBlobList.append(d)
                    colorL.append(len(compareList))
                    break
            for b in d:
                i+=1  
                c =  recurve.getBlobs(b,i,fyle)
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

image = cv2.imread('G.png')    
i = 0   
for blobs in finalBlobList:
    i += 1
    for blob in blobs:
       try: 
           y,x,r = blob
           X = int(x)
           Y = int(y)
           R = int(r)
       except:                
           y,x,r = blob[0]
           Y = int(y)
           X = int(x)
           R = int(r)
       if colorL[i] == 1:   
           cv2.circle(image,(X, Y), R, (0,0,255))
       if colorL[i] == 1 :   
           cv2.circle(image,(X, Y), R, (255,0,0))   
       if colorL[i] == 1 :   
           cv2.circle(image,(X, Y), R, (0,255,0)) 
       if colorL[i] == 1 :   
           cv2.circle(image,(X, Y), R, (255,255,255))  
       else:    
           cv2.circle(image,(X, Y), R, (0,0,0))  

#cv2.imwrite(image, fyle + '1')
#cv2.waitKey(0)
#        
#        
#  

