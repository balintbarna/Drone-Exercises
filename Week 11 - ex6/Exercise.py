from OldCode.utm import utmconv
from math import pi, cos, asin, sqrt, sin

uc = utmconv()

(hemisphere, zone, letter, e1, n1) = uc.geodetic_to_utm (lat1,lon1)
