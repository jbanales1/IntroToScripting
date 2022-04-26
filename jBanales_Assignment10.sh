#!/bin/bash
clear

#Part 1 - Gets numbers from a text file and adds them to array, recursive method used to find summation

<<'com'
getSum()
{
	if [ $# == 1 ]
	then
		echo 1
	else
		for (( i=2; i<$#; i++ ))
		do
			echo $$i	
			tempArr[i-2]=$$i
		done
		result=$(getSum ${tempArr[@]})
		echo $(( result+=$1 ))
	fi
}

filename="nums.txt"

count=0
while read line
do
	firstArr[count]=$line
	let count++
done < $filename

echo ${firstArr[@]}

printing="$(getSum ${firstArr[@]})"
echo $printing

com

#Part 2 - Taking input from user and using recursive function to find Fib sequence

findFib()
{
	if [ $1 <= 1 ]
	then
		echo $1
	else
		resultOne=$(findFib $(( $1 - 1 ))) 
		resultTwo=$(findFib $(( $1 - 2 )))
		echo $(( resultOne + resultTwo ))
	fi
}

read - [ "Enter number to find fibonacci sequence" fibNum
findFib fibNum
