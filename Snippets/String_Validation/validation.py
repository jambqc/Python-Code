#!/usr/bin/env python

def checkCharacters(string, function):
    '''
    Determines if a string has a specific attribute, for example,
    it will dteremine a given string contains any digits. The 
    string 'asd23d' does contain digits, thus the function would
    return True.

    INPUT:
    string- Any string of characters
    function- Must be an attribute of a string, and input as a string.
    
    OUTPUT: 
    True or False 
    '''
    for letter in string:
        if getattr(letter, function)():
            message1 = "Yes, the string '%s' does have the "\
                    "attribute %s()." % (string, function)
            return message1 
        else:
            pass
    message2 = "No, the string '%s' does not have " \
    "the attribute %s()." % (string, function) 
    return message2


if __name__ == '__main__':
     
    # user inputs a string, for example 'asd4Gd1'
    # and a function, for exampl 'isdigit'
    a = input('Please enter a string and press return: ')
    checkList = input('Please enter a string attribute (or multiple) to check for: ').strip().split(' ')
    # attributes to check for in string
    # they will pass as arguments in the getattr() function
    #checkList = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    #checkTF = [checkCharacters(a, x) for x in checkList] 
    try:
        #checkTF = checkCharacters(a, func)
        checkTF = [checkCharacters(a, x) for x in checkList] 

        if len(checkList) > 1:
            # prints True of False for each attribute.
            print(*checkTF, sep='\n')
        else:
            print(*checkTF)
    except:
        print("\nError: make sure the function argument is valid " \
              "and is also input as a string.")

    
