"""
Compiles the monthly data into one csv file.

TO DO:
    Break up the file into several different ones for easier testing and dubugging.
    Change the month_list function to create a list of the last number of months instead
        of starting.
    Change the month_list function to allow users to specify the month starting and ending
        the list. Say from August to November.

"""
def month_list(time_range):
    """ Creates a list of months starting from January to the time_range specified.
    Note: this should be changed to start from December and go back how many months.

    ATTRIBUTES:
        months (list): an empty list is created to be filled by strings in this format:
            '2016-01', '2016-02'. This is returned. The format is important because this
            is used to read the file names in the directory.
    """
    if time_range == 1: # for human indices
        time_range = 0
    months = []
    for mnth in range(12-time_range, 13):
        mnth = '2016-%s' % ('0%s' % (mnth)
                            if mnth < 10
                            else mnth)
        months.append(mnth)
    return months

def get_headings(months):
    """ Gets the headings of the first CSV file.

    This is done to avoid the heading row being repeated every time a CSV file is read.
    This is then used to write the first row for the compiled CSV file.
    """
    start_date = months[0] # gets first file
    filename = 'crime/' + start_date + '/' + start_date + '-devon-and-cornwall-street.csv'
    file = open(filename, 'r')
    first_file = list(file)
    headings = first_file[0] # takes first row which is a single element in the file list
    headings = headings.split(",") # splits into list of strings
    headings = headings[0:2] + headings[4:7] + headings[9:10] # skips unnecessary columns
    file.close()
    return headings

def get_files(months):
    """ Creates a compiled list of each file in months.

    This function uses the list of months to open the file using the date in the filename
    to compile a list of all the csv files for each month in the months list.
    """
    headings = get_headings(months)
    full_list = []
    full_list.append(headings)  # adds headings to top of list
    crimes_list = [] # new list for the compiled csvs (lists)

    for date in months:
        filename = 'crime/' + date + '/' + date + '-devon-and-cornwall-street.csv'
        file = open(filename, 'r')
        crime_loc = list(file)  # turns into list to use indices

        for row in crime_loc[1:]: # skips heading as already gotten
            row = row.split(',')
            row = row[0:2] + row[4:7] + row[9:10] # cleans columns
            crimes_list.append(row)

        full_list = full_list + crimes_list
    file.close()
    return full_list

def write_csv(months):
    """ Writes the compiled list into a single CSV file.

    This function calls the get_files function to return the months in a form of a nested
    list [[row], [row], [row]]. It then strips these lists of brackets and new line before
    writing the row to new CSV file.
    """
    data = get_files(months)
    new_file = open('crimes_in_sw.csv', 'w')
            # cleans list before writing to csv file
    for row in data:
        temp_row = ''
        for element in row:  # cleaning quotes and brackets
            element.lstrip('\'')
            element.lstrip('[')
            element.lstrip(']')
            temp_row = temp_row + element + ',' # recreates csv file
        row = temp_row
        new_file.write("%s\n" % row)
    new_file.close()
