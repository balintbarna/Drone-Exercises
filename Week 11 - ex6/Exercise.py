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
    
def kmlPlot(file, outputName):
    # altitude: use 'absolute' or 'relativeToGround'
    f = open(file,'r')

    line = f.readline().split("\n")[0].split("\t")
    kml = kmlclass()
    kml.begin(outputName+'.kml', 'Example', 'Example on the use of kmlclass', 0.7)
    while True:
        pLine = line
        line = f.readline().split("\n")[0].split("\t")
        if '' == line[0]:
            break
        if float(pLine[1]) != 0.0 and pLine[2] != 0.0:
            kml.trksegbegin ('', '', kmlColor(0), 'absolute')
            kml.pt(float(pLine[1]), float(pLine[2]), 0.0)
            kml.pt(float(line[1]), float(line[2]), 0.0)
            kml.trksegend()
    kml.end()

kmlPlot("Week 11 - ex6/input/gps_data_1583748176.57617.txt", "track1")
kmlPlot("Week 11 - ex6/input/gps_data_1583749050.86728.txt", "track2")
#print(line)
