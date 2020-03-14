from mercator.utm import utmconv
from math import pi, cos, asin, sqrt, sin
import matplotlib.pyplot as plt
import numpy as np
from Generate_plan import plan_generator as pgen
import outlier_removal
import kml.kmlplot as kmlplot

def main():
    print("main started")
    # kmlplot.plot_kml("Week 11 - ex6/input/gps_data_1583748176.57617.txt", "Week 11 - ex6/output/track1")
    # kmlplot.plot_kml("Week 11 - ex6/input/gps_data_1583749050.86728.txt", "Week 11 - ex6/output/track2")
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