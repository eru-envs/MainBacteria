import pickle
from PIL import Image, ImageDraw
import numpy as np
recList = []


def loadData():
    # for reading also binary mode is important 
    dbfile = open('pil', 'rb')
    db = pickle.load(dbfile)
    return db
data = loadData()

im = Image.open("resizeS.png") 
width, height = im.size

d = []
for x in range(0,width) :
   for y in range(0,height) : 
      d.append(x)
      d.append(y)

print(d)
print('*****************************')
print(data)


chunks = [data[x:x+2] for x in range(0, len(data), 2)]

   



for i in range(len(chunks)-10):

    recList = recList + [(chunks[i],chunks[i+10])]



print(recList)



print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')


slices = chunks
im = Image.open("resizeS.png")
rgb_im = im.convert('RGB')
pixels = []

count = 0 
img = Image.new('RGB', (707, 471), color = (73, 109, 137))
for listt in recList: 
   if count == 1:
      break 
   count += 1    
     # dbfile = open('pixels', 'ab')
      #source, destination 
      #pickle.dump(ash_pixel_array,dbfile)
      #dbfile.close()
   '''
   start = listt[0]
   end = listt[1]
   startx = start[0]
   starty = start[1]
   endx = end[0]
   endy = end[1]
   
   print(start)
   print(end)
   print(startx)
   print(endx)
   print(starty)
   print(endy)
   '''
   for x in range(1,57):
      for y in range(412,468):
          r, g, b = rgb_im.getpixel((x, y))
          pixels = pixels + [(r,g,b)]
          img.putpixel( (x, y), (r,g,b))



img.save("test_single.png")
img.show()
          
