import random

#Author: Jesus Banales
#Date Started: 2/15/2022

"""
Part 1: Created a car class, init function takes model year and make as arguments, and sets them to
corresponding class variables, sets speed to 0. Accelerate and brake methods, increase and decrease speed
by 5 and get speed method returns current speed. Main function utilizes class by creating a car object
and using accelerate and break method 5 times each and calling get speed function.
"""

class Car():
#init takes year model and make, sets variables and sets speed variable to 0
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
#accelerate adds 5 to speed
    def accelerate(self):
        self.__speed += 5
#breake removes 5 from speed
    def brake(self):
        self.__speed -= 5
#get speed returns speed     
    def get_speed(self):
        return self.__speed

"""
Part 2: Created employee class with first and last name, id number, department and job title class variables.
Also used __str__ method to display employee information in main

Part 3: Added fullname and email attributes which concatenate first and last name along with other characters
which are displayed in main
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

"""
Part 4: Creates student class, takes, first and last name and list of course marks/grades and calculates
percentage, which is sum of all course grades divided by 600. Includes __str__ method that displays name 
and percentage. In main method a list of students is created with random numbers for each student objects
list of grades/marks being set to a random number between 0-100. List is then sorted and the average of
each course is calculated using the student objects list.
"""

class Student():
    #init function takes first name, last name and list of course marks (ints) as arguments
    #percentage is calculated using calcPercentage function, which sums course marks and divides by 600
    def __init__(self, fName, lName, cList):
        self.firstName = fName
        self.lastName = lName
        self.courseList = cList
        
        self.percentage = self.calcPercentage()
    
    #returns first and last name as well as percentage
    def __str__(self):
        return '{self.firstName} {self.lastName}\tPercentage: {self.percentage}'.format(self=self)
    
    #returns percentage which is sum of course marks that is divided by 600
    def calcPercentage(self):
        sum = 0
        for temp in self.courseList:
            sum += temp
        return sum/600*100

if __name__ == '__main__':
    #
    #Part 1
    #
    
    #creating car object with model year 2011, and make as cadillac
    my_car = Car(2011, "Cadillac")
    
    #calls accelerate method 5 times for car object and prints out speed
    for i in range(0, 5):
        my_car.accelerate()
        print("Current speed: ", my_car.get_speed())
    #calls brake method 5 times for car object and prints out speed
    for i in range(0, 5):
        my_car.brake()
        print("Current speed: ", my_car.get_speed())
    print()
    
    #
    #Part 2
    #
    
    #Creating employee objects with information provided
    empOne = Employee("Susan", "Meyers", 47899, "Accounting", "Vice President")
    empTwo = Employee("Mark", "Jones", 39119, "IT", "Programmer")
    empThree = Employee("Joy", "Rogers", 81774, "Manufacturing", "Engineer")
    
    #Using __str__ function to print employee information
    print(empOne, "\n")
    print(empTwo, "\n")
    print(empThree, "\n")
   
    #
    #Part 3
    #
    
    #Using fullname and email attributes in employee to print out corresponding values
    print("Employee One Full Name: ", empOne.fullName)
    print("Employee One Email: ", empOne.email)
    print()
    
    #
    #Part 4
    #
    
    #Creating list for student objects to be stored in, also temporary name which will be Student n
    stuList = []
    tempFirst = "Student"
    tempLast = ""
    
    #Create 25 student objects and append them to stuList, each student will have
    #6 randomly generated marks for their 6 corresponding courses
    for i in range(0, 25):
        tempLast = i
        tempScores = [0, 0, 0 ,0 ,0 ,0]
        for i in range(0, 6):
            tempScores[i] = random.randint(0, 100)
        stuList.append(Student(tempFirst, tempLast, tempScores))
    
    #Display all student objects using str method
    for temp in stuList:
        print(temp)
    print()
    
    #Creating new list for sorted elements
    newList = []
    length = len(stuList)

    #While length of sorted list is not equal to the length of the original list, execute
    while len(newList) != length:
        #Assume that first index is smallest, iterate through entire list comparing and
        #swapping smallest index when a smaller value is found before popping smallest value into
        #new sorted list
        smallestIndex = 0 
        for tempIndex in range(0, len(stuList)):
            if(stuList[tempIndex].percentage < stuList[smallestIndex].percentage):
                smallestIndex = tempIndex
        tempVal = stuList.pop(smallestIndex)
        newList.append(tempVal);
        
    #Display new sorted student objects list
    for temp in newList:
        print(temp)
    print()
    
    #Creating a list for course averages
    courseAverages = [0, 0, 0 , 0 , 0, 0]
    
    #Summing all course marks from each student object, all students marks course 1 summed, 2, 3, etc.
    for temp in newList:
        for i in range(0, 6):
            courseAverages[i] += temp.courseList[i]
    
    #prints marks of each student for course 0
    #for temp in newList:
    #    print(temp.courseList[0]) <-- used to make sure that averages calculated correctly
    #print()
    
    
    #Dividing sum by 25 to get avg and displaying all course avgs
    for i in range(0, 6):
        courseAverages[i] = courseAverages[i]/25
        print("Course ", i+1," Average: ", courseAverages[i])
    