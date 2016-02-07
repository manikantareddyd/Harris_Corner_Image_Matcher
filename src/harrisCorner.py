from PIL import Image
import numpy as np
from math import *
import cv2

img = cv2.imread('data/set1/img1.png', 0)
newImg = img.copy()
color_img = cv2.cvtColor(newImg, cv2.COLOR_GRAY2RGB)

img = Image.open('data/set1/img1.png').convert('L')
img_data = (np.array(img, dtype = np.float))
# Creating the image with corners indicated as red points with the help of opencv

WIDTH = len(img_data)
LENGTH=len(img_data[0])

Iy,Ix = np.gradient(img_data)
R = [[0 for i in range(LENGTH)] for j in range(WIDTH)]
gradientMatrix = [[0 for i in range(LENGTH)] for j in range(WIDTH)]
for x in range(WIDTH):
	for y in range(LENGTH):
		dx=float(Ix[x][y])
		dy=float(Iy[x][y])
		gradientMatrix[x][y]=[dx,dy,np.linalg.norm([dx,dy]),atan2(dy,dx)]
print "Gradient Matrix Generated"
k=0.04
threshold=100000
possible_corners=[]
corners=[]
IxIx = Ix*Ix
IxIy = Ix*Iy
IyIy = Iy*Iy

print "Values Initialised"
for x in range(8,WIDTH-8):
	for y in range(8,LENGTH-8):
		Mxx,Myy,Mxy=0,0,0
		WIxx, WIxy, WIyy = IxIx[x-2:x+3,y-2:y+3], IxIy[x-2:x+3,y-2:y+3], IyIy[x-2:x+3,y-2:y+3]
		Mxx,Myy,Mxy = WIxx.sum(), WIyy.sum(), WIxy.sum()
		det = (Mxx*Myy) - (Mxy*Mxy)
		trace = Mxx+Myy
		R[x][y] = det - (k*(trace**2))
		if R[x][y]>threshold:
			possible_corners.append([x,y,R[x][y]])
print "R values computed"

for corner in possible_corners:
	flag=0
	for i in [-1,0,1]:
		for j in [-1,0,1]:
			if corner[2] < R[corner[0]+i][corner[1]+j]:
				flag=1
	if flag!=1:
		corners.append(corner)
		color_img.itemset((corner[0], corner[1], 0), 0)
		color_img.itemset((corner[0], corner[1], 1), 0)
		color_img.itemset((corner[0], corner[1], 2), 255)
print "Corners computed"
cv2.imwrite("d.png", color_img)
gradientMatrix = np.array(gradientMatrix)
