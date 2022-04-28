#!/bin/bash
clear

#Part 1 - Gets numbers from a text file and adds them to array, recursive method used to find summation

filename="nums.txt"
count=0
while read line
do
	a[count]=$line
	let count++
done < $filename

echo ${a[@]}

sum=0

getSum()
{
	index=$1
	
	if [ ${#a[@]} -lt 1 ]
	then
		return 0
	else
		let sum+=${a[index]}
		unset a[$index]
		let index--
		getSum $index	
	fi
}

let startingIndex=(${#a[@]}-1)
getSum startingIndex

echo "Sum of numbers: $sum"



#Part 2 - Taking input from user and using recursive function to find Fib sequence

getFib()
{
	fib=$1
	if [ $fib -le 1 ]
	then
		echo $fib
	else
		echo "$(( $(getFib $(($fib-2)))+$(getFib $(($fib-1))) ))"
	fi
}

read -p "Enter number to get fib sequence: " userIn

for (( i=0; i<=$userIn; i++ ))
do
	fibArr[i]=$(getFib $i)
done

echo "Fibonacci sequence: ${fibArr[@]}"



#Part 3 - Outputting elements from parts 1 and 2 to a file named output.txt

outFile=output.txt

echo $sum >> $outFile

for (( i=0; i<${#fibArr[@]}; i++ ))
do
	echo ${fibArr[i]} >> $outFile
done



#Part 4 - Creating a random array then sorting using a recursive function, array is printed before and after sorting

for (( i=0; i<10; i++))
do
	rand=$RANDOM
	sortArr[i]=$(($rand%100))
done
echo "Unsorted list: ${sortArr[@]}"

recSort()
{
	currIndex=$1
	if [ $currIndex == ${#sortArr[@]} ]
	then
		return 0
	else
		for (( i=$currIndex; i<${#sortArr[@]}; i++ ))
		do
			if [ ${sortArr[currIndex]} -gt ${sortArr[i]} ]
			then
				temp=${sortArr[currIndex]}
				sortArr[currIndex]=${sortArr[i]}
				sortArr[i]=$temp
			fi
		done
		let currIndex++
		recSort $currIndex
	fi
}

recSort 0
echo "Sorted list: ${sortArr[@]}"
