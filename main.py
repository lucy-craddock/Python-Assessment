'''
This module takes a time-range, radius and postcode to find all the crimes within a
radius of that postcode over a time-range. This is outputted in a form of a histogram
in the console.

ATTRIBUTES:
    start_date (str)

    end_date (str)

    postcode (str): inputted for user to be passed through the centre_point function
        that returns the lat, long for the postcode. This is used to calculate crimes
        within a mile of this geoposition.

    radius (int): inputted by user. This is the radius of which the crimes will be
        returned. By requirements, it supposed to return crimes within 1, 2, or
        5 miles.

    date (str): inputted by user. Used in old version to specify which month returns
        the crime data. Not yet included this functionality.

    MONTHS (list): uses the time_range variable to return a nested list of the all the
         crime data for the number of months specified.

    POSTDATA (tuple): longitude and latitude for the postcode inputted. Used in the
        crimes_in_radius to find the crimes within the radius of the geoposition.

    CR_LIST (list): a nested list [[row], [row], [row]] of all the crimes within the
        radius of the postcode geoposition. This is passed to the plot_map function.

'''
from validation.validate_date import validate_date
from validation.validate_postcode import validate_postcode
from compile_csv.write_csv import write_csv
from compile_csv.month_list import month_list
from postcode.centre_point import centre_point
from filter.crimes_in_box import crimes_in_box
from output.plot_histo import plot_histo
from output.csv_save import csv_save

def description():
    print('Authors: Lucy Craddock, Beth Harper, Jaime Viegas, Felipe Warrerner')
    print('ECM1421 - Systems Development 1: Continuous Assessment 2')
    print('Description \n--------------')
    print('''This program will print a histogram to console of the most common crimes for a
postcode within a radius of your choice for the latest month. You can specify a
time frame (in chronological order) if you choose to do. You also have the
option of saving the data used for the charts to a csv file.

The program will allow you to look up another postcode when finished. Crime data is avalible
for 2016-01 through to 2017-11. No crime data will be returned for months outside of this range.
To quit, press 'y'.\n-----------------''')

def get_input():
    postcode = input('Enter a postcode:')
    radius = input('Please choose a 1, 2 or 5 mile radius:')
    option_time = input("Would you like to specify the months? (Y/N)")
    
    if yes_no(option_time):
        start_date = input('Enter a start date in the format YYYY-MM:')
        end_date = input('Enter an end date in the format YYYY-MM:')
    else:
        start_date = '2017-11'
        end_date = '2017-11'
    
    option_save = input("Would you like to save the crimes to a CSV file? (Y/N)")
    
    if yes_no(option_save):
        save_file = True
    else:
        save_file = False

    produce_output(postcode, radius, start_date, end_date, save_file)
    
def yes_no(option):
    if (option.lower() == 'y') or (option.lower() == 'yes'):
        return True
    elif (option.lower() == 'n') or (option.lower() == 'no'):
        return False
    else:
        new_input = input("Sorry, we recieved an error. Please try again.")
        return yes_no(new_input)
    
def produce_output(postcode, radius, start_date,
                   end_date, save_file):
    valid_date1 = validate_date(start_date) # check if start date is valid
    valid_date2 = validate_date(end_date) # check if end date is valid
    valid_postcode = validate_postcode(postcode) # check if postcode is valid

    months = month_list(start_date, end_date) # gets list of months for file names
    write_csv(months) # compile all the crimes into one file

    if valid_postcode and (valid_date1 and valid_date2):
        try:  # catches exemption of postcode not found
            post_data = centre_point(postcode, 'postcode/postcodes.csv') # gets centrepoint latlong
            post_lat = post_data[0]
            post_lon = post_data[1]
            cr_list = crimes_in_box(post_lat, post_lon, int(radius))
            if save_file:
                csv_save(cr_list, postcode, start_date, end_date)
            plot_histo(cr_list)
        except (TypeError, ValueError):
            print('We cannot find your postcode.')
    else:
        print('Sorry, the details you provided were invalid!')

    program_quit = input('Quit? (Y/N)')

    if yes_no(program_quit):
        save_file = True
    else:
        get_input()


if __name__ == '__main__':
    description()
    get_input()
