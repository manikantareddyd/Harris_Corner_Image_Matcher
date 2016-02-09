s1 = HarrisExtractor(8,4,1)
s2 = HarrisExtractor(8,4,3)
y = matcher(s1,s2)
y.match_point_by_point(1.2)
y.compare_Image()


threshold 1.2 Experiment with it 
