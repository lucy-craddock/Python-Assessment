
"""
TO DO:
    Add an exception for error handling if postcode not found.
"""
def centre_point(postcode, file):
    """ Returns the latlong for the postcode.

    This function checks each row for the postcode and returns the lat and long
    in the 9th and 10th column as floats for the postcode.

    Note: postcode has to be exactly as in the file.
    """
    postcodes = []
    
    file = open(file, 'r')
    postcodes = list(file)  # read as strings

    for row in postcodes:
        if row[0] == postcode: #row[o] contains postcodes
            # if the value of row[0] matches the given postcode, find the lat and lon from the row
            lat = row[10]
            lon = row[11]

    return(float(lat), float(lon))
