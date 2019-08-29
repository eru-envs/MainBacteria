 
from os import remove 
import cv2


photolist = ['1.png','2.png','3.png']



def myround(x, base):
   return base * round(x/base)

hw = []

for photo in photolist:
   img = cv2.imread(photo, cv2.IMREAD_UNCHANGED)
   height,width = img.shape[:2]
   hw = hw + [(height,width)]

print(hw)
for photo in photolist :
   if photo.endswith(".png"):
      oldimg = cv2.imread(photo, cv2.IMREAD_UNCHANGED)
      img = cv2.resize(oldimg,(hw[0][1], hw[0][0]))    
      height,width = img.shape[:2]      

      heightR = myround(height,8)
      widthR  = myround(width,12)


      name = 'LCM + CSZD' + photo
      
      ires = cv2.resize(img,(widthR, heightR))
      cv2.imwrite(name,ires)

 
   else:
      continue 



