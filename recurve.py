#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:54:22 2019

@author: xam
"""

from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import numpy as np
import pickle
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from matplotlib.image import imread
from matplotlib.patches import Circle 
import imageio
import math
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import cv2
import sys
from pylab import figure, text, scatter, show
import os

#intialize lists
DogBlob = [] 
pixels = []
pixeList = []
Global = []
GlobalNLB = []
colorList = []
trackList = []
#files to be analyzed
files = ['Gg.png']
T = False
#img = plt.imread('Gg.png')
#   #threshold image by converting it to greyscale
#image_gray = rgb2gray(img)
#   #read file again. This opening is specifically used to run the file through the blob detection function
#im = Image.open('Gg.png')
#width,height = im.size
#   #change color spacr
#rgb_im = im.convert('RGB')
#blobs_dog = blob_dog(image_gray, max_sigma=50, threshold=.1)
#    #blob_dog(image_gray, max_sigma=30, threshold=.1)
#blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
#if T:
#    blobs_dog = blobs_dog[0:3]
#print(len(blobs_dog))


def points_in_circle_np(radius, x0, y0):
    ''' Given the center and radius collect all the points that lie inside the given circle'''
    x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
    y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
    x, y = np.where((x_[:,np.newaxis] - x0)**2 + (y_ - y0)**2 <= radius**2)
    for x, y in zip(x_[x], y_[y]):
        pixeList.append((x,y))
    return pixeList 

def normalizeCirc(xb,yb,x00,y00,InsideBlobList):
   normalizedBlobList = []
   for blob in InsideBlobList:
      ys,xs,rs = blob
      xd = xs - xb/2
      yd = ys - yb/2
      xn = x00 + xd
      yn = y00 + yd
      normalizedBlobList.append((yn,xn,rs))
   return normalizedBlobList



def draw_on_fig(Glist,GNBL,CL,TL):
   fNamePath = 'Gg.png'
   img = plt.imread(fNamePath)
   im = Image.open(fNamePath)
   width,height = im.size
   figO,axO = plt.subplots(1,figsize = (width/100,height/100))
   axO.imshow(img)
   idx = 0
   for G in Glist:
      if len(GNBL[idx]) == 0 and TL[idx] == 1:
         if CL[idx] == ['BGD']: 
            clr = 'yellow' 
         elif CL[idx] == ['NP']: 
            clr = 'blue' 
         else : 
            clr =  'red' 
         x00,y00,r00,MCH,NP,BGD,bigC,nbsl,counti,BSL = G
         circ = Circle((x00, y00), r00, color = clr, linewidth=2, fill=False)
         axO.add_patch(circ)
      idx += 1 
 
   flat_list = [item for sublist in GNBL for item in sublist] 
   secondblobList = []
   for i in range(len(CL)): 
      if TL[i] != 1 : 
         secondblobList.append(CL[i])
   flatSecondblobList = [item for sublist in secondblobList for item in sublist]
   idx2 = 0
   for lyst in flat_list:
      if flatSecondblobList[idx2] == 'BGD' :
         clr2 = 'yellow'
      elif flatSecondblobList[idx2] == 'NP' :
         clr2 = 'blue'
      else :
         clr2 = 'red'
      yst,xst,rst = lyst
      Scirc = Circle((xst, yst), rst, color = clr2, linewidth=2, fill=False)   
      axO.add_patch(Scirc)
      idx2 += 1 
 
   figO.savefig('fefewafewafewafew.png')

def colonyCounter(blobList,fyle,Maybe):
   ''' count colonies with relevant conditions and collect strings that correspond to how the colors of the circles will be labled in future funcitons''' 
   bacList = []
   MCH = NP = BGD = 0
   MCT = NPT = BGT = 0
   im = Image.open(fyle)
   rgb_im = im.convert('RGB') 
   for lyst in blobList: 
      y,x,r = lyst
      try: 
         red, green, blue= im.getpixel((int(x),int(y)))   
      except:
         print('raised exception') 
         red, green, blue= rgb_im.getpixel((int(x),int(y)))   
      print('yxr and color')
      print(y,x,r) 
      print(red,green,blue)
      if red > 210 and green > 40: 
         MCH += 1
         print('MCH')
         bacList.append('MCH')
      elif red < 210 and red > 100 and  green >= 0 and green < 40: 
         NP += 1
         print('NP')
         bacList.append('NP')
      else :
         BGD += 1
         print('BGD')
         bacList.append('BGD')
   return MCH, NP, BGD,bacList 

def blobDetector(fNamePath,T): 
   img = plt.imread(fNamePath)
   #threshold image by converting it to greyscale
   image_gray = rgb2gray(img)
   #read file again. This opening is specifically used to run the file through the blob detection function
   im = Image.open(fNamePath)
   width,height = im.size
   #change color spacr
   rgb_im = im.convert('RGB')
   blobs_dog = blob_dog(image_gray, max_sigma=50, threshold=.1)
    #blob_dog(image_gray, max_sigma=30, threshold=.1)
   blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
   if T:
      blobs_dog = blobs_dog[0:3]
   return blobs_dog
def blobDetectorLog(fNamePath,T): 
   img = plt.imread(fNamePath)
   #threshold image by converting it to greyscale
   image_gray = rgb2gray(img)
   #read file again. This opening is specifically used to run the file through the blob detection function
   im = Image.open(fNamePath)
   width,height = im.size
   #change color spacr
   rgb_im = im.convert('RGB')
   blobs_log = blob_log(image_gray, max_sigma=50, threshold=.1)
    #blob_dog(image_gray, max_sigma=30, threshold=.1)
   blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
   if T:
      blobs_log = blobs_log[0:3]
   return blobs_log

def draw(count): 
   print('im in draw')
   img = plt.imread("crop" + str(count) + ".jpg")
   image_gray = rgb2gray(img)
   im = Image.open("crop" + str(count) + ".jpg")
   width,height = im.size
   bloblist  = blob_dog(image_gray, max_sigma=50, threshold=.1)
   bloblist[:, 2] = bloblist[:, 2] * sqrt(2) 
   fig,ax = plt.subplots(1)
   ax.imshow(img)
   for blob in bloblist :
      y,x,r = blob
      c = plt.Circle((x, y), r, color='yellow', linewidth=2, fill=False) 
      center =  plt.Circle((x, y), 1, color='blue', linewidth=2, fill=True)
      ax.add_patch(c)
      ax.add_patch(center)
   fig.savefig('samlpe' + str(count) + '.png')
            
    


## analyze every file in files
#for fNamePath in files:
#   MCHb = NPb = BGDb = 0 
#   MCT = NPT = BGT = 0
#   #make sure that the file that is being grabbed is a photograph
#   if fNamePath.endswith(".png") or fNamePath.endswith(".jpg"):
#      # tell the user which file is being processed
#      print("processing" + ' ' +  fNamePath)
#      DogBlob = blobDetector(fNamePath,True)
#      print(DogBlob)
#      #keep an index of what blob in blob log you're looping through 
#      blobC = 1
#      #open images and convert their color coordinate spaces so the program can extract the rgb values subsequently
#      im = Image.open(fNamePath)
#      width,height = im.size
#      rgb_im = im.convert('RGB')      
#      # process second iteration of blobs
#      for puppy in DogBlob:
#         print('processing blob' + ' ' +  str(blobC) + ' ' + 'of' + ' ' + str(len(DogBlob)) + ' ' + 'blobs' + ' ' +  'for photo' + ' ' + fNamePath)   
#         #create a blank canvas in order to place the blobs on in order to eventually crop them.
#         blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))
#         #This is the radius of a single blob on the receipt file
#         y0,x0,radius = puppy
#         # grab every pixel in each blob
#         pixeList = points_in_circle_np(radius, x0, y0)  
#         #iterate through each pixel in a given blob
#         for point in pixeList:
#            xcirc,ycirc  = point
#            #try to grab each pixel, if the pixel is on the edge of the photo and an exception is thrown change the location of pixel so its in the photo
#            try :
#               rred, ggreen, bblue = rgb_im.getpixel((int(xcirc),int(ycirc)))
#            except :
#               if xcirc >= width : 
#                  xcirc = width - 1
#                  rred, ggreen, bblue = rgb_im.getpixel((int(xcirc),int(ycirc)))
#               if ycirc >= height :
#                  ycirc = height - 1
#                  rred, ggreen, bblue = rgb_im.getpixel((int(xcirc),int(ycirc)))
#            #put pixels on the canvas
#            blank.putpixel( (int(xcirc),int(ycirc)), (rred, ggreen, bblue))
#         blank.save("p" + str(blobC) + ".jpg")
#         img = cv2.imread("p" + str(blobC) + ".jpg")
#         #crop a rectangular box around the canvas that you are analyzing 
#         crop_img = img[int(y0-radius):int(y0+radius),int(x0-radius):int(x0+radius)]
#         try: 
#            cv2.imwrite("crop" + str(blobC) + ".jpg", crop_img)
#            cv2.waitKey(0)
#            blob_dog2 = blobDetector("crop" + str(blobC) + ".jpg",False)
#         except: 
#            continue 
#         draw(blobC) 
#         #run cropped image through the blob detector
#         # if the second iteration blob detector comes up empty then 
#         # count classify the original blob
#         if len(blob_dog2) == 0:
#            MCHE,NPE,GDPE,BLs = colonyCounter([puppy],fNamePath,True) 
#            trackList.append(1)
#         else:
#            print('puppy') 
#            print(puppy)
#            print('blob_dog')
#            print(blob_dog2) 
#            MCH,NP,GDP,BLs = colonyCounter(blob_dog2,"crop" + str(blobC) + ".jpg",True)
#            trackList.append(2)
#         '''
#         if len(blob_dog2) == 0 and 'MCH' in locals():
#            MCT = MCH + MCHE
#            NPT = NP + NPE
#            BGT = GDP + GDPE 
#         elif 'MCH' in locals():
#            MCT = MCH
#            NPT = NP
#            BGT = GDP
#         else:
#            MCT = MCHE
#            NPT = NPE 
#            BGT = GDPE
#         '''
#         # get the dimensions of the cropped image
#         imz = Image.open("crop" + str(blobC) + ".jpg")
#         xb,yb = imz.size
#         nbl = normalizeCirc(xb,yb,x0,y0,blob_dog2)
#         
#         GlobalNLB.append(nbl)
#         colorList.append(BLs)
#         Global.append([x0,y0,radius,MCT,NPT,BGT,DogBlob,nbl,blobC,BLs])
#         blobC += 1
#
#finalcount = [item for sublist in colorList for item in sublist]
#draw_on_fig(Global,GlobalNLB,colorList,trackList)

def getBlobs(a,b,c):
         im = Image.open(c)
         width,height = im.size   
         rgb_im = im.convert('RGB')      
         blobC = b 
         blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))
         y0,x0,radius = a
         pixeList = points_in_circle_np(radius, x0, y0)  
         for point in pixeList:
            xcirc,ycirc  = point
            try :
               rred, ggreen, bblue = rgb_im.getpixel((int(xcirc),int(ycirc)))
            except :
               if xcirc >= width : 
                  xcirc = width - 1
               if ycirc >= height :
                  ycirc = height - 1
               rred, ggreen, bblue = rgb_im.getpixel((int(xcirc),int(ycirc)))
            x = int(xcirc + (3000 - width/2))
            y = int(ycirc + (3000 - height/2))
            blank.putpixel((x,y),(rred,ggreen,bblue))
         blank.save("p" + str(b) + ".jpg")
         img = cv2.imread("p" + str(b) + ".jpg")
         crop_img = img[int((y0 + (3000 - height/2) - 2 * radius)):int(y0 + (3000 - height/2) + 2 * radius),int(x0 + (3000 - width/2) - 2 * radius):int(x0 + (3000 - width/2)  + 2 * radius)]
         cv2.imwrite(("crop" + str(b)) + ".jpg", crop_img)  
         blob_dog2 = blobDetector("crop" + str(b) + ".jpg",False)
         blob_dog3 = blobDetectorLog("crop" + str(b) + ".jpg",False)
         if len(blob_dog3) >= len(blob_dog2):
             blobs = blob_dog3
         else:
             blobs = blob_dog2
         imz = Image.open("crop" + str(b) + ".jpg")
         xb,yb = imz.size
         nbl = normalizeCirc(xb,yb,x0,y0,blobs)
       
         return nbl