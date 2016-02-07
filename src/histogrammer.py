from harrisCorner import *
from math import *
def histogrammer(gradientMatirx):
	pi = np.pi
	weights = [[gradientMatirx[x][y][2] for y in range(4)] for x in range(4)]
	thetas  = [[gradientMatirx[x][y][3] for y in range(4)] for x in range(4)]
	bins	= [0,0.25*pi,0.5*pi,0.75*pi,1.0*pi,1.25*pi,1.5*pi,1.75*pi,2.0*pi]
	histogram = np.histogram(thetas,bins=bins,weights=weights)
	return	histogram

neighbourhoods=[]
for corner in corners:
	x,y,r=corner
	neighbourhood = []
	for p in range(-8,8,4):
		for q in range(-8,8,4):
			print p,q,x,y
			neighbourhood.append(histogrammer(gradientMatirx[x+p:x+p+4,y+q:y+q+4]))
	neighbourhoods.append(neighbourhood)
