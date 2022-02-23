import random

#Author: Jesus Banales
#Date Started: 2/22/2022

"""
Part 1: Defines class, same as previous assignment. Uses while loop with if statements to let user either
look up an employee from dictionary, add employee to dictionary, edit an employee or delete an employee.
"""

class Employee():
    #init function takes first and last name, id number, department and job title
    #as arguments and sets values in the object
    def __init__(self, fName, lName, idNum, dept, title):
        self.firstName = fName
        self.lastName = lName
        self.idNumber = idNum
        self.department = dept
        self.jobTitle = title
        
        #Part 3
        #fullname attribute concatentates firstName and lastName with space in between
        self.fullName = self.firstName + " " + self.lastName
        #email concatenates firstName, period, lastName and then @company.com
        self.email = self.firstName.lower() + "." + self.lastName.lower() + "@company.com"
    
    #str returns first and last name, id number, department, and job title
    def __str__(self):
        return 'Name: {self.firstName} {self.lastName}\nIdNumber: {self.idNumber}\nDepartment: {self.department}\nJob Title: {self.jobTitle}\n'.format(self=self)

def partOne():
    #initialize flag and create dictionary to hold ids of employees and employee objects
    exitFlag = False
    empDict = {}
    
    #While the user does not input 5 the loop continues
    while exitFlag != True:
        #Output options and gather input from user
        print("1. Look up employee\n2. Add new employee\n3. Change employee\n4. Delete employee\n5. Quit\n")
        option = input("Enter an option using the corresponding number: ")
        
        #If user enters 1 and the dictionary has an object, look for the ID in the dictionary
        #print if employee ID is found, output info if not found
        if option == '1':
            if len(empDict) < 1:
                print("Dictionary is empty")
            else:
                tempID = int(input("Enter employee ID to look for: "))
                if tempID in empDict:
                    print(empDict[tempID])
                else:
                    print("Employee with ID ", tempID, " not found in dictionary")
        
        #If user enters 2 ask for information of employee, create employee object using input
        #and add employee to dictionary along with employee ID, also display the employee after
        elif option == '2':
            tempFirst = input("Enter first name: ")
            tempLast = input("Enter last name: ")
            tempID = int(input("Enter ID: "))
            tempDept = input("Enter department: ")
            tempTitle = input("Enter job title: ")
            tempEmployee = Employee(tempFirst, tempLast, tempID, tempDept, tempTitle)
            empDict[tempID] = tempEmployee
            
            print("Employee added:")
            print(empDict[tempID])
        
        #If user enters 3, ask for ID of employee they wish to edit and check if in dict
        #If ID is found, use pop to remove employee and gain employee object to edit
        #also ask for employee information, edit employee and add it back to the dictionary
        elif option == '3':
            tempID = int(input("Enter the ID of an employee to edit: "))
            if tempID in empDict:
                tempEmployee = empDict.pop(tempID)
                
                tempFirst = input("Enter first name: ")
                tempLast = input("Enter last name: ")
                tempDept = input("Enter department: ")
                tempTitle = input("Enter job title: ")
                tempEmployee.firstName = tempFirst
                tempEmployee.lastName = tempLast
                tempEmployee.department = tempDept
                tempEmployee.jobTitle = tempTitle
                
                empDict[tempID] = tempEmployee
                
                print("Employee added:")
                print(empDict[tempID])
            #If ID isnt found, output that its not in dict
            else:
                print("Employee with ID ", tempID, " not found in dictionary")
            print()
        
        #If input is 4, ask for ID of employee that should be deleted, if found the
        #ID and employee object are removed from dict, otherwise output is shown 
        #so user can see that the object was not found
        elif option == '4':
            tempID = int(input("Enter the ID of an employee to delete: "))
            if tempID in empDict:
                tempEmployee = empDict.pop(tempID)
                print("Employee deleted:")
                print(tempEmployee)
            else:
                print("Employee with ID ", tempID, " not found in dictionary")
        
        #if input is 5 change the flag so the loop can end
        elif option == '5':
            exitFlag = True
        
        #if input is not 1-5 it is invalid input
        else:
            print("Invalid Input, try again.")
    
"""
Part 2: Creates list and allows user to enter 20 numbers, outputs list, along with smallest and largest numbers
along with total sum and average of list
"""

def partTwo():
    #Create new list
    numList = []

    #Let user input 20 numbers to add to the end of the list
    for num in range(0, 20):
        temp = int(input("Enter num to add to list: "))
        numList.append(temp)

    #Print list, print min(smallest), max(largest), total sum and average of list
    print(numList)
    print("Smallest number in the list: ", min(numList))
    print("Largest number in the list: ", max(numList))
    print("Total of numbers in the list: ", sum(numList))
    print("Average of numbers in the list: ", sum(numList)/len(numList))
    print()

"""
Part 3: Create dictionary, allow user to enter some number n, for loop will iterate n times adding each
number as its key and its square as the value stored, dict displayed afterwards
"""

def partThree():
    #create dictionary, and ask for user's number n
    numDict = {}
    n = int(input("Enter some number n: "))

    #Loop goes from 1-n, using num as key and num*num as value
    for num in range(1, n):
        numDict[num] = num*num
    
    #Display dict
    print(numDict)
    print()

"""
Part 4: Defines functions to find second largest number in a list and to return a list without duplicate elements
using some other list. A list is created composed of 100 random numbers ranging from 0-20. Both functions are
called to find the second largest number and display a list that has no duplicates.
"""

def findSecondLargest(numberList):
    #use two indexes, largest and secondLargest, assume they are both at index 0 from beginning
    largest = 0
    secondLargest = 0
    
    #Go from index 1 to the end of the list
    for num in range(1, len(numberList)):
        #If a larger number is found, secondLargest is now the value of the previous largest
        #and the new largest is set, if number is between secondLargest and largest, set
        #secondlargest to that num
        if numberList[num] > numberList[largest]:
            secondLargest = largest
            largest = num
        elif numberList[num] > numberList[secondLargest] and numberList[num] < numberList[largest]:
            secondLargest = num
    
    #return the value at secondLargest index
    return numberList[secondLargest]
    
def removeDuplicates(numberList):
    #create new list
    woDuplicates = []
    
    #Go through each value in list passed
    for num in numberList:
        #if the number is not already in the list without duplicates, append it
        if num not in woDuplicates:
            woDuplicates.append(num)
    
    #return new list without duplicate elements
    return woDuplicates

def partFour():
    #create new list
    numListTwo = []
    
    #add 100 random elements ranging from 0-20
    for num in range(0, 100):
        temp = random.randint(0, 20)
        numListTwo.append(temp)
    
    #output list
    print("100 random numbers with range 0-20:")
    print(numListTwo)
    
    #Display second largest number and new list without duplicate elements
    print("Second largest number: ", findSecondLargest(numListTwo))
    print("List without duplicate elements: ", removeDuplicates(numListTwo))


#Main function calls functions for parts 1-4    
if __name__ == '__main__':
    partOne()   
    partTwo()
    partThree()
    partFour()