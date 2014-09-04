#!/usr/bin/env python

align_count = "/Users/cmdb/data/day2/accepted_hits.sam"

file = open(align_count)

TwoL = 0
TwoR = 0
ThreeL = 0
ThreeR = 0
Four  = 0
X  = 0

for line in file:
    fields = line.split()
    if line == "":
        break
    if fields[2] == "2L":
        TwoL = TwoL + 1
    if fields[2] == "2R":
        TwoR = TwoR + 1
	if fields[2] == "3L":
		ThreeL = ThreeL + 1
	if fields[2] == "3R":
		ThreeR = ThreeR + 1
	if fields[2] == "4":
		Four = Four + 1
    if fields[2] == "X":
        X = X + 1
        
print "2L has %d alignments, 2R has %d alignments, 3L has %d alignments, 3R has %d alignments, 4 has %d alignments, X has %d alignments" % (TwoL, TwoR, ThreeL, ThreeR, Four, X)