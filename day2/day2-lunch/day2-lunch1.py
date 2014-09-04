#!/usr/bin/env python

align_count = "/Users/cmdb/data/day2/accepted_hits.sam"

file = open(align_count)
total = 0

while True:
    line = file.readline()
    if line == "":
        break
    else:
        total = total + 1

print total



    


