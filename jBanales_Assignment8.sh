#!/bin/bash
<<com
#Questions 1 - Prints 1-15 in three different ways, using while, until and for loop

i=1
while [ $i -le 15 ]
do
	echo $i
	let i++
done


i=1
until [ $i -gt 15 ]
do
	echo $i
	let i++
done


for (( i=1; i<=15; i++ ))
do
	echo $i
done

#Question 2 - Finds summation of numbers 20-40 inclusive, using while, until and for loop

sum=0
init=20

while [ $init -le 40 ]
do
	let sum+=init init++
done

echo Sum for while loop is: $sum


sum=0
init=20

until [ $init -gt 40 ]
do
	let sum+=init init++
done

echo Sum for until loop is: $sum


sum=0

for (( i=20; i<=40; i++ ))
do
	let sum+=i
done
echo Sum for for loop is: $sum

#Question 3 - Prints all prime numbers less than 50 using while, until and for loop

i=2
while [ $i -le 50 ]
do
	flag=0
	j=2
	while [ $j -lt $i ]
	do
		rem=$((i%j))
		if [ $rem -eq 0 ]
		then
			flag=1
			break
		fi
		let j++
	done
	if [ $flag -eq 0 ]
	then
		echo $i
	fi
	let i++
done


i=2
until [ $i -gt 50 ]
do
	flag=0
	j=2
	until [ $j -ge $i ]
	do
		rem=$((i%j))
		if [ $rem -eq 0 ]
		then
			flag=1
			break
		fi
		let j++
	done
	if [ $flag -eq 0 ]
	then
		echo $i
	fi
	let i++
done


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
	fi
done
com
#Question 4 - 

select CITY in Corpus Kingsville Commerce Exit
do
	case $CITY in
		Corpus)
			echo "Texas A&M University Corpus Christi";;
		Kingsville)
			echo "Texas A&M University Kingsville";;
		Commerce)
			echo "Texas A&M University Commerce";;
		Exit)
			break;;
		*)
			echo "Texas A&M University";;
	esac
done

#Bonus - Fixing code

var_test=30

if [[ $var_test=>1 && $var_test<=10 ]]
then
	echo Between 1 to 10
elif [[ $var_test=>11 && $var_test<=20 ]]
then
	echo Between 11 to 20
elif [[ $var_test>20 ]] #Added a set of brackets :|
then
	echo Greater than 20
else
	echo Less than 1
fi
