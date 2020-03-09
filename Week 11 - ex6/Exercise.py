from OldCode.transverse_mercator import tranmerc
from OldCode.utm import utmconv
from math import pi, cos, asin, sqrt, sin
import matplotlib.pyplot as plt
import numpy as np
from OldCode.exportkml import kmlclass

#uc = utmconv()
#(hemisphere, zone, letter, e1, n1) = uc.geodetic_to_utm (lat1,lon1)

def plotPath(allEVal,allNVal):
    plt.plot(allEVal, allNVal)
    plt.axis('equal')
    plt.title('Path taken', fontsize=10)
    plt.show()

def kmlColor(val):
    # color: red,green,blue,cyan,yellow,grey,red_poly,yellow_poly,green_poly
    if val <= 0.5:
        return 'red'
    if val <= 0.7:
        return 'green'
    
def kmlPlot(allLat,allLon):
    kml = kmlclass()
    kml.begin('testfile.kml', 'Example', 'Example on the use of kmlclass', 0.7)
    # altitude: use 'absolute' or 'relativeToGround'
    
    kml.trksegbegin ('', '', kmlColor(0), 'absolute') 
    kml.pt(55.47, 10.33, 0.0)
    kml.pt(55.47, 10.34, 0.0)
    kml.pt(55.48, 10.34, 0.0)
    kml.pt(55.47, 10.33, 0.0)
    kml.trksegend()
    kml.end()