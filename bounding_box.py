import math

def bounding_box(latlng, radius):
    """
    Passes postcode latlong and radius to find the maximum and minimum
    coordinates. These will be returned to find all the crimes within this
    bounding box and then work out which is within 1 mile.

    The aim is to reduce the number of times the program will calculcate the
    distance between the centrepoint and crime. This function will be done once
    returning say 80 crimes instead of 1200 that will need to be calculated
    individually.
    """
    EARTH_R = 6371.009  # radius from center of the sphere in km
    lat, lng = latlng  # unpacks tuple

    radius = radius * 1.60934  # turns the radius, given in miles, to km

    # some math
    dlat = radius / EARTH_R
    dlon = math.asin(math.sin(dlat) / math.cos(math.radians(lat)))
    dlat = math.degrees(dlat)
    dlon = (math.degrees(dlon))

    lat_min = lat - dlat
    lat_max = lat + dlat

    lon_min = lng - dlon
    lon_max = lng + dlon

    return(lat_min, lat_max, lon_min, lon_max)

if __name__ == "__main__":
    print("testing bounding box")
    assert bounding_box((-2.43695132, 50.71167397), 1) == (-2.4514244418872213, -2.4224781981127785, 50.697187747001045, 50.726160192998954)
    assert bounding_box((-2.43223905, 50.7105854), 1) == (-2.4467121718872216, -2.417765928112779, 50.69609922765665, 50.725071572343346)
    assert bounding_box((-2.4366918, 50.71422888), 1) == (-2.4511649218872216, -2.422218678112779, 50.69974265979337, 50.72871510020663)