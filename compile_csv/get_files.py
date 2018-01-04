from  compile_csv.get_headings import get_headings
from check_list import empty_list

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
        filename = 'crime/' + date + '/' + date + '-devon-and-cornwall-street.csv'
        file = open(filename, 'r')
        crime_loc = list(file)  # turns into list to use indices

        for row in crime_loc[1:]:  # skips heading as already gotten
            row = row.split(',')
            row = row[0:2] + row[4:7] + row[9:10]  # cleans columns
            crimes_list.append(row)

        full_list = full_list + crimes_list

    file.close()

    return full_list

if __name__ == '__main__':
    print('testing get files')
    assert empty_list(get_files(['2016-01']))
    assert empty_list(get_files(['2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07']))
    assert empty_list(get_files(['2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12']))
