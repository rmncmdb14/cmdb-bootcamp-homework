#!/usr/bin/env python

# "transcripts.fa"" contains all the transcipts from using BedTools
# The Bed Tools command used was $ bedtools getfasta -fi dmel-all-chromosome-r5.57.fasta -bed transcripts.gtf -s -fo all_transcripts.fasta
# the -s option allows to get the reverse complement of the transcript if it 

file = open("transcripts.fa")

line = file.readline()
assert line.startswith( ">" )
my_id = line[1:].rstrip("\r\n")

sequences = []

while True:
    line = file.readline()
    if line.startswith( "G" or "A" or "T" or "C" ):
        sequences.append( line.strip() )
        #print line,
    if line == "":
        break
        
sequence = sorted(sequences, key = len, reverse = True)

#List = [1, 3, 30, 5, 9, 7, 10, 20, 15, 4, 25, 2, 40]

#List_sort = sorted(List)

#print type(List_sort)
#print List_sort
#print type(sequence)
#print sequence


first_hundred = sequence[0:100]

count = 0
extracted_seq_file = open("first_hundred.fa", "w")
for i,j in enumerate(first_hundred):
    #print i, j
    count = count + 1
    Seq = "> " + str(count) + ")" + " " + j + " "
    print Seq
    extracted_seq_file.write(Seq)
extracted_seq_file.close()

print count
