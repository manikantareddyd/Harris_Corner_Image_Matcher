from match import *

i=1000000
j=1.2
dir=1
s1 = HarrisExtractor(8,4,i,1,dir)
s2 = HarrisExtractor(8,4,i,3,dir)
y  = matcher(s1,s2)
y.match_point_by_point(j)
y.compare_Image(j)
print i, j, len(s1.harris_Points), len(s2.harris_Points), len(y.matching_pairs)
