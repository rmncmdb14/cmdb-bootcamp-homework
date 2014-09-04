#!/usr/bin/env python

align_count = "/Users/cmdb/data/day2/accepted_hits.sam"

file = open(align_count)
total = 0

for line in file:
	if "NM:i:0" in line:
		total = total + 1
	
print total