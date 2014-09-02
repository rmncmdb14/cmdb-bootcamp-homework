cmdb-bootcamp-homework - Rodrigo Matus-Nicodemos - September 02, 2014
======================

CMDB Boot Camp Repository
1:
$ wc dmel-all-r5.57-removeFASTA.gff
13564834

2. 
$ grep --color -c "Sxl" dmel-all-r5.57-removeFASTA.gff
696

3. 
$ head -n5000 dmel-all-r5.57-removeFASTA.gff > dmel-all-r5.57.sm.gff
$ grep -v "^#" dmel-all-r5.57.sm.gff | cut -f3 | sort | uniq

BAC_cloned_genomic_insert
CDS
RNAi_reagent
TF_binding_site
TSS
breakpoint
chromosome_arm
chromosome_band
complex_substitution
exon
exon_junction
five_prime_UTR
gene
insulator
intron
mRNA
match
match_part
modified_RNA_base_feature
ncRNA
oligonucleotide
origin_of_replication
orthologous_region
orthologous_to
pcr_product
point_mutation
protein
region
rescue_fragment
syntenic_region
three_prime_UTR
transposable_element
transposable_element_insertion_site

4.  
$ grep -v "^#" dmel-all-r5.57.sm.gff | cut -f3 | sort | uniq -c > features.txt
1 BAC_cloned_genomic_insert
 106 CDS
  25 RNAi_reagent
  99 TF_binding_site
   2 TSS
   1 breakpoint
   1 chromosome_arm
   9 chromosome_band
   1 complex_substitution
  43 exon
  64 exon_junction
  28 five_prime_UTR
   5 gene
   5 insulator
  53 intron
  23 mRNA
1029 match
3142 match_part
   1 modified_RNA_base_feature
   1 ncRNA
  73 oligonucleotide
   3 origin_of_replication
   4 orthologous_region
 185 orthologous_to
   4 pcr_product
   1 point_mutation
  23 protein
   6 region
   4 rescue_fragment
   1 syntenic_region
  16 three_prime_UTR
   4 transposable_element
  18 transposable_element_insertion_site
