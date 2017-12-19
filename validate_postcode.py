# validate postcode
def validate_postcode(postcode):

    """ Checks a string to determine if it is a valid postcode. Return boolean value where
    True indicates the postcode is valid. """
    
    # Inital validity set to False
    valid = False
    
    # Remove spaces in string if necessary
    if " " in postcode:
        postcode = postcode.replace(" ", "")
        
    # If the postcode is longer the 7 characters, or less than 5 characters in length, then it is not valid
    if (len(postcode) < 5) or (len(postcode) > 7):
        return valid
        
    elif (postcode[0].isnumeric()) or (postcode[-1].isnumeric()):
        # If the postcode has a number at the start or end then it is not valid
        return valid

    else:
        if len(postcode) == 5:
            # Test format A11AA
            if (postcode[1].isnumeric() and postcode[2].isnumeric()) and (postcode[0].isalpha() and postcode[3:].isalpha()):
                valid = True
                
        elif len(postcode) == 6:
            # Test format A111AA
            if (postcode[1:3].isnumeric()) and (postcode[0].isalpha() and postcode[4:].isalpha()):
                valid = True
            # Test format AA11AA
            elif (postcode[2:4].isnumeric()) and (postcode[0:1].isalpha() and postcode[4:].isalpha()):
                valid = True
            # Test format A1A1AA
            elif (postcode[1].isnumeric() and postcode[3].isnumeric()) and (postcode[-1].isalpha() and postcode[0:-1:2].isalpha):
                valid = True
                
        elif len(postcode) == 7:
            # Test format AA111AA
            if (postcode[2:5].isnumeric()) and (postcode[0:2].isalpha() and postcode[5:].isalpha()):
                valid = True
            # Test format AA1A1AA
            elif (postcode[2].isnumeric() and postcode[4].isnumeric()) and (postcode[0:2].isalpha() and postcode[5:].isalpha() and postcode[5:].isalpha()):
                valid = True
        else:
            valid = False
            
    return valid
    
    
def test_valid():

    validFormat = ["A11AA", "A111AA", "AA11AA", "A1A1AA", "AA111AA", "AA1A1AA", "DT1 1AA", "DT11 7XQ", "PL25 3UH"]
    invalidFormat = ["A1AA", "AAAAAA", "AAA1A11AA", "AA", "AA1AAAA", "AA11111", "DT1AA", "DTXQ", "4L253UH"]
    
    for i in range(len(validFormat)):
        validate = validatePostcode(validFormat[i])
        print(validate)
        
    for j in range(len(invalidFormat)):
        validate = validatePostcode(invalidFormat[j])
        print(validate)
