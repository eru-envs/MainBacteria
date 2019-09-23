import os  
from os import listdir
from os.path import isfile, join
import shutil
import sys 

from PIL import Image

path = os.path.dirname(os.path.realpath(__file__))
allFiles = [f for f in listdir(path) if isfile(join(path, f))]


for fyle in allFiles:
   if fyle.endswith('.png') or fyle.endswith('.jpg') or fyle.endswith('.JPG'):
      img = Image.open(path + '/' + fyle)
      width,height = img.size
      new_img = img.resize((int(width/4),int(height/4)))
      new_img.save('res'+ fyle,'png')
