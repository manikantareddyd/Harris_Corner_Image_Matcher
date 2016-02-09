from descriptor import *
import numpy as np

class matcher:
    def __init__(self,harris1,harris2):
        self.harris1 = harris1
        self.harris2 = harris2
        self.features1, self.features2 = featureExtractor(harris1).get_Descriptors(), featureExtractor(harris2).get_Descriptors()
        self.N1,self.N2 = len(self.features1), len(self.features2)
        print self.N1, self.N2
        self.matching_pairs = []
    def match_point_by_point(self,ratio_Threshold):
        for i in range(self.N1):
            first = 1000000000
            second = 1000000000
            for j in range(self.N2):
                if (j,i) not in self.matching_pairs:
                    distance = float(np.linalg.norm(self.features1[i].flatten()-self.features2[j].flatten()))
                    #print distance
                    first = min(first,distance)
                    if first == distance:
                            first_Match = j
                    else:
                        second = min(second,distance)
                        if second == distance:
                            second_Match = j
            ratio = float(second)/float(first)
            if ratio > ratio_Threshold:
                self.matching_pairs.append((i,first_Match))
                print  self.harris1.harris_Points[i],self.harris2.harris_Points[first_Match],first,'matched'
    def compare_Image(self):
        newWIDTH = self.harris1.WIDTH
        newLENGTH = 2*self.harris1.LENGTH
        newImg = np.zeros((newWIDTH,newLENGTH,3),np.uint8)
        newImg[:newWIDTH,:newLENGTH/2] = self.harris1.color_img
        newImg[:newWIDTH,newLENGTH/2:newLENGTH] = self.harris2.color_img
        tkp = [self.harris1.harris_Points[i[0]][:2] for i in self.matching_pairs]
        skp = [self.harris2.harris_Points[i[1]][:2] for i in self.matching_pairs]
        for i in range(len(tkp)):
            pt_a = (int(tkp[i][0]), int(tkp[i][1]))
            pt_b = (int(skp[i][0]+newLENGTH/2), int(skp[i][1]))
            cv2.line(newImg, pt_a, pt_b, (255, 0, 0))
            cv2.imwrite("lol.png", newImg)
