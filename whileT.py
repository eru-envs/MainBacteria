#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:38:29 2019

@author: xam
"""
import recurve 
import cv2



def getRads(blobs):
    radL = []
    for blob in blobs:
        for b in blob
            y,x,r = blob
            R = int(r)
            radL.append(R)
    return radL    
fyleL = ['Gg.png']
count = 0
for fyle in fyleL:
    i = 1
    finalBlobList = []
    colorL = []
    blobs = recurve.blobDetector(fyle, False)
    compareList =[]
    count += 1
    for blob in blobs:
        compareList =[]
        compareList.append([blob]) 
        a = blob
        l = recurve.getBlobs(a,i,fyle) 
        if l == []:
            finalBlobList.append([a])
            colorL.append(1)
            continue
        i+=1      
        compareList.append(l)
        while True:
            i+=1  
            temp = []
            d = compareList[-1]
            if ((len(compareList[-1]) == len(compareList[-2])) or (len(compareList) >=2)):
#                if len(d) ==1 and len(compareList[-1]) == len(compareList[-2]):
#                    finalBlobList.append(compareList[-2])
#                    colorL.append(len(compareList)-1)
#                    print("second recurve corrected")
#                    break
#                else:    
                 finalBlobList.append(d)
                 colorL.append(len(compareList))
                 break
            for b in d:
                i+=1  
                c =  recurve.getBlobs(b,i,fyle)
                print("len")
                print(len(c))
                if c == []:
                    continue
#                    if temp != []:
#                        compareList.append(temp)
#                        colorL.append(len(compareList))
#                    else:
#                        compareList.append(d)
#                        colorL.append(len(compareList))
                else:
                    temp.extend(c)
                    print("lenT")
                    print(len(temp))
            if temp != []:        
                compareList.append(temp)    
             
    radL = getRads(nbl)
    x1 = statistics.mean(radL)
    pdev1 = statistics.pstdev(radL)

    image = cv2.imread(fyle)    
    for blobs, color in zip(finalBlobList, colorL):
        for blob in blobs:
#           try: 
           y,x,r = blob
           X = int(x)
           Y = int(y)
           R = int(r)
#           except:                
#               y,x,r = blob[0]
#               Y = int(y)
#               X = int(x)
#               R = int(r)
           
           if(x1!=[] and pdev1!=[]):
              for blob in nbl:
                  if R<=(x1-pdev1):
                      continue

           if color == 1:   
               cv2.circle(image,(X, Y), R, (255,255,255))
               print("working")
           elif color == 2 :   
               cv2.circle(image,(X, Y), R, (255,0,255)) 
               print ("not working")
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
    cv2.imwrite(("output" +str(8) ) + ".jpg", image)  
          
#cv2.imwrite(image, fyle + '1')
#cv2.waitKey(0)
#flat_list = [item for sublist in photo for item in sublist]

#        
#        
#        