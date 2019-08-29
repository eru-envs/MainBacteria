from PIL import Image
height = 2320
width = 3480
widthIterator = 12
heightIterator = 8
pointList = []
for x in range(0,width+1,int(width/widthIterator)):
   for y in range(0,height+1,int(height/heightIterator)):
      pointList = pointList + [x,y]
data = pointList 
recList = []
chunks = [data[x:x+2] for x in range(0, len(data), 2)]
for i in range(len(chunks)-10):

   recList = recList + [(chunks[i],chunks[i+10])]

print(recList)


slices = chunks
im = Image.open("LCM+CSZD1.png")
rgb_im = im.convert('RGB')
pixels = []

count = 0
img = Image.new('RGB', (4000, 4000), color = (73, 109, 137))
for listt in recList:
   if count == 1:
      break
   count += 1
   for x in range(0,290):
      for y in range(0,290):
          r, g, b = rgb_im.getpixel((x, y))
          pixels = pixels + [(r,g,b)]
          img.putpixel( (x, y), (r,g,b))


#img.save("test_single.png")
img.show()



