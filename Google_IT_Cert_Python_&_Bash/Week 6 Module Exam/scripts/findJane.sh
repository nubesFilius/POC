#!/bin/bash

> oldFiles.txt

files=$(grep -s "jane " ../data/list.txt | cut -d " " -f 3)

for i in $files; do

    [ -e ../$i ] && echo $i >> oldFiles.txt;

done



