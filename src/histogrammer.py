from harrisCorner import *
from math import *

class featureExtractor:
	def __init__(self,corners,gradientMatrix):
		self.corners = corners
		self.gradientMatrix = gradientMatrix

	def histogramGen(self,gradientMatrixTrimmed):
		pi = np.pi
		weights = [[gradientMatrixTrimmed[x][y][2] for y in range(4)] for x in range(4)]
		thetas  = [[gradientMatrixTrimmed[x][y][3] for y in range(4)] for x in range(4)]
		bins	= [0,0.25*pi,0.5*pi,0.75*pi,1.0*pi,1.25*pi,1.5*pi,1.75*pi,2.0*pi]
		histogram = np.histogram(thetas,bins=bins,weights=weights)
		return	histogram

	def features(self):
		neighbourhoods=[]
		for corner in self.corners:
			x,y,r=corner
			neighbourhood = []
			for p in range(-8,8,4):
				for q in range(-8,8,4):
					neighbourhood.append(self.histogramGen(self.gradientMatrix[x+p:x+p+4,y+q:y+q+4]))
			neighbourhoods.append(neighbourhood)
		return neighbourhoods
