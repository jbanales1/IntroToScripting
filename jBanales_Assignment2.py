#Author: Jesus Banales
#Date Started: 2/3/2022

"""
Part 1: Prints pattern of asterisks in the shape of a ramp using for loop
"""

#Nested for loop, inner loop iterates to temp (outer loop counter) printing asterisk each time
for temp in range(1, 6):
    for temp2 in range(0,temp):
        print("*", end = " ")
    print()
print()

#For loop with two other for loops inside, first for loop has number of iterations
#Second for loop prints spaces, using difference of outer for loop and total amount of iterations
#Third for loop prints asterisk number of times corresponding to outer for loop
for temp in range(1, 6):
    for temp2 in range(0, 5 - temp):
        print(end = "  ")
    for temp3 in range(0, temp):
        print("*", end = " ")
    print()
print()

"""
Part 2: Takes two inputs and calculates values for factorial using for loop
"""

#Collecting numbers n and r, finding difference
numberN = int(input("Enter first number: "))
numberR = int(input("Enter second number: "))
difference = numberN - numberR

#Initializing factorials
factN = 1
factR = 1
factDifference = 1

#Calculating n factorial
for temp in range(1, numberN+1):
    factN = factN * temp

#Calculating r factorial
for temp in range(1, numberR+1):
    factR = factR * temp

#Calculating (n-r) factorial
for temp in range(1, difference+1):
    factDifference = factDifference * temp

#Printing results of calculations
print("n!/(r!(n-r)!) is equal to: ", factN/(factR*factDifference))
print("n!/(n-r)! is equal to: ", factN/factDifference) 

print()

"""
Part 3: Using a for loop to sort a list into a new list and print it out
"""

#Setting up original list and new (sorted) list
ogList = [20, 68, 41, 88, 16, 40, 65, 97, 85]
newList = []


length = len(ogList)

#While length of sorted list is not equal to the length of the original list, execute
while len(newList) != length:
    #Assume that first index is smallest, iterate through entire list comparing and
    #swapping smallest index when a smaller value is found before popping smallest value into
    #new sorted list
    smallestIndex = 0 
    for tempIndex in range(0, len(ogList)):
        if(ogList[tempIndex] < ogList[smallestIndex]):
            smallestIndex = tempIndex
    tempVal = ogList.pop(smallestIndex)
    newList.append(tempVal);
    
print("Sorted list: ", newList);

"""
Part 4: Finds the sum of a given list, creates new list with even numbers and displays the list as well
as the sum of this new even list, and finally uses the original list to create a new list of odd numbers
before finding the sum of all numbers in the odd list
"""

#Using for loop to sum all integers in list and prints them
sum = 0

for temp in newList:
    sum += temp
    
print("Sum of list: ", sum)

#Using for loop and if statement using modulus to find even numbers and add them to new list
evenList = []

for temp in newList:
    if temp % 2 == 0:
        evenList.append(temp)
        
print("Even list: ", evenList)

#Using for loop to sum up even list
sum = 0

for temp in evenList:
    sum += temp
    
print("Sum of even list: ", sum)

#Using for loop and if statement using modulus to find odd numbers and add them to new list
oddList = []

for temp in newList:
    if temp % 2 == 1:
        oddList.append(temp)
        
print("Odd list: ", oddList)

#Using for loop to sum up odd list
sum = 0

for temp in oddList:
    sum += temp
    
print("Sum of odd list: ", sum)
print()

"""
Part 5: Finding all prime numbers from range of 2-50 using for loop
"""

print("All prime numbers between 2 and 50: ")

#Iterate from 2-50
for temp in range(2, 50):
    #Assume the number is prime until proven otherwise
    isPrime = True
    #Divide the current number by 2, 3, 4,.. n to see if it is divisible by other numbers
    for n in range(2, temp):
        #If it is divisible by another number then it is not prime
        if temp % n == 0:
            isPrime = False
    
    if isPrime == True:
        print(temp)
print()

"""
Part 6: Creating 3 different methods, for questions 1-3
"""

def firstMethod():
    #Nested for loop, inner loop iterates to temp (outer loop counter) printing asterisk each time
    for temp in range(1, 6):
        for temp2 in range(0,temp):
            print("*", end = " ")
        print()
    print()

    #For loop with two other for loops inside, first for loop has number of iterations
    #Second for loop prints spaces, using difference of outer for loop and total amount of iterations
    #Third for loop prints asterisk number of times corresponding to outer for loop
    for temp in range(1, 6):
        for temp2 in range(0, 5 - temp):
            print(end = "  ")
        for temp3 in range(0, temp):
            print("*", end = " ")
        print()
    print()

def secondMethod(n, r):
    #Collecting numbers n and r, finding difference
    numberN = n
    numberR = r
    difference = numberN - numberR

    #Initializing factorials
    factN = 1
    factR = 1
    factDifference = 1

    #Calculating n factorial
    for temp in range(1, numberN+1):
        factN = factN * temp

    #Calculating r factorial
    for temp in range(1, numberR+1):
        factR = factR * temp

    #Calculating (n-r) factorial
    for temp in range(1, difference+1):
        factDifference = factDifference * temp

    #Printing results of calculations
    print("n!/(r!(n-r)!) is equal to: ", factN/(factR*factDifference))
    print("n!/(n-r)! is equal to: ", factN/factDifference) 

    print()

def thirdMethod(ogList):
    #Setting up new (sorted) list
    newList = []

    length = len(ogList)

    #While length of sorted list is not equal to the length of the original list, execute
    while len(newList) != length:
        #Assume that first index is smallest, iterate through entire list comparing and
        #swapping smallest index when a smaller value is found before popping smallest value into
        #new sorted list
        smallestIndex = 0 
        for tempIndex in range(0, len(ogList)):
            if(ogList[tempIndex] < ogList[smallestIndex]):
                smallestIndex = tempIndex
        tempVal = ogList.pop(smallestIndex)
        newList.append(tempVal);
        
    print("Sorted list: ", newList);
    print()

"""
Part 7: Takes number from user and analyzes it to see if it is an armstrong number
"""

#Taking input and casting it to a string
num = input("Enter a number: ")
strNum = str(num)

armstrong = 0

#Going through each element of the string (number) and putting it to the power of
#the length of the string before adding it to the final result
for temp in strNum:
    numTwo = int(temp)**len(num)
    armstrong += numTwo

#If result is equal to the original number it is an armstrong number, otherwise not
if armstrong == int(num):
    print(num, " is an armstrong number")
else:
    print(num, " is not an armstrong number")
print()

"""
Part 8: Method for calculating fibonacci sequence using user input
"""

def computeFib(fibNum):
    #creating list to hold fib sequence
    fibSequence = []
    
    firstFib = 0
    secondFib = 1
    
    #Iterate from 0 to user input
    for temp in range(0, fibNum):
        #Append 1st and 2nd elements as 0 and 1 respectively
        if temp == 0:
            fibSequence.append(firstFib)
            continue
        if temp == 1:
            fibSequence.append(secondFib)
            continue
            
        #Append nextFib(sum of previous two numbers) and change firstFib
        #to secondFib and secondFib to nextFib
        nextFib = firstFib + secondFib
        firstFib = secondFib
        secondFib = nextFib
        fibSequence.append(nextFib)
    
    print("Fibonacci sequence for : ", fibSequence)
    print()
    
#Main function runs first method, second method with sample input, third method
#with provided list and fib sequence using user input
if __name__ == '__main__':
    firstMethod()

    secondMethod(8, 3)

    passedList = [20, 68, 41, 88, 16, 40, 65, 97, 85]
    thirdMethod(passedList)
    
    fibInput = int(input("Enter a number for fib sequence: "))
    computeFib(fibInput)

"""
Part 9: Correcting code to print even numbers
"""

print("Even numberse from 1-10:")

loop_counter = 1
while loop_counter <= 10:
    #print(loop_counter) <-- not necessary
    if loop_counter%2 == 0:
        print(loop_counter)
    loop_counter += 1 #Here we are increasing loop count by 1