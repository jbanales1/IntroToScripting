import random
import re

#Midterm Exam
#Jesus Banales - 3/10/2022

"""
True or false questions
"""

#Question 1: True
#Question 2: True
#Question 3: False
#Question 4: False
#Question 5: False
#Question 6: True
#Question 7: True
#Question 8: True
#Question 9: False
#Question 10: False

"""
Short answer questions
"""

#Question 1: A decision structure is a conditional statement, if a condition is met then some code is executed.
#A repetition structure is similar, however it will execute this code over and over, and a decision structure will
#only execute once.
#Question 2: A class is a blueprint in a way for a programmer made data type. It can have private attributes/variables
#and built in methods for the class itself. An instance of a class is an object, you could say its the blueprint in work.
#The object can store values as attributes and make use of the predefined methods for the class.
#Question 3: A recursive function is a function that calls itself until some base case is met. This is the case in
#which we do not want the function to call itself again.
#Question 4: First an object must be created to hold the file reading/writing/appending object so it can be stored.
#Next you can call a function whether it be read/write to make your changes to the file or read it and afterwards
#the file object must be closed.
#Question 5: Inheritance is the idea that a super class or parent class can pass on attributes or methods to it's
#child or sub class. One class, an employee, can pass down it's attributes such as employee number or base salary
#down to some more specific sub class, a mechanic or something of this sort. It can also pass down methods.


"""
Coding challenges
"""

#Question 1
def questOne():
    print("Part one: ")
    for num in range(2, 50, 2):
        print(num, end = " ")
    print()
    
    for num in range(1, 50):
        print(num, end = " ")
    print("\n\n")

#Question 2   
def questTwo():
    print("Part two: ")
    randList = []
    for num in range(0, 20):
        temp = random.randint(0, 100)
        randList.append(temp)
    print("Regular list: ", randList)
    randList.sort()
    print("Sorted list: ", randList)
    randList.reverse()
    print("Reversed list: ", randList)
    print("\n\n")

#Question 3
def questThree():
    print("Part three: ")
    students = {}
    for num in range (0, 3):
        tempList = []
        stuName = "Student " + str(num)
        for num2 in range (0, 6):
            temp = random.randint(0, 100)
            tempList.append(temp)
        students[stuName] = tempList
    print(students)
    print("\n\n")
    
#Question 4    
def questFour():
    print("Part four: ")
    print("Type A Seat: $20\nType B Seat: $15\nType C Seat: $10")
    try:
        seatsA = int(input("Enter number of tickets for A seats: "))
        seatsB = int(input("Enter number of tickets for B seats: "))
        seatsC = int(input("Enter number of tickets for C seats: "))
        print("Total income generated: $", seatsA*20 + seatsB*15 + seatsC*10)
    except ValueError:
        print("Invalid input, please enter integer")
    print("\n\n")
    
#Question 5
#def findSecondLargest(listOfNums):
    #if():
        #return secondLargest
    #elif:

#def questFive():
    #print("Part five: ")
    
    #findSecondLargest()
    #print("\n\n")
    
#Question 6
class Clothing():
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = str(units)
        self.__price = str(price)
    
    def getDesc(self):
        return self.__description
    
    def getUnits(self):
        return self.__units
        
    def getPrice(self):
        return self.__price

def questSix():
    print("Part six: ")
    clothList = []
    temp = Clothing("Jacket", 40, 59.95)
    clothList.append(temp)
    temp = Clothing("Designer Jeans", 100, 34.95)
    clothList.append(temp)
    temp = Clothing("Shirt", 200, 24.95)
    clothList.append(temp)
    print(clothList)
    print("\n\n")
    
    outfile = open("clothing.txt", 'w')
    for item in clothList:
        outfile.write(item.getDesc())
        outfile.write(" ")
        outfile.write(item.getUnits())
        outfile.write(" ")
        outfile.write(item.getPrice())
        outfile.write("\n")
    outfile.close()

#Question 7
def questSeven():
    print("Part seven: ")
    userIn = input("Please enter anything: ")
    
    if userIn.isdigit():
        num = userIn
        print("User entered only: ", num)
    elif userIn.isalpha():
        userIn = userIn.lstrip()
        userIn = userIn.rstrip()
        userIn = userIn.upper()
        count = 0
        for ch in userIn:
            if ch.upper() == 'T':
                count += 1
        print("Edited input: ", userIn)
        print("Number of t's: ", count)
    
    print("\n\n")

#Question 8
def questEight():
    print("Part eight: ")
    firstSet = set([1, 2, 3, 4, 5])
    secondSet = set([3, 4, 5, 6, 7])
    print("First set: ", firstSet)
    print("Second set: ", secondSet)
    print("Union: ", firstSet.union(secondSet))
    print("Intersection: ", firstSet & secondSet)
    
    print("\n\n")
    
def bonus():
    string_test = "Hello my name is Rajesh, and my number is 123456789. My friend's name is Timmy, and his phone number is 987654321."
    
    names = re.findall("\ +[A-Z]+[a-z]+\,", string_test)
    numbers = re.findall("\s+[0-9]+\.", string_test)
    
    print(names)
    print(numbers)
    
if __name__ == '__main__':
    questOne()
    questTwo()
    questThree()
    questFour()
    #questFive()
    questSix()
    questSeven()
    questEight()
    bonus()