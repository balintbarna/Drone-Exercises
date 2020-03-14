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

def inliers(p1, p2):
    distance = get_distance_from_geo(p1, p2)
    return distance_is_ok(distance)

def coords_not_zero(point):
    return float(point[1]) != 0.0 and point[2] != 0.0

def remove_outliers(input_path,output_path):
    input_file = open(input_path,'r')
    line = input_file.readline().split("\n")[0].split("\t")
    previous_line = line
    with open(output_path, 'w') as output_file:
        while True:
            new_line = input_file.readline().split("\n")[0].split("\t")
            if '' == new_line[0]:
                break
            if coords_not_equal(previous_line,new_line):
                previous_line = line
                line = new_line
                if coords_not_zero(previous_line):
                    if inliers(previous_line,line):
                        full_text = '%02.5f\t%02.5f\t%03.5f\t%.1f\n' % (float(line[0]), float(line[1]), float(line[2]), float(line[3]))
                        output_file.write(full_text)

if __name__ == "__main__":
    # test functions
    remove_outliers("Week 11 - ex6/input/gps_data_1583748176.57617.txt", "Week 11 - ex6/output/gps_data_1_clean.txt")
    remove_outliers("Week 11 - ex6/input/gps_data_1583749050.86728.txt", "Week 11 - ex6/output/gps_data_2_clean.txt")