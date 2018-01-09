def month_list(startdate, enddate):
    ''' Creates a list of months starting from a given start date to a given end date.

    ATTRIBUTES:
        months (list): an empty list is created to be filled by strings in this format:
            '2016-01', '2016-02'. This is returned. The format is important because this
            is used to read the file names in the directory.
    '''

    months = []

    try:
        if startdate[:4] == "2016" or startdate[:4] == "2017":
            year_start = startdate[:4]
        # the year for the start and end date must be 2016 or 2017
        if enddate[:4] == "2016" or enddate[:4] == "2017":
            year_end = enddate[:4]
            
    except:
        print('Start and end dates must be either 2016 or 2017.')

    else:  # runs if there are no exception errors in the try block
        month_start = int(startdate[5:])
        month_end = int(enddate[5:])

        # compare months of start and end dates
        if year_start == year_end:
            # add dates to empty list
            for month in range(month_start, month_end):
                date = year + '-'
                if month < 10:
                    date += '0'
                date += str(month)
                months.append(date)
            months.append(enddate)
                
         else: # if years are different
            for month in range(month_start, 13):
                date = year + '-'
                if month < 10:
                    date += '0'
                date += str(month)
                months.append(date)
                
            for month in range(01, month_end):
                date = year + '-'
                if month < 10:
                    date += '0'
                date += str(month)
                months.append(date)
                
    return months

if __name__ == '__main__':
    print('testing month list')
    assert month_list('2016-01','2016-03') == ['2016-01', '2016-02', '2016-03']
   # print(month_list('2016-12', '2016-10'))
   # print(month_list('2016-12', '2016-06'))
    print(month_list('2016-01', '2017-12'))
