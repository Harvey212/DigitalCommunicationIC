import numpy as np
import math

pdb=[0,-3,-4,-8,-15]
D=[0,10,40,80,100]
################################

pval=[]

for i in range(len(pdb)):
	s=(pdb[i]/10)
	ss=pow(10,s)
	pval.append(ss)
###############################
print("power ratio of 5 taps in linear scale")
print("tap0: {}".format(pval[0]))
print("tap1: {}".format(pval[1]))
print("tap2: {}".format(pval[2]))
print("tap3: {}".format(pval[3]))
print("tap4: {}".format(pval[4]))



#######################################
denom=0

for i in range(len(pval)):
	denom += (pval[i]) #* D[i])
###################################
pnorm=[]

for i in range(len(pval)):
	sss=pval[i]/denom
	pnorm.append(sss)
###################################
#print("Normalized PDP")
#print("tap0: {}".format(pnorm[0]))
#print("tap1: {}".format(pnorm[1]))
#print("tap2: {}".format(pnorm[2]))
#print("tap3: {}".format(pnorm[3]))
#print("tap4: {}".format(pnorm[4]))
###########################################################
MED=0

for i in range(len(D)):
	MED += D[i]*pnorm[i]

print("Mean excess delay: {}".format(MED))
#############################################
RMS1=0

for i in range(len(D)):
	RMS1 += pow(D[i] - MED,2) *pnorm[i]

RMS2=math.sqrt(RMS1)


print("RMS excess delay: {}".format(RMS2))


