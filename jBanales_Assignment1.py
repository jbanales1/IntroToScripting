"""
Part 1: Prints out name, address, telephone number, and college major
"""
print("Jesus Banales")
print("Corpus Christ, TX, 78413")
print("956-293-5811")
print("Computer Science: Information Systems")
print("\n")

"""
Part 2: Asks user for number of square feet, divides number by 43,560 to get number of acres and displays
"""

#Asking for input
squareFt = float(input("Enter number of square feet: "))

#Calculating acres/output
numAcres = squareFt/43560

#Printing number of acres
print("Total number of acres: ", numAcres)
print("\n")

"""
Part 3: Prints distance a car would travel in 6 hours, 10 hours, and 15 hours if it were travelling 70 mph
"""

#Prints out a car travelling 70mph would travel 70*6, 70*10, and 70*15 miles for appropriate times
print("A car travelling at 70 mph would travel:")
print(70*6, " miles in 6 hours")
print(70*10, " miles in 10 hours")
print(70*15, " miles in 15 hours")
print("\n")

"""
Part 4: Asks for users age as input, age is then used to identify wheter a person is an infant, child, teenager
or adult using if statements
"""

#Getting user age as input
userAge = int(input("Enter your age: "))

#If userAge is greater than/equal 20, adult
if(userAge >= 20):
    print("You are an adult")
#If userAge is greater than/equal 13, less than 20, teen
elif(userAge >= 13):
    print("You are a teenager")
#If userAge is greater than 1, less than 13, child
elif(userAge > 1):
    print("You are a child")
#Otherwise (less than/equal to 1), infant
else:
    print("You are an infant")
print("\n")

"""
Part 5: Asks for user to enter number of pennies, nickels, dimes, and quarters. Adds values appropriately and
determines whether or not values add up to one dollar. If values are equal to a dollar the user is prompted with
a congratulatory message, otherwise user is told if they are over or under a dollar worth of coins.
"""

#Getting total number of pennies, nickels, dimes, and quarters
numPennies = float(input("Enter number of pennies: "))
numNickels = float(input("Enter number of nickels: "))
numDimes = float(input("Enter number of dimes: "))
numQuarters = float(input("Enter number of quarters: "))

#Calculating total value of coins
totalValue = numPennies*0.01 + numNickels*0.05 + numDimes*0.1 + numQuarters*0.25

#If totalValue is equal to a dollar, congratulate, otherwise tell if over or under
if(totalValue == 1):
    print("Congratulations! You have exactly one dollar worth of coins!")
elif(totalValue < 1):
    print("The total value of your coins is less than one dollar")
else:
    print("The total value of your coins is more than one dollar")
print("\n")

"""
Part 6: Prompts user to enter a year. If it is determined that the year is a leap year, it will display that
the month of february has 29 days, otherwise it will show that february has 28 days for that year. 
"""

#Prompts user for year to determine if it is a leap year
userYear = int(input("Enter year: "))

#If the year is divisible by 100 AND 400 it is a leap year, meaning Feb has 29 days
if(userYear % 100 == 0 and userYear % 400 == 0):
    print("The year ", userYear, " is a leap year. The month of February has 29 days.")
#Otherwise it is not a leap year and Feb has 28 days
else:
    print("The year ", userYear, " is not  leap year. The month of February has 28 days.")
print("\n")

"""
Part 7: Prompts user to enter their weight in pounds and height in inches. The user's BMI is calculated and
the output is whether or not the user's BMI indicates that they are underweight, at optimal weight or overweight. 
"""

#Prompting user for height and weight
userWeight = float(input("Enter your weight in pounds: "))
userHeight = float(input("Enter your height in inches: "))

#Calculating BMI
userBMI = (userWeight*703)/(userHeight**2)

#Displaying BMI
print("Your BMI is: ", userBMI)

#If BMI is greater than 25, overweight, if between 18.5 and 25, optimal, otherwise (less than 18.5) underweight
if(userBMI > 25):
    print("BMI indicates that you are overweight")
elif(userBMI >= 18.5):
    print("BMI indicates that you are at optimal weight")
else:
    print("BMI indicates that you are underweight")
print("\n")
    
"""
Part 8: Displays amount of money Joe paid for stocks, commission paid to his broker for buying stock, amount
for which Joe sold the stock, another commission payment, and different from selling the stock and commission payment.
"""

stockPayment = float(2000*40)
firstCommission = 0.03*stockPayment;

stockSell = float(2000*42.75)
secondCommission = 0.03*stockSell

moneyLeft = stockSell - (stockPayment + firstCommission + secondCommission)

print("Joe paid $", stockPayment, " for 40 shares in Acme")
print("Joe paid his broker 3% commission which is ", firstCommission)
print("Joe sold all his shares for $", stockSell)
print("Joe paid his broker another 3% commission of $", secondCommission)
if(moneyLeft > 0):
    print("Joe made a profit of $", moneyLeft)
else:
    print("Joe lost $", moneyLeft)