import csv
'''
TO DO:
    Add an exception for error handling if postcode not found.
    Make this work without csv module
'''

def centre_point(postcode, file):
    ''' Returns the latlong for the postcode.

    This function checks each row for the postcode and returns the lat and long
    in the 9th and 10th column as floats for the postcode.

    Note: postcode has to be exactly as in the file.
    '''
    postcodes = []

    file = open(file, 'r')
    postcodes = csv.reader(file)
    postcodes = list(postcodes)  # read as strings

    for row in postcodes:
        # row = row.split(',')
        if row[0] == postcode:  # row[0] contains postcodes
            # if the value of row[0] matches the given postcode, find the lat and lon from the row
            lat = row[10]
            lon = row[11]

            file.close()  # not good practise - won't be closed if postcode not found
            return(float(lat), float(lon))
