#!/usr/bin/env python

align_count = "/Users/cmdb/data/day2/accepted_hits.sam"

file = open(align_count)

for line in file:
	fields = line.split()
	
	print fields[2]

