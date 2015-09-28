# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:34:16 2015

@author: francescoperera
"""
table=[]

supersid=[]
cancerdx=[]
sex=[]
racev1x=[]
faminc12=[]



CMWFI=[] # cancer,male,white,family income
CMBFI=[] # cancer,male,black,family income
CMAAFI=[] # cancer,male,american indian, family income
CMAFI=[] # cancer,male,asian,family income
CMPIFI=[] # cancer,male,pacific islander/hawaiin,family income
CMMFI=[] # cancer,male,mixed, family income

CFWFI=[] # cancer,female,white,family income
CFBFI=[] # cancer,female,black,family income
CFAAFI=[] # cancer,female,american indian, family income
CFAFI=[] # cancer,female,asian,family income
CFPIFI=[] # cancer,female,pacific islander/hawaiin,family income
CFMFI=[] # cancer,female,mixed, family income


MWFI=[] #male,white,family income
MBFI=[] #male,black,family income
MAAFI=[] #male,american indian, family income
MAFI=[] #male,asian,family income
MPIFI=[] #male,pacific islander/hawaiin,family income
MMFI=[] #male,mixed, family income

FWFI=[] #male,white,family income
FBFI=[] #male,black,family income
FAAFI=[] #male,american indian, family income
FAFI=[] #male,asian,family income
FPIFI=[] #male,pacific islander/hawaiin,family income
FMFI=[] #male,mixed, family income


firstRow = 0
for line in open('/Users/francescoperera/Documents/Health Tech/2012Datastripped.csv'):
    if firstRow == 0:
        firstRow = 1
        continue
    
    row=[]
    count=0
    for number in line.split(','):
        row.append(float(number))
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
            
        count+=1
    table.append(row)

index_array=[]   
for index in range(len(supersid)):
    index_array.append(index) # for debugging purposes
    #for supersid(index):
     
    if cancerdx[index]==1:
        if sex[index]==1:
            if racev1x[index]==1:
                print 'hello'
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


print CMWFI
print
print CMBFI
print
print CMAAFI
print
print CMAFI



#print index_array                    
                    
                
            
    











#print  table




