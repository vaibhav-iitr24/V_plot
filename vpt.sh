#!/bin/bash


awk '{value=($3+$4)/2;avg=($9+$10)/2; print int(avg)-int(value), $12}' mapped.bed | tr ' ' '\t' | sort -n -k1,1 > op.tsv
uniq -c op.tsv | awk '{print $2,$3,$1}' | tr ' ' '\t' > file.tsv
cat file.tsv | python3 plot1.py
