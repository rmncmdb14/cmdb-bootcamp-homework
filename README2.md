#!/bin/bash

#
# Day 1 - Homework: - debug this bash script - Rodrigo Matus-Nicodemos - 20140902
#

echo "There are around 6 mistakes"

# Unique file names to be iterated
ONE="893"
TWO="903"
THR="905"
FOR="915"

# Directories where raw data is located and to be exported to
FASTQ_DIR=/Users/cmdb/data/fastq/
OUTPUT_DIR=/Users/cmdb/data/day1/
TOPHAT_DIR_OUT=/Users/cmdb/data/day1/tophat_out/
SAMPLE_PREFIX="SRR072"

# Directory where Genome annotation is located and annotation file
GENOME_DIR=/Users/cmdb/day1-lunch/genomes/
ANNOTATION=dmel-all-r5.57.gff
GENOME_OUT=dmel-all-chromosome-r5.57

CORES=4

for i in $ONE $TWO $THR $FOR
do
  	# Fastq for determine quality check on raw data. Data appears to be from NCBI SRA SRP004442 dataset. Don't know how to get this dataset. There appears to be a file similar in our directory called SRP004442_clout.tgz?
  	echo fastqc $FASTQ_DIR$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  	# input genome annotation for TopHat, with the output directory. Nature protocol paper has a file that ends in .gft instead of .gff? The output files should have .bam files after running TopHat.
  	echo tophat -p 4 -G $GENOME_DIR$ANNOTATION -o $TOPHAT_DIR_OUT --no-novel-juncs --segment-length 20 /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57 $SAMPLE_PREFIX$i\.fastq
  	# Cufflinks requires accepted_hit.bam file from TopHat to assemble each transcript. Then it requires a file with .gtf to assemble to the assemblies.txt file. Cuffmerge seems merge all the assemblies into one file. 
 	echo cufflinks -p 4 -G $GENOME_DIR$ANNOTATION -o day1-results/accepted_hits.bam | cufflinks day1-results/transcripts.gtf | cuffmerge -g genes.gft -s genome.fa -p 8 assemblies.txt
done