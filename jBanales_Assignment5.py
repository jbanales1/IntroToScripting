import math

#Author: Jesus Banales
#Date Started: 3/1/2022

"""
Part 1: Creates a dictionary with corresponding characters and their translations in morse code.
User is asked to enter a string, and it is then translated using a for loop and the dictionary.
Output is then printed out (translation of string into morse code)
"""

def partOne():
    #extraordinarily long dictionary with morse code conversions inside
    morseCode = {' ': ' ',
             ',': '--..--',
             '.': '.-.-.-',
             '?': '..--..',
             '0': '-----',
             '1': '.----',
             '2': '..---',
             '3': '...--',
             '4': '....-',
             '5': '.....',
             '6': '-....',
             '7': '--...',
             '8': '---..',
             '9': '----.',
             'A': '.-',
             'B': '-...',
             'C': '-.-.',
             'D': '-..',
             'E': '.',
             'F': '..-.',
             'G': '--.',
             'H': '....',
             'I': '..',
             'J': '.---',
             'K': '-.-',
             'L': '.-..',
             'M': '--',
             'N': '-.',
             'O': '---',
             'P': '.--.',
             'Q': '--.-',
             'R': '.-.',
             'S': '...',
             'T': '-',
             'U': '..-',
             'V': '...-',
             'X': '-..-',
             'Y': '-.--',
             'Z': '--..'}
    
    #Asking user for input and creating string to hold translation
    userIn = input("Please enter a string to translate to morse code: ")
    
    morsedOut = ""
    
    #For loop goes through each character in string and appends corresponding
    #translation to output string
    for ch in userIn:
        morsedOut = morsedOut + morseCode[ch.upper()]
    
    #Translated morse code printed out
    print("Morse code of ", userIn, " is ", morsedOut)
    print()

"""
Part 2: Two functions created, one to count vowels and the other to count consonants. User is
asked to enter a string and using previously mentioned functions the number of vowels and consonants
are displayed to the user.
"""

def getNumVows(someStr):
    count = 0
    #Check each character to see if it is a,e,i,o,u, if it is then iterate count
    for ch in someStr:
        if ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U':
            count += 1
    #Return count
    return count

def getNumCons(someStr):
    count = 0
    #Check each character to see if it is not a,e,i,o,u, but is a letter (a consonant) 
    #if it is then iterate count
    for ch in someStr:
        if ch.isalpha() and ch.upper() != 'A' and ch.upper() != 'E' and ch.upper() != 'I' and ch.upper() != 'O' and ch.upper() != 'U':
            count += 1
    #Return count
    return count

def partTwo():
    #User is asked to enter string and using getNumVows and getNumCons, number of vowels and
    #consonants are displayed
    userIn = input("Please enter a string to count vowels and consonants: ")
    print("Number of vowels in string: ", getNumVows(userIn))
    print("Number of consonants in string: ", getNumCons(userIn))
    print()
    
"""
Part 3: Uses for loop to count number of individual letters, digits and symbols in a string. Also uses for loop
to modify a string to remove special characters and punctuation. Uses for loop to replace hyphens in a string with
spaces and uses for loop to remove all consonants from a string. All modified strings are displayed for the user.
"""

def partThree():
    #Display string we will be counting letters,digits and symbols for
    print("Counting numbers of leters, digits, and symbols in P@#yn26at^&i5ve")
    
    #Setting string and count variables
    strOne = 'P@#yn26at^&i5ve'
    letterCount = 0
    digitCount = 0
    symbolCount = 0
    
    #Go through each character in string, if alphabetical, iterate corresponding count by 1
    #same goes for digit, if its neither digit or alpha then it must be a special symbol so iterate that count
    for ch in strOne:
        if ch.isalpha():
            letterCount += 1
        elif ch.isdigit():
            digitCount += 1
        else:
            symbolCount += 1
    
    #Display different counts
    print("Number of letters: ", letterCount)
    print("Number of digits: ", digitCount)
    print("Number of symbols: ", symbolCount)
    print()
    
    #Set initial string and create string variable to hold modified value
    strTwo = '/*Jon is @developer & musician'
    modTwo = ""
    
    #Go through each character in the string, if the character is alphabetical, a digit, or a spaces
    #add it, (dont add special characters)
    for ch in strTwo:
        if ch.isalpha() or ch.isdigit() or ch.isspace():
            modTwo = modTwo + ch
    
    #Display before and after of string
    print("String before modification: ", strTwo)
    print("String after modification: ", modTwo)
    print()

    #Set initial string and create string variable to hold modified value    
    strThree = 'Emma-is-a-data-scientist'
    modThree = ""
    
    #Go through each character in the loop and if the character is a hyphen instead of adding it to
    #the modified string, add a space, and add all other characters regardless
    for ch in strThree:
        if ch == '-':
            modThree = modThree + ' '
        else:
            modThree = modThree + ch
    
    #Display string before and after modification
    print("String before modification: ", strThree)
    print("String after modification: ", modThree)
    print()
    
    #Set initial string and create string variable to hold modified value
    strFour = 'Hello, have a good day'
    modFour = ""
    
    #Go through each character in string, if it is a vowel or a space then add it,
    #therefore we do not add consonants to the modified version of the string
    for ch in strFour :
        if ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U' or ch.isspace():
            modFour = modFour + ch
    
    #Display string before and after modification
    print("String before modification: ", strFour)
    print("String after modification: ", modFour)
    print()
    
"""
Part 4: Asks user to enter a number of integers greater than 10, this will be the number of integers they are asked
to enter. The user is then asked to enter numbers ranging from 0-100 and the average, median and std deviation are
calculated. Some input validation is implemented in the form of while loops and if statements for this. Afterwards
a second list is made using the first list's values. The second list contains division from an element
and the element that is next after it in the original list. A try and except block is used to prevent the code 
from running into an error at runtime.
"""

def partFour():
    #Flag is used in while loop for input validation, assumed true from beginning
    badInput = True
    #While flag is true, ask for input and use if statement to make sure user enters
    #a digit and that it is greater than 10, if user input is validated change flag 
    #and end loop
    while badInput == True:
        numOfIns = input("Enter number of integers greater than 10: ")
        if not numOfIns.isdigit() or int(numOfIns) <= 10:
            print("Invalid input, try again")
        else:
            badInput = False
    
    #Create list to hold integers
    listOfIns = []
    
    #Use number gathered before for for loop range 
    for num in range(0, int(numOfIns)):
        #Once again using flag for input validation
        badInput = True
        #While flag is true, ask for num in range 0-100, if not in range then try again,
        #otherwise set flag to false and continue
        while badInput == True:
            temp = input("Enter a number between 0-100: ")
            if not temp.isdigit() or int(temp) < 0 or int(temp) > 100:
                print("Invalid input, try again")
            else:
                badInput = False
        #Append value to list after validated
        listOfIns.append(int(temp))
    
    #Display list
    print("List of integers: ", listOfIns)
    
    #Find average using sum and length and display
    avg = sum(listOfIns)/len(listOfIns)
    print("Average of list: ", avg)
    
    #Sort copy of list for median
    sortedList = listOfIns.copy()
    sortedList.sort()
    #Find median if list is even by finding average of two middle elements
    if len(sortedList) % 2 == 0:
        firstMiddle = (len(sortedList)+1)/2
        secondMiddle = (len(sortedList)+1)/2 + 1
        median = (sortedList[firstMiddle] + sortedList[secondMiddle])/2
    #Find median of odd list by finding middle element
    else:
        middle = int((len(sortedList)+1)/2 - 1)
        median = sortedList[middle]
    
    #Display median
    print("Median of list: ", median)
    
    #Calculating std dev using single variable
    stdDev = 0
    #First get each number in list and subtract average before squaring and sum them together
    for num in listOfIns:
        stdDev += (num - avg)**2  
    #Then divide by length-1
    stdDev /= len(listOfIns)-1
    #Then square root the value to get final std dev
    stdDev = math.sqrt(stdDev)
    
    #Display std dev
    print("Standard deviation of list: ", stdDev)
    
    #Create second list
    divList = []
    try:
        #Try to append division of some element and the element after it
        #Possible error of division by zero
        for num in range(0, len(listOfIns)-1):
            temp = listOfIns[num]/listOfIns[num+1]
            divList.append(temp)
    except:
        #If exception occurs output that there was some exception
        print("An exception has occurred creating the division list")
    
    #Regardless of exception, display division list
    print("Division list: ", divList)
    print()
    
"""
Part 5: Converts a given string using loops. First capitalizes all first letters of each word in the string, second
removes spaces, third replaces 's' with '$', fourth only capitalizes first letters of certain words.
"""

def partFive():
    #Original string
    mainStr = "this is the string for the class"
    
    #Variables to hold other copies of string
    copyOne = ""
    copyTwo = ""
    copyThree = ""
    copyFour = ""
    
    #index to hold previous element index
    beforeNum = 0
    #Go from index 0 to the final index
    for num in range(0, len(mainStr)):
        #If its the first index capitalize the letter
        if num == 0:
            copyOne = copyOne + mainStr[num].upper()
        #if the previous index held a space, capitalize current letter
        elif mainStr[beforeNum] == ' ':
            copyOne = copyOne + mainStr[num].upper()
        #otherwise copy the letter the same
        else:
            copyOne = copyOne + mainStr[num]
        #update previous index
        beforeNum = num
    
    #Print new copy
    print(copyOne)
    
    #Now iterating through each character in copyOne
    for ch in copyOne:
        #if character is not a space then add it to the new string
        if ch != ' ':
            copyTwo = copyTwo + ch
    
    #Display new string
    print(copyTwo)
    
    #Iterate through first copy again
    for ch in copyOne:
        #If the character is an s, dont add it but add $ instead
        if ch == 's':
            copyThree = copyThree + '$'
        #Otherwise add character the same
        else:
            copyThree = copyThree + ch
    
    #Print new string 
    print(copyThree)
    
    #Utilizing index for character before current again
    beforeNum = 0
    #Go through each index of the string
    for num in range(0, len(mainStr)):
        #If at first index, capitalize that letter
        if num == 0:
            copyFour = copyFour + mainStr[num].upper()
        #if previous index held character that was a space and the current letter is an s or a c,
        #capitalize that letter and add it
        elif mainStr[beforeNum] == ' ' and mainStr[num] == 's' or mainStr[num] == 'c':
            copyFour = copyFour + mainStr[num].upper()
        #Otherwise add the letter the same
        else:
            copyFour = copyFour + mainStr[num]
        #and update the previous index
        beforeNum = num
    
    #print the new string
    print(copyFour)

#Main function calls functions for parts 1-4    
if __name__ == '__main__':
    partOne()
    partTwo()
    partThree()
    partFour()
    partFive()