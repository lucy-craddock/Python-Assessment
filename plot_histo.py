""" Histogram for most common types of crimes.

The module prints the a histogram in the console of the most common crimes
in a postcode area in descending order.
"""

def plot_map(data, postcode):
    """ Prints the histogram for the crimes in area.

    This function creates a dictionary to store each crime  and its count. It then
    calculates the count to a percentage using the length of the dictionary and sorts
    to print out the 10 most common crimes using the histoplot function.

    Step One:
        Adds crimes to the dictionary as keys and assign the count for the values.
    Step Two:
        Turns the values into a percentages.
    Step Three:
        histoplot() is defined to print a line of the histogram for each of the
        crime types in the text.
    Step Four:
        Sorts the dictionary from highest percentage to lowest. The key parameter to
        call the lambda function to sort the percentages in the second column,
        value (v).
    Step Five:
        Uses sorted_dict to iterate through for each line. This only loops a maximum
        of the number of crime types in the dictionary.

    """
    crime_types = dict()
    length = len(data)

    print(postcode, "has a total of", length, "crimes \n")

    for row in data[1:]:
        if row[5] not in crime_types.keys():
            crime_types[row[5]] = 1
        else:
            crime_types[row[5]] += 1

    for value in crime_types:
        crime_types[value] = crime_types[value]/length * 100

    character_to_display = "*"
    screen_width = 250


    def histoplot(cr_type, percent, max_width, character):
        """ Prints a line for each crime type in the list.

        Args:
            percent (float): percentage used to calculate number of crimes to
                print within max_width.
            max_width (int): maximum width of the screen. This is later subtracted
                by 50 to accomdate for the printed crime type and percentage.
            character (str): the character to display for visualising the histogram.
                This is set to '*'.
        """
        count = round(percent * ((max_width-15)/100))
        count = count * character
        print("'", cr_type, "'", count, "(", "{:02.0f}".format(percent), "%)")


    count = 0
    sorted_dict = sorted(crime_types.items(), key=lambda value: value[1], reverse=True)

    for key in sorted_dict:
        histoplot(key[0], key[1], screen_width, character_to_display)
        count += 1
        if count >= len(crime_types):
            break
