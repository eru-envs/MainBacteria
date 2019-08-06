from PIL import Image, ImageDraw

photolist = ['LCM + CSZD1.png','LCM + CSZD2.png','LCM + CSZD3.png']



for photo in photolist :

   im = Image.open(photo)
   d = ImageDraw.Draw(im)


   height = 2320
   width = 3480

   for i in range(0,width,int(width/12)):
      d.line((i,0,i,height),fill=(0,255,0),width = 30)

   for i in range(0,height,int(height/8)):
      d.line((0,i,width,i),fill = (0,255,0),width = 30)

   name = 'grided' + photo
   print(name)
   im.save(photo)
