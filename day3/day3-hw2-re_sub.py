#!/usr/bin/env python

# script to find the start codon 'ATG' and translate the transcipts from the first_hundred.fa file 

import sys

file = open("first_hundred.fa")

table = {"TTT ": "F ", "TTC ": "F ", "TTA ": "L ", "TTG ": "L ", "TCT ": "S ", "TCC ": "S ", "TCA ": "S ", "TCG ": "S ", "TAT ": "Y ", "TAC ": "Y ", "TAA ": "STOP ", "TAG ": "STOP ", "TGT ": "C ", "TGC ": "C ", "TGA ": "STOP ", "TGG ": "W ", "CTT ": "L ", "CTC ": "L ", "CTA ": "L ", "CTG ": "L ", "CCT ": "P ", "CCC ": "P ", "CCA ": "P ", "CCG ": "P ", "CAT ": "H ", "CAC ": "H ", "CAA ": "Q ", "CAG ": "Q ", "CGT ": "R ", "CGC ": "R ", "CGA ": "R ", "CGG ": "R ", "ATT ": "I ", "ATC ": "I ", "ATA ": "I ", "ATG ": "M ", "ACT ": "T ", "ACC ": "T ", "ACA ": "T ", "ACG ": "T ", "AAT ": "N ", "AAC ": "N ", "AAA ": "K ", "AAG ": "K ", "AGT ": "S ", "AGC ": "S ", "AGA ": "R ", "AGG ": "R ", "GTT ": "V ", "GTC ": "V ", "GTA ": "V ", "GTG ": "V ", "GCT ": "A ", "GCC ": "A ", "GCA ": "A ", "GCG ": "A ", "GAT ": "D ", "GAC ": "D ", "GAA ": "E ", "GAG ": "E ", "GGT ": "G ", "GGC ": "G ", "GGA ": "G ", "GGG ": "G "}

new_table = {}

for key, value in table.iteritems():
	new_table[ key.strip() ] = value.strip()

start = ""

result = ""

protein = []

while True:
    line = file.readline()
    if line.startswith( ">" ):
        print "Protein sequence is " + result
        result = ""
        continue
        
    if line == "":
        print "Protein sequence is " + result
        break
        
    else:
        print line,
        start = line.find("ATG")
        print "ATG is at nucleotide # " + str(start),
        for i in range( start, len(line), 3):
    
            codon = new_table[line[i:i+3]]
            
            if codon == "STOP":
                break
                
            result += codon
            
#print start

#print protein

#print result + "[STOP]"
        