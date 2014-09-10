#!/usr/bin/env python

import pandas as pd
import sys


SAMPLE_FILE = "/Users/cmdb/data/day2/samples.csv"
CSV_DATA = pd.read_csv(SAMPLE_FILE)
#print CSV_DATA

CODIR_PRE="/Users/cmdb/data/results/"
CODIR_SUF="_clout/genes.fpkm_tracking"


for i in CSV_DATA[ CSV_DATA["sex"] == "female" ]["sample"]:
    current_df = pd.read_table ( CODIR_PRE + i + CODIR_SUF)
    print "Sxl abundance (FPKM) for " + i
    print current_df[ current_df["gene_short_name"] == "Sxl" ]["FPKM"]

import matplotlib.pyplot as plt

SXL= []

for x in CSV_DATA[ CSV_DATA["sex"] == "female" ]["sample"]:
    current_df = pd.read_table ( CODIR_PRE + i + CODIR_SUF)
    SXL.append( current_df[ current_df["gene_short_name"] == "Sxl" ]["FPKM"] )

plt.figure()
plt.plot(SXL);
plt.savefig( "Sxl-female-abundance.png" )
