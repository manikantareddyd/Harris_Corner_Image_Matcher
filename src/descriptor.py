from Harrison import *

class featureExtractor:
	def __init__(self,Harris):
		self.gradientMatrix = Harris.gradientMatrix
		self.harris_Points = Harris.harris_Points
		self.bin = Harris.bin

	def get_Histogram(self,gradientMatrixTrimmed,p,q):
		pi = np.pi
		weightSum = 0
		# print p,q
		for x in range(self.bin):
			for y in range(self.bin):
				weightSum=weightSum+gradientMatrixTrimmed[x][y][2]
		weights = [[gradientMatrixTrimmed[x][y][2]/weightSum for y in range(self.bin)] for x in range(self.bin)]
		thetas  = [[gradientMatrixTrimmed[x][y][3]-self.gradientMatrix[p][q][3] for y in range(self.bin)] for x in range(self.bin)]
		bins	= [0,0.25*pi,0.5*pi,0.75*pi,1.0*pi,1.25*pi,1.5*pi,1.75*pi,2.0*pi]
		histogram = np.histogram(thetas,bins=bins,weights=weights)[0]
		return	histogram

	def get_Descriptors(self):
		neighbourhoods=[]
		for corner in self.harris_Points:
			x,y,r=corner
			neighbourhood = []
			for p in range(-2*self.bin,2*self.bin,self.bin):
				for q in range(-2*self.bin,2*self.bin,self.bin):
					# print p,q
					# print x+p,x+p+self.bin
					# print y+p,y+p+self.bin
					neighbourhood.append(self.get_Histogram(self.gradientMatrix[x+p:x+p+self.bin,y+q:y+q+self.bin],x+p+int(self.bin)/2,y+q+int(self.bin)/2))
			neighbourhoods.append(neighbourhood)
		neighbourhoods = np.array(neighbourhoods)
		return neighbourhoods
