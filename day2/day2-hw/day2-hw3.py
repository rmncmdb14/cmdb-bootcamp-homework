#!/usr/bin/env python

import pandas as pd

import matplotlib.pyplot as plt

plt.figure()

CODIR_PRE="/Users/cmdb/data/results/SRR072"
CODIR_SUF="_clout/genes.fpkm_tracking"
n = 0
my_list = []
for n in range (905, 916):
    #print n
    file = CODIR_PRE + str(n) + CODIR_SUF
    #print file
    if n == 910:
        #print "value 910"
        continue
    elif n == 912:
        #print "value 912"
        continue
    elif n == 914:
        #print "value 914"
        continue
    else:
        #print file
        meta_data_True = pd.read_table(CODIR_PRE + str(n) + CODIR_SUF)
        #print "Good loop"
        
        columns_of_interest = ["FPKM", "gene_short_name"]
        my_sort = meta_data_True.sort("gene_short_name")
        #print my_sort
        COI = my_sort[columns_of_interest][11898:11899]
        FPKM = ["FPKM"]
        #print my_sort[columns_of_interest][11898:11899]
        Sxl_GeX = COI[FPKM]
        DF = pd.DataFrame(my_list.append(Sxl_GeX))
        #my_list["Sxl_Gex"].plot()
    n = n + 1
print DF
plt.figure()
DF.plot()
plt.savefig("My_list.png")