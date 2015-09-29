# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:34:16 2015

@author: francescoperera & zaidhaque
"""

import numpy as np
import matplotlib.pyplot as plt

from numpy import mean
#table=[]

supersid=[]
cancerdx=[]
sex=[]
racev1x=[]
faminc12=[]
age = []
exp = []



CMWFI  = [] # cancer,male,white,family income
CMBFI  = [] # cancer,male,black,family income
CMAAFI = [] # cancer,male,american indian, family income
CMAFI  = [] # cancer,male,asian,family income
CMPIFI = [] # cancer,male,pacific islander/hawaiin,family income
CMMFI  = [] # cancer,male,mixed, family income

CFWFI  = [] # cancer,female,white,family income
CFBFI  = [] # cancer,female,black,family income
CFAAFI = [] # cancer,female,american indian, family income
CFAFI  = [] # cancer,female,asian,family income
CFPIFI = [] # cancer,female,pacific islander/hawaiin,family income
CFMFI  = [] # cancer,female,mixed, family income


MWFI  = [] #male,white,family income
MBFI  = [] #male,black,family income
MAAFI = [] #male,american indian, family income
MAFI  = [] #male,asian,family income
MPIFI = [] #male,pacific islander/hawaiin,family income
MMFI  = [] #male,mixed, family income

FWFI  = [] #male,white,family income
FBFI  = [] #male,black,family income
FAAFI = [] #male,american indian, family income
FAFI  = [] #male,asian,family income
FPIFI = [] #male,pacific islander/hawaiin,family income
FMFI  = [] #male,mixed, family income


firstRow = 0
for line in open('/Users/zaidhaque/Documents/Cornell Tech/Semester 1/CS 5555 Health Tech/Lab 2/MEPSDataAnalysis/2012Datastripped.csv'):
    if firstRow == 0:
        firstRow = 1
        continue
    
    row=[]
    count=0
    for element in line.split(','):
        
        number=float(element)
        
        if count==0:
            supersid.append(number)
        elif count==3:
            sex.append(number)
        elif count==5:
            racev1x.append(number)
        elif count==22:
            cancerdx.append(number)
        elif count==72:
            faminc12.append(number)
        elif count==2:
            age.append(number)
        elif count==78:
            exp.append(number)
            
        count+=1
    #table.append(row)

#index_array=[]



for index in range(len(supersid)):
    #index_array.append(index) # for debugging purposes
    #for supersid(index):
     
    if cancerdx[index]==1:
        if sex[index]==1:
            if racev1x[index]==1:
                CMWFI.append(faminc12[index])
            elif racev1x[index]==2:
                CMBFI.append(faminc12[index])
            elif racev1x[index]==3:
                CMAAFI.append(faminc12[index])
            elif racev1x[index]==4:
                CMAFI.append(faminc12[index])
            elif racev1x[index]==5:
                CMPIFI.append(faminc12[index])
            elif racev1x[index]==6:
                CMMFI.append(faminc12[index])
        else: # else sex(index)==2 female
            if racev1x[index]==1:
                CFWFI.append(faminc12[index])
            elif racev1x[index]==2:
                CFBFI.append(faminc12[index])
            elif racev1x[index]==3:
                CFAAFI.append(faminc12[index])
            elif racev1x[index]==4:
                CFAFI.append(faminc12[index])
            elif racev1x[index]==5:
                CFPIFI.append(faminc12[index])
            elif racev1x[index]==6:
                CFMFI.append(faminc12[index])
                    
    else: # else cancerdx ==2 ( no cancer)
        if sex[index]==1: # if sex=male
            if racev1x[index]==1:
                MWFI.append(faminc12[index])
            elif racev1x[index]==2:
                MBFI.append(faminc12[index])
            elif racev1x[index]==3:
                MAAFI.append(faminc12[index])
            elif racev1x[index]==4:
                MAFI.append(faminc12[index])
            elif racev1x[index]==5:
                MPIFI.append(faminc12[index])
            elif racev1x[index]==6:
                MMFI.append(faminc12[index])
        else: # else sex(index)==2=female
            if racev1x[index]==1:
                FWFI.append(faminc12[index])
            elif racev1x[index]==2:
                FBFI.append(faminc12[index])
            elif racev1x[index]==3:
                FAAFI.append(faminc12[index])
            elif racev1x[index]==4:
                FAFI.append(faminc12[index])
            elif racev1x[index]==5:
                FPIFI.append(faminc12[index])
            elif racev1x[index]==6:
                FMFI.append(faminc12[index])
                
# these ifs  adda a 0 to the empty lists, if there are any                

    

print CMPIFI
print
print CFAFI
print
print CFPIFI
print
print CFMFI

CMWFI_ave  = mean(CMWFI)
CMBFI_ave  = mean(CMBFI)
CMAAFI_ave = mean(CMAAFI) 
CMAFI_ave  = mean(CMAFI)
CMPIFI_ave = mean(CMPIFI)
CMMFI_ave  = mean(CMMFI)

CFWFI_ave  = mean(CFWFI)
CFBFI_ave  = mean(CFBFI)
CFAAFI_ave = mean(CFAAFI)
CFAFI_ave  = mean(CFAFI)
CFPIFI_ave = mean(CFPIFI)
CFMFI_ave  = mean(CFMFI)

MWFI_ave  = mean(MWFI)
MBFI_ave  = mean(MBFI)
MAAFI_ave = mean(MAAFI)
MAFI_ave  = mean(MAFI)
MPIFI_ave = mean(MPIFI)
MMFI_ave  = mean(MMFI)

FWFI_ave  = mean(FWFI)
FBFI_ave  = mean(FBFI)
FAAFI_ave = mean(FAAFI)
FAFI_ave  = mean(FAFI)
FPIFI_ave = mean(FPIFI)
FMFI_ave  = mean(FMFI)

print CMBFI_ave
print CMAAFI_ave
print CMAFI_ave
print CMPIFI_ave
print CMMFI_ave
print

def add(x1,x2,x3,x4,x5,x6):
    """ helper function that takes 6 inputs and returns their sum """
    return x1+x2+x3+x4+x5+x6

all_CM_FI = []
all_M_FI  = []

for i in range(len(supersid)):
    if sex[i] == 1:
        if cancerdx[i] == 1:
            all_CM_FI.append(faminc12[i])
        elif cancerdx[i] == 2:
            all_M_FI.append(faminc12[i])

all_CF_FI = []
all_F_FI  = []  
                      
for i in range(len(supersid)):
    if sex[i] == 2:
        if cancerdx[i] == 1:
            all_CF_FI.append(faminc12[i])
        elif cancerdx[i] == 2:
            all_F_FI.append(faminc12[i])



#all_CM_ave=add(CMWFI_ave,CMBFI_ave,CMAAFI_ave,CMAFI_ave,CMPIFI_ave,CMMFI_ave)
#all_M_ave=add(MWFI_ave,MBFI_ave,MAAFI_ave,MAFI_ave,CMPIFI_ave,MMFI_ave)

print ("Cancer Male Avg Income")
print mean(all_CM_FI)
print
print ("Non-cancer Male Avg Income")
print mean(all_M_FI)
print

print ("Cancer Female Avg Income")
print mean(all_CF_FI)
print
print ("Non-cancer Female Avg Income")
print mean(all_F_FI)

np.histogram(all_CM_FI, bins=10, range=None, normed=False, weights=None, density=None)

#print age
#print exp
print ("Age vs. Expenditure")
plt.scatter(age,exp, s=10, c=u'b', marker=u'o', cmap=None, norm=None, vmin=None, vmax=None, alpha=.1, linewidths=None, verts=None, hold=None)
"""
Graph shows expenditure over a lifetime. Note that there is high expenditure at birth,
but apart from that median expenditure peaks at 60 yrs. 
"""

expenditureByAge = []

for i in range(86):
    expForAge = []    
    for j in range(len(supersid)):        
        if int(age[j]) == i:
            expForAge.append(int(exp[j]))
    print i
    print len(expForAge)
    print
    expenditureByAge.append(expForAge)

print ("exp sorted by age.")        



print 
#print index_array   



                    
                
            
    











#print  table




