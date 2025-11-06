# program to convert roman numerals tp integers

def romanToInt(romanInput):

    # all roman units with integer equivalent values
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    #result
    resultInteger = 0

    # go from 0 to len-1: if integer equivalent of current roman is less than next roman, subtract it else add it
    for i in range(0, len(romanInput)- 1):
        if roman[romanInput[i]] < roman[romanInput[i + 1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]
        
    return resultInteger + roman[romanInput[-1]]

# input from user
roman = input("Enter a roman numeral: ")

# Print the integer
print("Integer equivalent : ", romanToInt(roman))