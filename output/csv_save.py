from compile_csv.get_files import get_files

def csv_save(data, postcode, start_date, end_date):
    ''' Writes the filtered list of crimes to csv.
    
    Optional by user.
    '''
    filename = postcode + ' from ' + start_date + ' to ' + end_date + '.csv'
    
    new_file = open(filename, 'w')
            # cleans list before writing to csv file

    for row in data:
        temp_row = ''
        for element in row:  # cleaning quotes and brackets
            element.lstrip('\'')
            element.lstrip('[')
            element.lstrip(']')
            temp_row = temp_row + element + ','  # recreates csv file
        row = temp_row
        new_file.write('%s' % row)

    new_file.close()