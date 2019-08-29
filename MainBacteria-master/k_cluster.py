import numpy as np
import cv2

img = cv2.imread('test_single.png')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

#cv2.imwrite('messigray.png',img)
countb = 0
countnb = 0
for x in range(0,55):
   for y in range(0,55):
        color = res2[y,x]
        print(color[0],color[1],color[2])
        if color[0] == 1 and color[1] == 1 and color[2] ==98:
           countnb += 1
        else :
           countb += 1        

cv2.imshow('res2',res2)
print(countb)
print(countnb)
cv2.waitKey(0)
cv2.destroyAllWindows()
