#!/bin/bash

echo -n "Please enter keyword:"
read key

sum=0
for i in `find . -type f `
do
	if ( basename $i | grep -q $key ); then
		sum=$(($sum+`ls -l $i|cut -d" " -f5`))
		#echo $i $sum
	fi
done

echo $sum

