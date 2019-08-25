#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:38:29 2019

@author: xam
"""
import recurve 
i = 1
finalBlobList = []
blobs = recurve.blobDetector('Gg.png', False)
compareList =[]
print("blobs")
print(len(blobs))
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
        
        
        
        
        
        
        