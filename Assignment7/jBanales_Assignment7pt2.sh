#!/bin/bash

gross=$1
hra=0
da=0
#bash hates non whole numbers, this program is a failure
if [ $1 -le 10000 ]
then
	hra=$((gross/5))
	echo $hra
	da=$((gross/(5/4)))
	echo $da
elif [ $1 -le 20000 && $1 -ge 10001]
then
	hra=$((gross/4))
	echo $hra
	da=$((gross*(9/10)))
	echo $da
else
	hra=$((gross/3))
	echo $hra
	da=$((gross*(95/100)))
	echo $da
fi

gross=$((gross+hra))
gross=$((gross+da))
echo "Gross salary is: $gross"