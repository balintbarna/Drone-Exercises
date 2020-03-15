from mercator.utm import utmconv
from math import pi, cos, asin, sqrt, sin
import matplotlib.pyplot as plt
import numpy as np
from Generate_plan import plan_generator as pgen
import kml.kmlplot as kmlplot
import outlier_removal
import track_simplifier
import Q_plan

def main():
    print("main started")
    recorded_path_1 = "Week 11 - ex6/input/gps_data_1583748176.57617.txt"
    recorded_path_2 = "Week 11 - ex6/input/gps_data_1583749050.86728.txt"
    kmlplot.plot_kml(recorded_path_1, "Week 11 - ex6/output/track1")
    kmlplot.plot_kml(recorded_path_2, "Week 11 - ex6/output/track2")

    clean_path_1 = "Week 11 - ex6/output/gps_data_1_clean.txt"
    clean_path_2 = "Week 11 - ex6/output/gps_data_2_clean.txt"
    outlier_removal.remove_outliers(recorded_path_1, clean_path_1)
    outlier_removal.remove_outliers(recorded_path_2, clean_path_2)
    kmlplot.plot_kml(clean_path_1, "Week 11 - ex6/output/track1clean")
    kmlplot.plot_kml(clean_path_2, "Week 11 - ex6/output/track2clean")

    simp_path_1 = "Week 11 - ex6/output/gps_data_1_simp.txt"
    simp_path_2 = "Week 11 - ex6/output/gps_data_2_simp.txt"
    config = (0.3, -1)
    track_simplifier.simplify_track(clean_path_1, simp_path_1, config)
    track_simplifier.simplify_track(clean_path_2, simp_path_2, config)
    kmlplot.plot_kml(simp_path_1, "Week 11 - ex6/output/track1simp")
    kmlplot.plot_kml(simp_path_2, "Week 11 - ex6/output/track2simp")

    simp_rdp_path_1 = "Week 11 - ex6/output/gps_data_1_simp_rdp.txt"
    simp_rdp_path_2 = "Week 11 - ex6/output/gps_data_2_simp_rdp.txt"
    treshold = 0.7
    track_simplifier.simplify_track_rdp(clean_path_1, simp_rdp_path_1, treshold)
    track_simplifier.simplify_track_rdp(clean_path_2, simp_rdp_path_2, treshold)
    kmlplot.plot_kml(simp_rdp_path_1, "Week 11 - ex6/output/track1simprdp")
    kmlplot.plot_kml(simp_rdp_path_2, "Week 11 - ex6/output/track2simprdp")

    ############################################
    Q_plan.Qplan("Week 11 - ex6/output/gps_data_2_clean.txt")
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