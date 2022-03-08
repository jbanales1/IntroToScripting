import re
import random

#Author: Jesus Banales
#Date Started: 3/7/2022

"""
Part 1: Creates student class with attributes firstName, lastName, email, and allCourse(list of course grades).
First read information from file into a string, use regular expression to find first names and place them into
a list. Afterwards remove spaces and \n. Does the same with last names except it removes space before and after.
Uses regular expression to find all emails and store in list. Then used regular expressions to find list of 
course marks, nested for loop and if statements used to separate numbers into actual lists from string format.
Each list is stored in a list of lists. For loop is then used to create a list of student objects using the
information gathered from the text file.
Using code from previous assignment, 25 student objects are made and their attributes are then appended to the 
same document that was used to create previously mentioned list of students. The student objects are also added 
to the list of students created before.
Next this list is sorted using the firstName attribute of the student. The list attributes are then written to
a new file in the same format as the previous file.
"""

class Student():
    #constructor takes fName, lName, email and cList as parameters and sets the values
    def __init__(self, fName, lName, eMail, cList):
        self.firstName = fName
        self.lastName = lName
        self.email = eMail
        self.allCourse = cList
    #to string function used for displaying class attributes 
    def __str__(self):
        return '{self.firstName} {self.lastName} {self.email} {self.allCourse}'.format(self=self)
        
def partOne():
    #students.txt file opened to store info in string (studentDetails)
    infile = open('students.txt', 'r')
    studentDetails = infile.read()
    infile.close()
    
    #use regular expression to find first names and strip functions to remove space and newline
    stuFnames = re.findall('\n[A-Z]+[a-z]+\s', studentDetails)
    for num in range(0, len(stuFnames)):
        temp = stuFnames[num].rstrip()
        temp = temp.lstrip('\n')
        #Change current string to edited string
        stuFnames[num] = temp
    
    #use regular expression to find last names and strip functions to remove spaces
    stuLnames = re.findall('\ +[A-Z]+[a-z]+\s', studentDetails)
    stuLnames.pop(0)
    for num in range(0, len(stuLnames)):
        temp = stuLnames[num].rstrip()
        temp = temp.lstrip()
        #Change current string to edited string
        stuLnames[num] = temp
    
    #find all emails using regular expressions and store in list
    stuEmails = re.findall('[a-z]+@islander.tamucc.edu', studentDetails)
    
    #find all course grades with regular expression (special case with final line)
    uneditedCourse = re.findall('\d+,\d+,\d+,\d+,\d+,\d+\n', studentDetails)
    uneditedCourse.append(re.findall('\d+,\d+,\d+,\d+,\d+,\d+$', studentDetails)[0])
    
    #Create a list to hold lists
    listOfLists = []
    #go through each string (list of course marks) in the list of strings (list of lists of course marks)
    #then go through each character in every individual list of course marks, use a temp string value to
    #hold an individual mark, and add each mark to a temporary list of marks(at a comma or at the end of the string), 
    #append each list of marks to the list of marks once you've gone through the entire string and extracting 
    #all marks
    for numList in uneditedCourse:
        tempList = [0, 0, 0, 0, 0, 0]
        temp = ""
        current = 0
        for ind in range(0, len(numList)):
            if not numList[ind].isdigit():
                tempList[current] = int(temp)
                current += 1
                temp = ""
            else:
                temp = temp + numList[ind]
                if ind == len(numList)-1:
                    tempList[current] = int(temp)
        listOfLists.append(tempList)
    
    #Create list of students, use for loop to create a temporary student and then append it to list
    listOfStudents = []
    print("List of students gathered from original text file: ")
    for num in range(0, len(stuFnames)):
        tempStudent = Student(stuFnames[num], stuLnames[num], stuEmails[num], listOfLists[num])
        listOfStudents.append(tempStudent)
        print(listOfStudents[num])
    print("\n\n")
    
    
    #Open the file again to append
    outfile = open('students.txt', 'a')
    
    #First name of each student will be student
    tempFirst = "Student"
    tempLast = ""
    
    print("Students being appended to file:")
    #Go through loop 25 times
    for i in range(0, 25):
        #newline, since we do not want to write on the same last line
        outfile.write('\n')
        #last name will be current iteration in loop
        tempLast = str(i)
        #generate some random marks for course list
        tempScores = [0, 0, 0 ,0 ,0 ,0]
        for i in range(0, 6):
            tempScores[i] = random.randint(0, 100)
        #create email for students
        tempEmail = tempFirst[0].lower() + str(tempLast) + "@islander.tamucc.edu"
        
        #create temp student and append it to list
        tempStudent = Student(tempFirst, tempLast, tempEmail, tempScores)
        print(tempStudent)
        listOfStudents.append(tempStudent)
        
        #write out student information
        outfile.write(tempFirst)
        outfile.write(" ")
        outfile.write(tempLast)
        outfile.write(" ")
        outfile.write(tempEmail)
        outfile.write(" ")
        for num in range(0, len(tempScores)):
            outfile.write(str(tempScores[num]))
            if num != len(tempScores)-1:
                outfile.write(",")
    print("\n\n")
    outfile.close()
    
    
    #Sort previously created list using student first name
    listOfStudents.sort(key=lambda x: x.firstName)
    print("Sorted list of students being added to final file:")
    for student in listOfStudents:
        print(student)
    
    #open new file to write in
    sortout = open('sorted_students.txt', 'w')
    
    #go through the sorted list of students and write out all information in new file
    for ind in range(0, len(listOfStudents)):
        sortout.write(listOfStudents[ind].firstName)
        sortout.write(" ")
        sortout.write(listOfStudents[ind].lastName)
        sortout.write(" ")
        sortout.write(listOfStudents[ind].email)
        sortout.write(" ")
        for num in range(0, len(listOfStudents[ind].allCourse)):
            sortout.write(str(listOfStudents[ind].allCourse[num]))
            if num != len(listOfStudents[ind].allCourse)-1:
                sortout.write(",")
        if ind != len(listOfStudents)-1:
            sortout.write('\n')
    
    sortout.close()
    
"""
Part 2: Creates two functions, one to read files (takes read object) and returns string holding the text 
gathered from the file. Another function for writing to files, it takes 3 string parameters and writes 
them all to a text file. In the main function we use a try except block to open the files in case they 
are not able to be found. The readFile method is called three times, once for every file we want to read
and the writeFile is called once to write all the strings to the final text file at once.
"""

#takes file object as parameter, reads file and returns string holding value
def readFile(inFile):
    tempTxt = inFile.read()    
    return tempTxt
    
#takes three strings as parameters, opens final_file.txt and writes all three
#strings into the file with newlines in between before closing the file
def writeFile(one, two, three):
    inFile = open('final_file.txt', 'a')
    inFile.write(one)
    inFile.write('\n')
    inFile.write(two)
    inFile.write('\n')
    inFile.write(three)
    inFile.close()

def partTwo():
    #use try except block to make sure program doesnt break if files arent found
    try:
        #use read objects for text files
        inOne = open('f1.txt', 'r')
        inTwo = open('f2.txt', 'r')
        inThree = open('f3.txt', 'r')
        
        #call functions and store returned strings
        firstTxt = readFile(inOne)
        secondTxt = readFile(inTwo)
        thirdTxt = readFile(inThree)
        
        #close all read objects
        inOne.close()
        inTwo.close()
        inThree.close()
        
        #call writeFile function to write strings to final_file.txt
        writeFile(firstTxt, secondTxt, thirdTxt)
    except:
        print("Error opening file")

if __name__ == '__main__':
    partOne()
    partTwo()