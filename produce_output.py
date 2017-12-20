"""
This module takes a time-range, radius and postcode to find all the crimes within a
radius of that postcode over a time-range. This is outputted in a form of a histogram
in the console.

ATTRIBUTES:
    time_range (int): inputted by user. This is the number of months passed into the
        month_list function. For example, if this is set to 1, it will return the
        last month. If 6, the last 6 months.
    
    postcode (str): inputted for user to be passed through the centre_point function
        that returns the lat, long for the postcode. This is used to calculate crimes
        within a mile of this geoposition.
    
    radius (int): inputted by user. This is the radius of which the crimes will be
        returned. By requirements, it supposed to return crimes within 1, 2, or
        5 miles. << validation??
    
    date (str): inputted by user. Used in old version to specify which month returns
        the crime data. Not yet included this functionality.
   
    MONTHS (list): uses the time_range variable to return a nested list of the all the
        crime data for the number of months specified.
    
    POSTDATA (tuple): longitude and latitude for the postcode inputted. Used in the
        crimes_in_radius to find the crimes within the radius of the geoposition.
    
    CR_LIST (list): a nested list [[row], [row], [row]] of all the crimes within the
        radius of the postcode geoposition. This is passed to the plot_map function.
        
"""
from compile_csvs import write_csv, month_list
from postcode import centre_point
from crimes_in_box import crimes_in_radius
from plot_map import plot_map
from validate_date import validate_date
from validate_postcode import validate_postcode

time_range = input("Enter a time range (0-12 months)")
postcode = input("Enter a postcode:")
radius = input("Please choose a 1, 2 or 5 mile radius:")
start_date = input("Enter a start date in the format YYYY-MM:")
end_date = input("Enter an end date in the format YYYY-MM:")

valid_date1 = validate_date(start_date) # check if start date is valid
valid_date2 = validate_date(end_date) # check if end date is valid
valid_postcode = validate_postcode(postcode) # check if postcode is valid


MONTHS = month_list(start_date, end_date) # gets list of months for file names
write_csv(MONTHS) # compile all the crimes into one file

if validatePostcode(postcode) and (valid_date1 and valid_date2):
    try:  # catches exemption of postcode not found 
        post_data = centre_point(postcode, 'postcodes.csv') # gets centrepoint latlong 
        post_lat = post_data[0]
        post_lon = post_data[1]
        cr_list = crimes_in_radius(post_lat, post_lon, int(radius))
        plot_map(cr_list, postcode)
    except ValueError:
        print("We cannot find your postcode.")
else:
    print("Sorry, the details you provided were invalid!") 
