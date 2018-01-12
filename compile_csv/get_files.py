#from get_headings import get_headings
from compile_csv.get_headings import get_headings
from compile_csv.check_list_ut import empty_list

def get_files(months):
    ''' Creates a compiled list of each file in months.

    This function uses the list of months to open the file using the date in the filename
    to compile a list of all the csv files for each month in the months list.
    '''

    headings = get_headings(months)
    full_list = []
    full_list.append(headings)  # adds headings to top of list
    crimes_list = []  # new list for the compiled csvs (lists)

    for date in months:
        filename = 'compile_csv/crime/' + date + '/' + date + '-devon-and-cornwall-street.csv'
        #filename = 'crime/' + date + '/' + date + '-devon-and-cornwall-street.csv'
        file = open(filename, 'r')
        crime_loc = list(file)  # turns into list to use indices

        for row in crime_loc[1:]:  # skips heading as already gotten
            row = row.split(',')
            row = row[0:2] + row[4:7] + row[9:11]  # cleans columns
            crimes_list.append(row)

        full_list = full_list + crimes_list

    file.close()

    return full_list

if __name__ == '__main__':
    print('testing get_files')
    assert empty_list(get_files['2016-01'])) == ["Crime ID", "Month", "Longditude",
                                                 "Latitude", "Location", "Crime type",
                                                 "Last outcome category"]
    print('test has run successfully')
