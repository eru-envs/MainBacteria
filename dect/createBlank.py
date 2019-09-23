from PIL import Image


for i in range(200):
   blank = Image.new('RGB', (6000,6000), color = (0, 0, 0))
   blank.save('b' + str(i) + '.png')
