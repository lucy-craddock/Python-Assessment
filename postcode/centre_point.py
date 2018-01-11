
def centre_point(postcode, filename):
    ''' Returns the latlong for the postcode.

    This function checks each row for the postcode and returns the lat and long
    in the 9th and 10th column as floats for the postcode.

    Note: postcode has to be exactly as in the file.
    '''
    postcodes = []

    file = open(filename, 'r')
    postcodes = list(file)
    for row in postcodes[1:]:
        row = row.split(',')
        if row[0].startswith('"'):
            row[0] = row[0][1:-1] # trims list as elements begin and end with quotation mark

        if row[0] == postcode:  # first element contains postcodes
            # if the value of row[0] matches the given postcode, find the lat and lon from the row
            lat = row[10][1:-1]
            lon = row[11][1:-2] # extra for the newline character (end of the row)

            file.close()
            if lat is None: # checks for postcode not found
                raise ValueError
            return(float(lat), float(lon))
