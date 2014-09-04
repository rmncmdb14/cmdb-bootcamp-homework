#!/usr/bin/env python

align_count = "/Users/cmdb/data/day2/accepted_hits.sam"

file = open(align_count)
MAPQ = 0
for i, line in enumerate(file):
	fields = line.rstrip("\r\n").split("\t")
        if i > 0:
            MAPQ = MAPQ + float(fields[4])

Avg_MAPQ = MAPQ / i
        
print "MAPQ Score is %d and Average MAPQ is %d " % (MAPQ, i)