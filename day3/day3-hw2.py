#!/usr/bin/env python

"""
Finding ORF of transcripts and translating them into amino acids
"""

import sys
from fasta import FASTAReader

#query = sys.argv[1]

reader = FASTAReader ( sys.stdin )

k = 3

index = 0

kmers = {}

#making sure sequence is split into 3mers
for _, sequence in reader:
    for i in range( 0, len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in kmers:
            kmers[kmer] = set( [index])
        else:
            kmers[kmer].add( index )
    index = index + 1 # or index += 1


for key in kmers:
    if key == "ATG":
        print "Found Start Codon"
    if key == "TAG":
        print "Found a Stop Codon"
    if key == "TGA":
        print "Found a Stop Codon"
    if key == "TAA":
        print "Found a Stop Codon"
    print key, kmers[kmer]

startCodon = 'ATG'

#Finding start codon in sequence
matched_sequences_start = []
for i in range( 0, len(sequence) - k):
    kmer = startCodon
    if kmer in kmers:
        #print kmer
        matched_sequences_start.append( kmers[kmer] )
        
print "start codon is here ", sorted( matched_sequences_start )

stopCodonTAG = 'TAG'
stopCodonTGA = 'TGA'
stopCodonTAA = 'TAA'       

#Finding stop codon in sequence but very redundant because 3 if statements for each stop codon
matched_sequences_stop = []
for i in range( 0, len(sequence) - k):
    kmerTAG = stopCodonTAG
    kmerTGA = stopCodonTGA
    kmerTAA = stopCodonTAA
    if kmerTAG in kmers:
        #print kmer
        matched_sequences_stop.append( kmers[kmer] )
    if kmerTGA in kmers:
        #print kmer
        matched_sequences_stop.append( kmers[kmer] )
    if kmerTAA in kmers:
        #print kmer
        matched_sequences_stop.append( kmers[kmer] )
    
print "stop codon is here ", sorted( matched_sequences_stop )

# find the greatest length between first start codon in matched_sequence_start and matched_sequence_stop using set indices to find ORF

if matched_sequences_start[0] >= matched_sequences_stop[0]:
    print "true"
    print sequence