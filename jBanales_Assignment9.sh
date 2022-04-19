#!/bin/bash
clear

#Question 1 - Creates a random array of numbers with size 20, using $RANDOM. Bubble sort is implemented
#using a for loop to sort the array in ascending order and it is then printed.

for (( i=0; i<20; i++ ))
do
	rand=$RANDOM
	firstArr[i]=$(($rand%100))
done
echo "Unsorted list: ${firstArr[*]}"


for (( i = 0; i<${#firstArr[@]}; i++ ))
do
    for(( j = 0; j<${#firstArr[@]}-$i-1; j++ ))
    do
    
        if [ ${firstArr[$j]} -gt ${firstArr[$((j+1))]} ]
        then
            temp=${firstArr[$j]}
            firstArr[$j]=${firstArr[$((j+1))]}  
            firstArr[$((j+1))]=$temp
        fi
    done
done

echo "List in ascending order: ${firstArr[@]}"

#Question 2 - Creates a random array of numbers with size 20, using $RANDOM. Bubble sort is implemented
#using a for loop to sort the array in descending order and it is then printed.

for (( i=0; i<20; i++ ))
do
	rand=$RANDOM
	secArr[i]=$(($rand%100))
done
echo "Unsorted list: ${secArr[*]}"


for (( i = 0; i<${#secArr[@]}; i++ ))
do
    for(( j = 0; j<${#secArr[@]}-$i-1; j++ ))
    do
    
        if [ ${secArr[$j]} -lt ${secArr[$((j+1))]} ]
        then
            temp=${secArr[$j]}
            secArr[$j]=${secArr[$((j+1))]}  
            secArr[$((j+1))]=$temp
        fi
    done
done

echo "List in descending order: ${secArr[@]}"

#Question 3 - Array of numbers 1-50 created using for loop

for (( i=1; i<=50; i++ ))
do
	funcArray[$i-1]=$i
done

echo "Array of 1-50: ${funcArray[@]}"

#Question 4 - Creating a function that finds all prime numbers from 1-50 and stores it in an array
#Function then finds summation of all prime numbers and displays them.

getPrime()
{	
	sum=0
	echo "Prime numbers 1-50: "
	for (( i=2; i<=50; i++))
	do
		flag=0
		for(( j=2; j<i; j++))
		do
			rem=$((i%j))
			if [ $rem -eq 0 ]
			then
				flag=1
				break
			fi
		done
		if [ $flag -eq 0 ]
		then
			echo $i
			let sum+=$i
		fi
	done
	echo "Summation of all prime numbers 1-50 is: $sum"
}

getPrime

#Question 5 - Uses for loop to iterate from 1-50, even numbers are added to an array and odd numbers
#are placed in a different array. The even and odd numbers are summed together when added to their
#respective arrays. The arrays are displayed along with their summations.

evenIn=0
evenSum=0
oddIn=0
oddSum=0
for(( i = 1; i<=50; i++ ))
do
	if [ $((i%2)) -eq 0 ]
	then
		evenArr[evenIn]=$i
		let evenIn++ evenSum+=i
	else
		oddArr[oddIn]=$i
		let oddIn++ oddSum+=i
	fi
done

echo "Even numbers in 1-50: ${evenArr[@]}"
echo "Even summation: $evenSum"
echo "Even numbers in 1-50: ${oddArr[@]}"
echo "Even summation: $oddSum"