import math
from enum import Enum
# Python 3 program for the
# haversine formula
class EarthRadiusIn(Enum):
    MILES = 3960
    KILOMETERS = 6371
    METERS = 6371000


def haversine(lat1: float, lon1: float, lat2: float, lon2: float, measurement: EarthRadiusIn):
     
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
    
    rad = measurement.value

    c = 2 * math.asin(math.sqrt(a))
    return rad * c
 

if __name__ == "__main__":
    # -28.264276, 29.116736
    # -28.282985, 29.139095
    rad = EarthRadiusIn

    lat1 = -28.264276
    lon1 = 29.116736
    lat2 = -28.282985
    lon2 = 29.139095
    print(rad.METERS)
    print(haversine(lat1, lon1,lat2, lon2, rad.METERS), "Meters")
    print(haversine(lat1, lon1,lat2, lon2, rad.KILOMETERS), "kilometers")
    print(haversine(lat1, lon1,lat2, lon2, rad.MILES), "miles")
