
def tabular_output(data, postcode):
	''' Prints a table of data.
	'''
	crime_types = dict()
	length = len(data) - 1 # skips header
	
	print('\n' + postcode, 'has a total of', length, 'crimes. \n')
	
	for row in data[1:]:
		if row[5] not in crime_types.keys():
			crime_types[row[5]] = 1
		else:
			crime_types[row[5]] += 1


	heading = ['Crime Type', 'Count', 'Percent']
	
	def histoplot(heading,
	
		for value in crime_types: # move to line
			crime_types[value] = crime_types[value]/length * 100
	
	
	
	
	for key in sorted_dict:
        table_line(key[0], key[1], screen_width, character_to_display)
        count += 1
        if count >= length:
            break
	'''
	for i, d in enumerate(data):
		line = '|'.join(str(x).ljust(15) for x in d)
		print(line)
	if i == 0:
		print('-' * len(line))
	'''
'''
def tabular_output(data, postcode):
    """print_table(rows)
    Prints out a table using the data in `rows`, which is assumed to be a
    sequence of sequences with the 0th element being the header.
    """
	crime_types = dict()
	length = len(data) - 1 # skips header
	
	print('\n' + postcode, 'has a total of', length, 'crimes. \n')
	
	for row in data[1:]:
        if row[5] not in crime_types.keys():
            crime_types[row[5]] = 1
        else:
            crime_types[row[5]] += 1
	
	
    # - figure out column widths
    widths = [ len(max(columns, key=len)) for columns in zip(*rows) ]

    # - print the header
    header, data = rows[0], rows[1:]
    print(
        ' | '.join( format(title, "%ds" % width) for width, title in zip(widths, header) )
        )

    # - print the separator
    print( '-+-'.join( '-' * width for width in widths ) )

    # - print the data
    for row in data:
        print(
            " | ".join( format(cdata, "%ds" % width) for width, cdata in zip(widths, row) )
            )
'''