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