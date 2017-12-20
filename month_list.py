def month_list(startdate, enddate):
    """ Creates a list of months starting from a given start date to a given end date.

    ATTRIBUTES:
        months (list): an empty list is created to be filled by strings in this format:
            '2016-01', '2016-02'. This is returned. The format is important because this
            is used to read the file names in the directory.
    """
    
    months = []
    
    try: 
      if startdate[:4] == enddate[:4]:
        year = startdate[:4]
        # the year for both dates must be the same for the module to function correctly
        
    except:
      print("Start and end dates must be within the same year.")
      
    else: # runs if there are no exception errors in the try block
      month_start = startdate[5:]
      month_end = enddate[5:]
      
      # compare months of start and end dates
      range = month_end - month_start
      
      if range < 0:
          # if the range is negative (occurs if dates entered are not in chronological order) then
          # multiply by -1 to make it a postive integer
          range = range*(-1)
      
      if (range > 0) and (range < 12):
          # add dates to empty list
          for month in range(month_start, month_end):
              date = year + "-"
              if month < 10:
                  date += "0"
              date += month
              months.append(date)
          months.append(enddate)
        
     elif range == 0
        months.append(startdate)
        
     else:
        print("Invalid month range)
    
    
    return months
