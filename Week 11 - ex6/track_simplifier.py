from math import pi, cos, asin, sqrt, sin
import numpy as np
from mercator.utm import utmconv
from gps.data_helper import *

def convert_to_meters(line):
    uc = utmconv()
    (hemisphere1, zone1, letter1, e1, n1) = uc.geodetic_to_utm(float(line[1]),float(line[2]))
    return [float(line[0]), e1, n1, float(line[3])]

def convert_all_to_meters(lines):
    points = []
    for line in lines:
        points.append(convert_to_meters(line))
    return points

def calculate_distance(p1, p2):
    return sqrt((p1[1]-p2[1])*(p1[1]-p2[1]) + (p1[2]-p2[2])*(p1[2]-p2[2]) + (p1[3]-p2[3])*(p1[3]-p2[3]))

def calculate_distance_errors(points):
    dist_0_1 = calculate_distance(points[0], points[1])
    dist_1_2 = calculate_distance(points[1], points[2])
    real_distance = dist_0_1 + dist_1_2
    simplified_distance = calculate_distance(points[0], points[2])
    error = abs(real_distance - simplified_distance)
    return error

def enabled(criteria):
    return not criteria < 0

def simplify_track(input_path, output_path, config):
    """
    Parameters
    ----------
    config : tuple
        must contain the following:

        max_distance_diff : float
        max_angular_diff : float

        -1 means disabled criteria
    """
    print("simplifying track for " + input_path)
    print("parameters:")
    maxdist = config[0]
    maxang = config[1]
    print("maximum distance error\t"+("disabled" if maxdist < 0 else str(maxdist)))
    print("maximum angular error \t"+("disabled" if maxang < 0 else str(maxang)))

    incount = 0
    outcount = 0
    lines = []
    with open(input_path, 'r') as input_file:
        with open(output_path, 'w') as output_file:
            while True:
                new_line = get_data(input_file)
                incount = incount + 1
                if empty_line(new_line):
                    break
                lines.append(new_line)
                if len(lines) < 3:
                    continue
                # we have 3 points, check if second can be removed or should be kept
                points = convert_all_to_meters(lines)
                if enabled(maxdist):
                    distance_error = calculate_distance_errors(points)
                    if distance_error > maxdist:
                        # cannot remove middle point
                        first_line = lines.pop(0)
                        write_data(output_file, first_line)
                        outcount += 1
                        continue
                
                # if we get to this part, point can be removed
                lines.pop(1)

            # write remaining points
            for line in lines:
                write_data(output_file, line)
                outcount += 1

    print("removed " + str(incount - outcount) + " points")
    print("simplyfying finished: " + output_path)

if __name__ == "__main__":
    # test functions
    config = (0.1, -1)
    simplify_track("Week 11 - ex6/input/gps_data_1_clean.txt", "Week 11 - ex6/output/gps_data_1_simp.txt", config)
    simplify_track("Week 11 - ex6/input/gps_data_2_clean.txt", "Week 11 - ex6/output/gps_data_2_simp.txt", config)