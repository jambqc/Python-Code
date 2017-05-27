def checkCharacters(string, function):
    for letter in string:
        if getattr(letter, function)():
            return True
        else:
            pass
    return False

a = input()
checkList = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
checkTF = [checkCharacters(a, x) for x in checkList] 
print(*checkTF)
