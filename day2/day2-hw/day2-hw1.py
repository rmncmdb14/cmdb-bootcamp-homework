#!/usr/bin/env python

import pandas as pd

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"

cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

df = pd.read_table( cufflinks_output)

df2 = pd.read_table( cufflinks_output2)

#male_female = pd.DataFrame( {"male": df["FPKM"], "female": df2["FPKM"] } )

sortM =  df.sort("FPKM", ascending=True)
sortF = df2.sort("FPKM", ascending=True)
print sortM

#Bottom =  sortM*(0.333)
#Middle =  sortM*(0.666)
#Top =  sortM
#print Bottom, Middle, Top

bottom_male = sortM[0:5196]["FPKM"]
middle_male = sortM[5196:10390]["FPKM"]
top_male = sortM[10391:15603]["FPKM"]

bottom_female = sortF[0:5196]["FPKM"]
middle_female = sortF[5196:10390]["FPKM"]
top_female = sortF[10391:15603]["FPKM"]

my_list = [bottom_male, middle_male, top_male, bottom_female, middle_female, top_female]

import matplotlib.pyplot as plt

plt.figure()
plt.ylim(-10, 100)
#male_female.boxplot()
plt.boxplot(my_list)

plt.savefig("boxplot.png")