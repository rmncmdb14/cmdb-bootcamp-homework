#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""

import sys

from fasta import FASTAReader
        
reader = FASTAReader( sys.stdin )      
 
seq_list = [] 

for sid, sequence in reader:
    seq_list.append(sequence)
    #print seq_list
    
seq_sort = sorted(seq_list, key = len, reverse = True)

first_hundred = seq_sort[0:101]

#print first_hundred to file
extracted_seq_file = open("first_hundred.gtf", "w")
for i,j in enumerate(first_hundred):
    print i, j
    Seq = "> " + j + " "
    extracted_seq_file.write(Seq)
extracted_seq_file.close()

