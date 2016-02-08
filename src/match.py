from descriptor import *

harris1 = HarrisExtractor(WINDOW,1)
harris2 = HarrisExtractor(WINDOW,2)
features1 = featureExtractor(harris1)
features2 = featureExtractor(harris2)
