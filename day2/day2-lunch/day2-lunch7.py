#!/usr/bin/env python

align_count = "/Users/cmdb/data/day2/accepted_hits.sam"

file = open(align_count)
POS = 0
for i, line in enumerate(file):
	fields = line.rstrip("\r\n").split("\t")
        if i > 0 and 10000 <= float(fields[3]) <= 20000:
            POS = POS + 1
print POS
			