from OldCode.transverse_mercator import tranmerc
from OldCode.utm import utmconv
from math import pi, cos, asin, sqrt, sin
import matplotlib.pyplot as plt
import numpy as np
from OldCode.exportkml import kmlclass
from Generate_plan import plan_generator as pgen

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

def distance(p1,p2):
    uc = utmconv()
    (hemisphere1, zone1, letter1, e1, n1) = uc.geodetic_to_utm(float(p1[1]),float(p1[2]))
    (hemisphere2, zone2, letter2, e2, n2) = uc.geodetic_to_utm(float(p2[1]),float(p2[2]))
    dis=sqrt((e1-e2)*(e1-e2)+(n1-n2)*(n1-n2))
    if dis != 0.0 and dis < 2:
        return True
    return False

def isNew(old,new):
    if float(old[1]) != float(new[1]) or float(old[2]) != float(new[2]):
        return True
    return False

def removeOutlier(file,outputName):
    f = open(file,'r')
    line = f.readline().split("\n")[0].split("\t")
    pLine = line
    with open(outputName, 'w') as outF:
        while True:
            newLine = f.readline().split("\n")[0].split("\t")
            if '' == newLine[0]:
                break
            if isNew(pLine,newLine):
                pLine = line
                line = newLine
                if float(pLine[1]) != 0.0 and pLine[2] != 0.0:
                    if distance(pLine,line):
                        full_text = '%02.5f\t%02.5f\t%03.5f\t%.1f\n' % (float(line[0]), float(line[1]), float(line[2]), float(line[3]))
                        outF.write(full_text)

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

#kmlPlot("Week 11 - ex6/input/gps_data_1583748176.57617.txt", "Week 11 - ex6/output/track1")
#kmlPlot("Week 11 - ex6/input/gps_data_1583749050.86728.txt", "Week 11 - ex6/output/track2")
#removeOutlier("Week 11 - ex6/input/gps_data_1583748176.57617.txt", "Week 11 - ex6/input/gps_data_1_clean.txt")
#removeOutlier("Week 11 - ex6/input/gps_data_1583749050.86728.txt", "Week 11 - ex6/input/gps_data_2_clean.txt")
#kmlPlot("Week 11 - ex6/input/gps_data_1_clean.txt", "Week 11 - ex6/output/track1clean")
#kmlPlot("Week 11 - ex6/input/gps_data_2_clean.txt", "Week 11 - ex6/output/track2clean")
simplifyTrack("Week 11 - ex6/input/gps_data_1_clean.txt")
#simplifyTrack()

#print(line)
