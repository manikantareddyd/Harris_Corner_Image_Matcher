from match import *

for dir in [1,2,3]:
    print "*"*100
    print "Working on set"+str(dir)+" images"
    for i in [11,10,9,8,7,6,5,4]:
        s1 = HarrisExtractor(8,4,10**i,1,dir)
        s2 = HarrisExtractor(8,4,10**i,3,dir)
        y  = matcher(s1,s2)
        print "\n"
        print "*"*60
        print "Using a threshold of 10^"+str(i)+" for filteirng Harris Points"
        print "Number of Harris Points in 1st ",len(s1.harris_Points)
        print "Number of Harris Points in 2nd ",len(s2.harris_Points)
        for j in reversed([1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.6,1.7]):
            print "\n"
            print "Using a threshold of "+str(j)+" for ratio of 1st to 2nd"
            y.match_point_by_point(j)
            y.compare_Image(j)
            print "Number of matching points found",len(y.matching_pairs)
