#!/bin/bash

#Problem 2 - using variables to print name, and four different course names

#Setting Variables
name="Jesus Banales"
courseOne="Intro to Scripting"
courseTwo="Into to Database Systems"
courseThree="Cybersecurity"
courseFour="Applied Probability and Statistics"

#Printing Variables
echo "$name $courseOne , $courseTwo , $courseThree , $courseFour "


#Problem 3 - printing name and courses by printing all arguments (pass name and course names as arguments)
echo "$*"


#Problem 4 - Print current process number of the shell and all arguments passed

#Printing current process number of shell
echo "Current process number of shell: $$"

#Printing all arguments
echo "$*"


#Problem 5 - Find random number (grade), find letter grade using if, else if, else 

#Get random number by using process number of the shell
rand=$$
realRand=$(($rand%100))
echo Random number is $realRand

#If rand number is between 100-90 then its A, if its between 89 and 80 then B, etc.
if [[ $realRand -le 100 && $realRand -ge 90 ]]
then
	echo "Grade is A"
elif [[ $realRand -le 89 && $realRand -ge 80 ]]
then
	echo "Grade is B"
elif [[ $realRand -le 79 && $realRand -ge 70 ]]
then
	echo "Grade is C"
elif [[ $realRand -le 69 && $realRand -ge 60 ]]
then
	echo "Grade is D"
else
	echo "Failing Grade"
fi

#Problem 6 - Performing addition, subtraction, multiplication and division for some numbers, also
#incrementing and decrementing for all numbers

varOne=7
varTwo=9
varThree=11
varFour=14

echo "$varOne, $varTwo, $varThree, $varFour"

echo "Variable two - variable one = $((varTwo-varOne))"
echo "Variable two + variable three = $((varTwo+varThree))"
echo "Variable three * variable four = $((varThree*varFour))"
echo "Variable four / variable one = $((varFour/varOne))"
echo "Incrementing varOne: $((++varOne))"
echo "Decrementing varThree: $((--varThree))"