from get_files import get_files

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
            temp_row = temp_row + element + ','  # recreates csv file
        row = temp_row
        new_file.write("%s\n" % row)
        
    new_file.close()
