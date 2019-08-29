import statistics
import pickle 
import matplotlib.pyplot as plt
from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray

globyl_dog = []
globyl_log = []
globyl_doh = []

'''
photolist = ['ND.JPG','-1.JPG','-2.JPG','-3.JPG']


cc = 0
for photo in photolist:
   cc = cc+  1
   print('processing' + photo)
   image = plt.imread(photo)
   image_gray = rgb2gray(image)
   blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)
   blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

   blobs_dog = blob_dog(image_gray, max_sigma=30, threshold=.1)
   blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)

   blobs_doh = blob_doh(image_gray, max_sigma=30, threshold=.01)

   blobs_list = [blobs_log, blobs_dog, blobs_doh]
   colors = ['yellow', 'lime', 'red']
   titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
          'Determinant of Hessian']
   sequence = zip(blobs_list, colors, titles)

   fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
   ax = axes.ravel()

   for idx, (blobs, color, title) in enumerate(sequence):
       ax[idx].set_title(title)
       ax[idx].imshow(image)
       for blob in blobs:
           y, x, r = blob
           c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
           ax[idx].add_patch(c)
       ax[idx].set_axis_off()

   plt.tight_layout()
   fig.savefig('temp1111' + str(c) + '.png')
   local_dog = []
   local_log = []
   local_doh = []

   for blob in blobs_doh:
      y,x,r = blob
      local_doh.append(r)
   for blob in blobs_dog:
      y,x,r = blob
      local_dog.append(r)
   for blob in blobs_log:
      y,x,r = blob
      local_log.append(r)
   globyl_dog.append(local_dog)
   globyl_log.append(local_log)
   globyl_doh.append(local_doh)

glists= open('glists', 'ab')
pickle.dump([globyl_dog,globyl_log, globyl_doh], glists)
glists.close() 

'''

dbfile = open('glists', 'rb')      
db = pickle.load(dbfile)
dbfile.close

globyl_dog = db[0]
globyl_log = db[1]
globyl_doh = db[2]

print('gtgtr')
print(len(globyl_log[2]) == len(globyl_log[0]))




'''

flatlistdog = [item for sublist in globyl_dog for item in sublist]
flatlistlog = [item for sublist in globyl_log for item in sublist]
flatlistdoh = [item for sublist in globyl_doh for item in sublist]



x1 = statistics.mean(flatlistdog)
x2 = statistics.mean(flatlistlog)
x3 = statistics.mean(flatlistdoh) 

sd1 = statistics.stdev(flatlistdog)
sd2 = statistics.stdev(flatlistlog)
sd3 = statistics.stdev(flatlistdoh)

hm1 = statistics.harmonic_mean(flatlistdog)
hm2 = statistics.harmonic_mean(flatlistlog)
hm3 = statistics.harmonic_mean(flatlistdoh)

md1 = statistics.median(flatlistdog)
md2 = statistics.median(flatlistlog)
md3 = statistics.median(flatlistdoh)

mdl1 = statistics.median_low(flatlistdog)
mdl2 = statistics.median_low(flatlistlog)
mdl3 = statistics.median_low(flatlistdoh)

mdh1 = statistics.median_high(flatlistdog)
mdh2 = statistics.median_high(flatlistlog)
mdh3 = statistics.median_high(flatlistdoh)

mdg1 =  statistics.median_grouped(flatlistdog)
mdg2 =  statistics.median_grouped(flatlistlog)
mdg3 = statistics.median_grouped(flatlistdoh)

mude1 = statistics.mode(flatlistdog)
mude2 = statistics.mode(flatlistlog)
mude3 = statistics.mode(flatlistdoh)

pdev1 = statistics.pstdev(flatlistdog)
pdev2 = statistics.pstdev(flatlistlog)
pdev3 = statistics.pstdev(flatlistdoh)

pvar1 = statistics.pvariance(flatlistdog)
pvar2 = statistics.pvariance(flatlistlog)
pvar3 = statistics.pvariance(flatlistdoh)

var1  = statistics.variance(flatlistdog)
var2  = statistics.variance(flatlistlog)
var3  = statistics.variance(flatlistdoh)



print('mean',x1,x2,x3)
print('sd',sd1,sd2,sd3)

print('hm',hm1,hm2,hm3)
print('md',md1,md2,md3)

print('mdl',mdl1,mdl2,mdl3)

print('mdh',mdh1,mdh2,mdh3)

print('mdg',mdg1,mdg2,mdg3)

print('mude',mude1,mude2,mude3)

print('pdev',pdev1,pdev2,pdev3)

print('pvar1',pvar1,pvar2,pvar3)


print('var1',var1,var2,var3)


localND_dog = globyl_dog[0] 
local1_dog =  globyl_dog[1]
local2_dog =  globyl_dog[2]
local3_dog =  globyl_dog[3]

localND_log = globyl_log[0]
local1_log =  globyl_log[1]
local2_log =  globyl_log[2]
local3_log =  globyl_log[3]

localND_doh = globyl_doh[0]
local1_doh =  globyl_doh[1]
local2_doh =  globyl_doh[2]
local3_doh =  globyl_doh[3]



import matplotlib.pyplot as plt
print('gregresgresge')
print(len(flatlistdog))
print(len(list(set(flatlistdog))))

# plotting the points  
plt.plot(flatlistdog, [0]*len(flatlistdog),'.') 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 
'''
