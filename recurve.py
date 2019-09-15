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
import statistics


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

def draw(count,bloblist): 
   img = plt.imread("crop" + str(count) + ".jpg")
   image_gray = rgb2gray(img)
   im = Image.open("crop" + str(count) + ".jpg")
   width,height = im.size
   fig,ax = plt.subplots(1)
   ax.imshow(img)
   for blob in bloblist: 
      y,x,r = blob
      c = plt.Circle((x, y), r, color='yellow', linewidth=2, fill=False) 
      center =  plt.Circle((x, y), 1, color='blue', linewidth=2, fill=True)
      ax.add_patch(c)
      ax.add_patch(center)
   fig.savefig('samlpe' + str(count) + '.png')
            


def getRads(blobs):
    radL = []
    for blob in blobs:
        y,x,r = blob
        R = int(r)
        radL.append(R)
    return radL  

def checkBlack(blank):
   test = set(list(blank.getdata()))
   print(test)
   if len(test)>1:
      raise Exception('The compnents of the set are {}'.format(test))
         
def getUnique(l1,l2):
    print(len(l2))
    for val in l1:
        if val in l2:
            l2.remove(val)
    print("lens")        
    print(len(l1), len(l2))        
    return l2        


def getBlobs(blob,b,c,blank,blank2):
         im = Image.open(c)
         img = blank
         print('b' + str(b) + '.png')
         pixdata = img.load()
         width,height = im.size   
         rgb_im = im.convert('RGB')      
#         blobC = b 
         checkBlack(blank)
         y0,x0,radius = blob
         pixeList = points_in_circle_np(radius, x0, y0) 
         combList = pixeList = points_in_circle_np((2*radius), x0, y0) 
         blackList = getUnique(pixeList,combList)
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
            pixdata[x, y] = (rred, ggreen, bblue, 255)
         for point in blackList:
            xcirc,ycirc  = point
#            try :
#                rred, ggreen, bblue = rgb_im.getpixel((int(xcirc),int(ycirc)))
#            except :
#               if xcirc >= width : 
#                     xcirc = width - 1
#               if ycirc >= height :
#                     ycirc = height - 1
#               rred, ggreen, bblue = rgb_im.getpixel((int(xcirc),int(ycirc)))
            x = int(xcirc + (3000 - width/2))
            y = int(ycirc + (3000 - height/2))
            pixdata[x, y] = (0, 0, 0, 255)
         img.save("p" + str(b) + ".jpg")
         img = cv2.imread("p" + str(b) +".jpg")
         crop_img = img[int((y0 + (3000 - height/2) - 2 * radius)):int(y0 + (3000 - height/2) + 2 * radius),int(x0 + (3000 - width/2) - 2 * radius):int(x0 + (3000 - width/2)  + 2 * radius)]
         cv2.imwrite(("crop" + str(b)) + ".jpg", crop_img)  
#         blob_dog2 = blobDetector("crop" + str(b) + ".jpg",False)
         blob_dog3 = blobDetectorLog("crop" + str(b) + ".jpg",False)
         imz = Image.open("crop" + str(b) + ".jpg")
         draw(b,blob_dog3)
         xb,yb = imz.size
         nbl = normalizeCirc(xb,yb,x0,y0,blob_dog3)
          
         return nbl