from compile_csv.check_list_ut import empty_list
#from check_list_ut import empty_list

def get_headings(months):
    ''' Gets the headings of the first CSV file.

    This is done to avoid the heading row being repeated every time a CSV file is read.
    This is then used to write the first row for the compiled CSV file.
    Note: The start_date is not static because if the user has updated their files for
    2017, 2016-01 will not exist in the directory.
    '''

    start_date = months[0] # gets first file
    filename = ('compile_csv/crime/' + start_date + '/' +
                start_date + '-devon-and-cornwall-street.csv')
    #filename = ('crime/' + start_date + '/' +
    #start_date + '-devon-and-cornwall-street.csv')
    file = open(filename, 'r')

    first_file = list(file)
    headings = first_file[0] # takes first row which is a single element in the file list
    headings = headings.split(',') # splits into list of strings
    headings = headings[0:2] + headings[4:7] + headings[9:11] # skips unnecessary columns
    file.close()

    return headings

if __name__ == '__main__':
    print('testing get headings')
    assert empty_list(get_headings(['2016-01'])) == ["Crime ID", "Month", "Longditude", "Latitude", "Location", "Crime type", "Last outcome category"]
    print('test has run successfully)
