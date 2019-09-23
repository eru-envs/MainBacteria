#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Created on Tue Aug 20 19:38:29 2019



@author: xam

"""

"comment"

from PIL import Image

import rec 

import cv2

import sys

import statistics

import os

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

   nlyst = []

   rads = getRadishes(whole)


   x1 = statistics.mean(rads)

   y1 = statistics.pstdev(rads)

   for blobs in lyst:
       idx = 0
       for blob in blobs:
          try:
             y,x,r = blob
          except:
             print(idx)
             print('blobs before')
             print(blob)
             print(blobs)
             nlyst.append(blob)

             del blobs[idx]
             print('blobs after')
             print(blobs)
             continue
          if int(r) < (x1-(2*y1)):
             print(idx)
             print('blobs before')
             print(blob)
             print(blobs)             
             del blobs[idx]
             print('blobs after')
             print(blobs)
             continue
          if int(r)<5:
             print(idx)
             print('blobs before')
             print(blob)
             print(blobs)
             del blobs[idx]
             print('blobs after')
             print(blobs)
              
             continue
          idx += 1
       if len(nlyst) % 3==0 and len(nlyst)!=0:
           for pos in range (0,len(nlyst),3):
               newBlob = (nlyst[pos],nlyst[pos+1],nlyst[pos+2])
               if int(r) < (x1-(2*y1)):
                   blobs.append(newBlob) 
               else:
                   continue    
               

   if lyst[-1] == []:

       lyst.remove([])

   return lyst



#load files 



from os import listdir

from os.path import isfile, join

cir_dir = os.path.dirname(os.path.realpath(__file__))
mypath = cir_dir 

count = 0

fyleL = ['res.png','resa.png','resb.png','resc.png','resd.png','rese.png','resf.png','resg.png','resh.png','resi.png','resj.png','resk.png','resl.png','resm.png','resn.png','reso.png','resq.png','resr.png','ress.png','rest.png','resu.png','resv.png','resw.png','resx.png','resy.png','resz.png','resza.png']

for fyle in fyleL:
    print(fyle)

    whole = rec.blobDetectorLog(fyle,False)

    #index value passed to make sure that you will never have the same number for cropped photos

    i = 1

    finalBlobList = []

    #number of recursions and the corresponding color for the printed circle

    colorL = []

    blobs = rec.blobDetector(fyle, False)

     

    compareList =[]

    count += 1

    for blob in blobs:

        compareList =[]

        compareList.append([blob])

        blank2 = Image.new('RGB', (6000,6000), color = (255, 255, 255))

        blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))

        l = rec.getBlobs(blob,i,fyle,blank,blank2)

        if l == []:

            finalBlobList.append([blob])

            colorL.append(1)

            continue

        i += 1  

        recursions = 1

        compareList.append(l)

        

        while True:

            i+=1  

            temp = []

            #d : list of blobs from last recursion

#            print('compareList')

#            print(compareList)

            #compareList = fuckSmallCircles(compareList,whole,True)

            whole = rec.blobDetectorLog(fyle,False)

            compareList = fuckSmallCircles(compareList,whole)

        
            recursions +=1

            d = compareList[-1]

#            print('comparelist fucksmall')

#            print(compareList) 

            if len(compareList)==1:

                finalBlobList.append(d)

                colorL.append(1)

                break

            if ((len(compareList[-1]) == len(compareList[-2])) or ( recursions >= 6)):
                 print(recursions)
                 finalBlobList.append(d)

                 colorL.append(recursions)

                 break

            for b in d:

                i+=1

                blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))

                blank2 =  Image.new('RGB', (6000,6000), color = (255, 255, 255)) 

                c =  rec.getBlobs(b,i,fyle,blank,blank2)

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

           if color == 1: 

               print('grgr')  

               cv2.circle(image,(X, Y), R, (255,255,255))

           elif color == 2 :

               print('max')   

               cv2.circle(image,(X, Y), R, (255,255,0)) 

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

    blobs = rec.blobDetector(fyle, False)

    for blob in blobs:

       y,x,r = blob

       cv2.circle(image2,(int(x),int(y)),int(r),(0,0,0))

    cv2.imwrite('finalrecurv1' + str(count) +  ".jpg",image2)

        

def getRecusions(fyleL):
    count = 0
    outputL = []
    for fyle in fyleL:
        outputL = []
    
        whole = rec.blobDetectorLog(fyle,False)
    
        #index value passed to make sure that you will never have the same number for cropped photos
    
        i = 1
    
        finalBlobList = []
    
        #number of recursions and the corresponding color for the printed circle
    
        colorL = []
    
        blobs = rec.blobDetector(fyle, False)
    
         
    
        compareList =[]
    
        count += 1
    
        for blob in blobs:

            compareList =[]
    
            compareList.append([blob])
    
            blank2 = Image.new('RGB', (6000,6000), color = (255, 255, 255))
    
            blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))
    
            l = rec.getBlobs(blob,i,fyle,blank,blank2)
    
            if l == []:
    
                finalBlobList.append([blob])
    
                colorL.append(1)
    
                continue
    
            i += 1  
    
            recursions = 1
    
            compareList.append(l)

        

            while True:

                i+=1  
    
                temp = []
    
                #d : list of blobs from last recursion
             
                #compareList = fuckSmallCircles(compareList,whole,True)
    
                whole = rec.blobDetectorLog(fyle,False)
    
                compareList = fuckSmallCircles(compareList,whole)
    
            
                recursions +=1
    
                d = compareList[-1]
    
    #            print('comparelist fucksmall')
    
    #            print(compareList) 
    
                if len(compareList)==1:
    
                    finalBlobList.append(d)
    
                    colorL.append(1)
    
                    break
    
                if ((len(compareList[-1]) == len(compareList[-2])) or ( recursions >= 6)):
    
                     finalBlobList.append(d)
    
                     colorL.append(recursions)
    
                     break
    
                for b in d:

                    i+=1
    
                    blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))
    
                    blank2 =  Image.new('RGB', (6000,6000), color = (255, 255, 255)) 
    
                    c =  rec.getBlobs(b,i,fyle,blank,blank2)
    
                    if c == []:
    
                        temp.extend(b)
    
                        continue
    
                    else:
    
                        temp.extend(c)
    
                if temp != []:        
    
                    compareList.append(temp)    



    image = cv2.imread(fyle) 

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

           if color == 1: 

               cv2.circle(image,(X, Y), R, (255,255,255))

           elif color == 2 :

               cv2.circle(image,(X, Y), R, (255,255,0)) 

           elif color == 3 :   

               cv2.circle(image,(X, Y), R, (0,255,0))

           elif color == 4 :   

               cv2.circle(image,(X, Y), R, (0,255,255))  

           elif color == 5 :   

               cv2.circle(image,(X, Y), R, (255,255,0))   

           else:    

               cv2.circle(image,(X, Y), R, (0,0,0)) 

    cv2.imwrite("final" + str(count) + ".jpg", image)  
    outputL.append("final" + str(count) + ".jpg")
    return finalBlobList,outputL
   
