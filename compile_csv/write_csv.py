#from compile_csv.get_files import get_files
from get_files import get_files

def write_csv(months):
	''' Writes the compiled list into a single CSV file.

    This function calls the get_files function to return the months in a form of a nested
	list [[row], [row], [row]]. It then strips these lists of brackets and new line before
	writing the row to new CSV file.
	'''
	data = get_files(months)
	
	new_file = open('compile_csv/crimes_in_sw.csv', 'w')
	#new_file = open('crimes_in_sw.csv', 'w')
	
	for row in data:
		temp_row = ''
		for element in row:  # cleaning quotes and brackets
			element.lstrip('\'')
			element.lstrip('[')
			element.lstrip(']')
			temp_row = temp_row + element + ','  # recreates csv file
		row = temp_row
		new_file.write('%s\n' % row)
	new_file.close()

def check_csv():
	''' Unit testing for write_csv file
	checks whether the file contains data
	'''
	with open('crimes_in_sw.csv') as file:
	# no parent directory needed since just for unit testing
		line_ten = file.readline()[0:10] # reads line by line
		len = 0

		for line in line_ten:
			len += 1

		if len > 1:
			result = True
		else:
			result = False

		return result



if __name__ == "__main__":
	print("testing write_csv.py")
	write_csv(['2016-01'])
	assert check_csv()
	write_csv(['2016-01','2016-02','2016-03'])
	assert check_csv()
	write_csv(['2016-08','2016-09','2016-10','2016-11','2016-12'])
	assert check_csv()
