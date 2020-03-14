from OldCode.transverse_mercator import tranmerc
from OldCode.utm import utmconv
from math import pi, cos, asin, sqrt, sin
import matplotlib.pyplot as plt
import numpy as np
from OldCode.exportkml import kmlclass
from Generate_plan import plan_generator as pgen
import outlier_removal

def main():
    print("main started")
    # kmlPlot("Week 11 - ex6/input/gps_data_1583748176.57617.txt", "Week 11 - ex6/output/track1")
    # kmlPlot("Week 11 - ex6/input/gps_data_1583749050.86728.txt", "Week 11 - ex6/output/track2")
    # outlier_removal.remove_outliers("Week 11 - ex6/input/gps_data_1583748176.57617.txt", "Week 11 - ex6/output/gps_data_1_clean.txt")
    # outlier_removal.remove_outliers("Week 11 - ex6/input/gps_data_1583749050.86728.txt", "Week 11 - ex6/output/gps_data_2_clean.txt")
    # kmlPlot("Week 11 - ex6/input/gps_data_1_clean.txt", "Week 11 - ex6/output/track1clean")
    # kmlPlot("Week 11 - ex6/input/gps_data_2_clean.txt", "Week 11 - ex6/output/track2clean")
    # simplifyTrack("Week 11 - ex6/input/gps_data_1_clean.txt")
    # simplifyTrack()
    print("main ended")

def plotPath(v1,v2):
    plt.plot(v1, v2)
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

def simplifyTrack(file):
    eVal=[]
    nVal=[]
    uc = utmconv()
    f = open(file,'r')
    while True:
        line = f.readline().split("\n")[0].split("\t")
        if '' == line[0]:
            break
        (hemisphere1, zone1, letter1, e1, n1) = uc.geodetic_to_utm(float(line[1]),float(line[2]))
        eVal.append(float(e1))
        nVal.append(float(n1))

    plan = pgen(eVal,nVal)
    plan.minimizeDisErr()

    print("Not complete")

def makePlan():
    print("Not complete")


if __name__ == "__main__":
    main()