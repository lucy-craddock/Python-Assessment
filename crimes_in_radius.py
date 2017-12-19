from geodist import distance

def crimes_in_radius(date, lat, lon):
    """
    Returns a nested list of street crimes within a mile radius
    of centrepoint postcode. At the moment, only returns elements in
    strings.
    
    """
    file = open(r'crime/' + date + '/' + date + '-devon-and-cornwall-street.csv', 'r')
    crime_loc = list(file)  # turns into list to use indices
    
    headings = crime_loc[0] # takes first row which is a single element in the file list
    headings = headings.split(",") # splits into list
    headings = [headings[0]] + headings[4:7] + headings[9:10] # skips unneccessary columns
    
    crimes_list = []
    crimes_list.append(headings)  # adds headings to top of list

    for row in crime_loc[1:]: # skips heading to calculate distance
        row = row.split(',')
        
        row = [row[0]] + row[4:7] + row[9:10]
        if row[2] != '':
            crime_lat = float(row[2]) # turns strings into floats
            crime_lon = float(row[1])
            if crime_lat != '':
                difference = distance((crime_lat, crime_lon), (lat, lon))
                if difference < 1: # radius of 1 mile
                    crimes_list.append(row)
    return(crimes_list)
    
    file.close()
    
print(crimes_in_radius("2016-05", 50.827973, -4.544117))