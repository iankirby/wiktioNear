#!/bin/bash

for j in *Cleaned.txt
do
cp "$j" ./asCSV/"${j%.txt}.csv"
done

for k in *Cleaned.txt
do
mv "$k" ./Cleaned-txt-Files/"${k%.txt}.txt"
done

for i in *.txt
do 
mv "$i" ./Pre-cleaned/"${i%.txt}.txt"
done

# for f in *.txt; do
# mv "$f" ./asCSV/"${f%.txt}.csv"
#  done