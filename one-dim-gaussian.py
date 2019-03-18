import numpy as np 
import cv2
import math
import matplotlib.pyplot as plt

img = cv2.imread('cameraman.bmp', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

size = 5
radius = 1
sigma = 0.000001

gauss = np.zeros((1,size))
for i in range(1):
    for j in range(size):
        gauss[i][j] = (1/math.sqrt(2*math.pi*sigma))*math.exp(-((i-radius-1)**2 
            + (j-radius-1)**2)/2*sigma**2)
gauss = gauss / gauss.sum()
for i in range(len(gauss)):
    for j in range(len(gauss[i])):
        print(gauss[i][j], end=' ')
    print()


print(sum(sum(gauss)))

for i in np.arange(2, height-2):
    for j in np.arange(2, width-2):        
        sum = 0
        for k in np.arange(-2, 3):
            for l in np.arange(-2, 3):
                a = img.item(i+k, j+l)
                p = gauss[0,2+l]
                sum = sum + (p * a)
        b = sum
        img_out.itemset((i,j), b/size)


gauss_trans = np.zeros((size,1))
for i in range(size):
    for j in range(1):
        gauss_trans[i][j] = (1/math.sqrt(2*math.pi*sigma))*math.exp(-((i-radius-1)**2 + (j-radius-1)**2)/2*sigma**2)
gauss_trans = gauss_trans / gauss_trans.sum()



for i in np.arange(2, height-2):
    for j in np.arange(2, width-2):        
        sum = 0
        for k in np.arange(-2, 3):
            for l in np.arange(-2, 3):
                a = img_out.item(i+k, j+l)
                p = gauss_trans[2+l,0]
                sum = sum + (p * a)
        b = sum
        img_out.itemset((i,j), b/size)


newName = 'one_dim_sigma'+str(sigma)+'.bmp'
cv2.imwrite(newName, img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()

