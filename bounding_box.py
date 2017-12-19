import math

def bounding_box(latlng, radius):
    """
    Passes postcode latlong and radius to find the maximum and minimum
    coordinates. These will be returned to find all the crimes within this
    bounding box and then work out which is within 1 mile.

    The aim is to reduce the number of times the program will calulcate the
    distance between the centrepoint and crime. This function will be done once
    returning say 80 crimes instead of 1200 that will need to be calculated
    individually.
    """
    EARTH_R = 6371.009  # radius from center of the sphere in km
    lat, lng = latlng   # unpacks tuple

    radius = radius * 1.60934 # turns the radius, given in miles, to km

    # some math
    dlat = radius / EARTH_R
    dlon = math.asin(math.sin(dlat) / math.cos(math.radians(lat)))
    dlat = math.degrees(dlat)
    dlon = (math.degrees(dlon))

    lat_min = lat - dlat
    lat_max = lat + dlat

    lon_min = lng -dlon
    lon_max = lng + dlon

    return(lat_min, lat_max, lon_min, lon_max)
