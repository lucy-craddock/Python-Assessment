"""
TO DO:
    Add an exception for error handling if postcode not found.
    Change syntax to with open(file) as file.
"""
def centre_point(postcode, file):
    """ Returns the latlong for the postcode.

    This function checks each row for the postcode and returns the lat and long
    in the 9th and 10th column as floats for the postcode.

    Note: postcode has to be exactly as in the file.
    """
    file = open(file, 'r')
    postcodes = list(file)  # read as strings
    firstcol = 0 # first column contains postcodes
    for row in postcodes:
        if row[firstcol] == postcode:
            lat = row[10]
            lon = row[11]

    file.close()
    return(float(lat), float(lon))
