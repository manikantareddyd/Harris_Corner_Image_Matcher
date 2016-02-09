from PIL import Image
import numpy as np
from math import *
import cv2
import sys

class HarrisExtractor:
	def __init__(self,WINDOW,BIN,i):
		img = cv2.imread('data/set3/img'+str(i)+'.png', 0)
		#img = cv2.imread('data/chess.png', 0)
		self.kok=i
		newImg = img.copy()
		self.color_img = cv2.cvtColor(newImg, cv2.COLOR_GRAY2RGB)
		img = Image.open('data/set3/img'+str(i)+'.png').convert('L')
		#img = Image.open('data/chess.png').convert('L')
		self.img_data = (np.array(img, dtype = np.float))
		self.WIDTH = len(self.img_data)
		self.LENGTH=len(self.img_data[0])
		self.R = [[0 for i in range(self.LENGTH)] for j in range(self.WIDTH)]
		self.gradientMatrix = [[0 for i in range(self.LENGTH)] for j in range(self.WIDTH)]
		self.k=0.04
		self.WINDOW = WINDOW
		self.offset = self.WINDOW/2
		self.bin = BIN
		self.padding = max(self.bin*2, self.offset)
		self.threshold=1000000
		self.thresholded_Responses=[]
		self.harris_Points=[]
		print "Values Initialised"
		self.get_Gradient()
		self.get_Harris_Response()
		self.get_Harris_Points()

	def get_Gradient(self):
		self.Iy,self.Ix = np.gradient(self.img_data)
		for x in range(self.WIDTH):
			for y in range(self.LENGTH):
				dx=float(self.Ix[x][y])
				dy=float(self.Iy[x][y])
				self.gradientMatrix[x][y]=[dx,dy,np.linalg.norm([dx,dy]),atan2(dy,dx)]
		print "Gradient Matrix Generated"

	def get_Harris_Response(self):
		IxIx = self.Ix*self.Ix
		IxIy = self.Ix*self.Iy
		IyIy = self.Iy*self.Iy
		for x in range(self.padding,self.WIDTH-self.padding):
			for y in range(self.padding,self.LENGTH-self.padding):
				Mxx,Myy,Mxy=0,0,0
				WIxx, WIxy, WIyy = IxIx[x-self.offset:x+self.offset,y-self.offset:y+self.offset], IxIy[x-self.offset:x+self.offset,y-self.offset:y+self.offset], IyIy[x-self.offset:x+self.offset,y-self.offset:y+self.offset]
				Mxx,Myy,Mxy = WIxx.sum(), WIyy.sum(), WIxy.sum()
				det = (Mxx*Myy) - (Mxy*Mxy)
				trace = float(Mxx+Myy)
				if trace==0:
					trace=0.01
				self.R[x][y] = det - (self.k*(trace**2))
				#self.R[x][y] = float(det/trace)
				if self.R[x][y]>self.threshold:
					self.thresholded_Responses.append([x,y,self.R[x][y]])
		print "R values computed"

	def get_Harris_Points(self):
		for corner in self.thresholded_Responses:
			flag=0
			for i in [-1,0,1]:
				for j in [-1,0,1]:
					if corner[2] < self.R[corner[0]+i][corner[1]+j]:
						flag=1
			if flag!=1:
				self.harris_Points.append(corner)
				self.color_img.itemset((corner[0], corner[1], 0), 0)
				self.color_img.itemset((corner[0], corner[1], 1), 0)
				self.color_img.itemset((corner[0], corner[1], 2), 255)
		print "harris_Points computed"
		cv2.imwrite("d"+str(self.kok)+".png", self.color_img)
		self.gradientMatrix = np.array(self.gradientMatrix)
