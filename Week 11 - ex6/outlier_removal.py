from math import pi, cos, asin, sqrt, sin
import numpy as np
from OldCode.utm import utmconv

def coords_not_equal(p1, p2):
    if float(p1[1]) != float(p2[1]) or float(p1[2]) != float(p2[2]):
        return True
    return False

# format [time, lat, long, alt]
def get_distance_from_geo(p1, p2):
    uc = utmconv()
    (hemisphere1, zone1, letter1, e1, n1) = uc.geodetic_to_utm(float(p1[1]),float(p1[2]))
    (hemisphere2, zone2, letter2, e2, n2) = uc.geodetic_to_utm(float(p2[1]),float(p2[2]))
    dis = sqrt((e1-e2)*(e1-e2)+(n1-n2)*(n1-n2))
    return dis

def distance_is_ok(distance):
    if distance != 0.0 and distance < 2:
        return True
    return False

def should_keep(p1, p2):
    distance = get_distance_from_geo(p1, p2)
    return distance_is_ok(distance)

def remove_outliers(input_path,output_path):
    f = open(input_path,'r')
    line = f.readline().split("\n")[0].split("\t")
    pLine = line
    with open(output_path, 'w') as outF:
        while True:
            newLine = f.readline().split("\n")[0].split("\t")
            if '' == newLine[0]:
                break
            if coords_not_equal(pLine,newLine):
                pLine = line
                line = newLine
                if float(pLine[1]) != 0.0 and pLine[2] != 0.0:
                    if should_keep(pLine,line):
                        full_text = '%02.5f\t%02.5f\t%03.5f\t%.1f\n' % (float(line[0]), float(line[1]), float(line[2]), float(line[3]))
                        outF.write(full_text)