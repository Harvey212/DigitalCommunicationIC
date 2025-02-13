import math

import matplotlib.pyplot as plt
import numpy as np

################################################################################
#common information
################################################################################
T=500 #ns
#fsub = 2*pow(10,6) #Hz   #subcarrier spacing
fsub = 2*pow(10,-3) #1/ns
scale= 1/8
#fs = 32*pow(10,6) #Hz #sampling rate

Ts =31.25 #ns

data=[0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
k=[0,1,2,3,4,5,6,7]
#black constellation
bphi1=math.pi*(1/4)
bphi2=math.pi*(3/4)
bphi3=math.pi*(5/4)
bphi4=math.pi*(7/4)
########################################
phi=0
rpt=0
ipt=0
#ptt=0
###################################################################################






##################################################################
#IFFT
#################################################################
totaln=int(T/Ts)+1
##########################
R=[]
I=[]
##########3
for kk in k:
	fk = kk * fsub
	rpts=[]
	ipts=[]

	signal=[]
	signal.append(data[2*kk])
	signal.append(data[2*kk+1])
	################################
	#black constellation
	if signal == [0,0]:
		phi =bphi4
	elif signal == [0,1]:
		phi =bphi1
	elif signal == [1,0]:
		phi =bphi3
	elif signal == [1,1]:
		phi =bphi2
	else:
		phi =0
	#################################
	
	for n in range(totaln):
		rpt=math.cos(2*math.pi *fk*n*Ts)*math.cos(phi)-math.sin(2*math.pi *fk*n*Ts)*math.sin(phi)
		ipt = math.cos(2*math.pi *fk*n*Ts)*math.sin(phi)+math.sin(2*math.pi *fk*n*Ts)*math.cos(phi)

		rpts.append(rpt*scale)
		ipts.append(ipt*scale)
	#################################
	R.append(rpts)
	I.append(ipts)

############################################
fR=[]
fI=[]

for n in range(totaln):
	sr=0
	si=0
	for  j in range(len(R)):
		sr+= (R[j])[n]
		si+= (I[j])[n]

	fR.append(sr)
	fI.append(si)

#############################################
x1=[]
for n in range(totaln):
	x1.append(n*Ts) 
X1 = np.array(x1)

yr =np.array(fR)
yi =np.array(fI)
#########################################################################
#end of IFFT
########################################################################












#######################################################################################3
#continuous
########################################################################################

phi2=0

R2=[]
I2=[]
##########3
for kk in k:
	fk = kk * fsub
	rpts2=[]
	ipts2=[]

	signal2=[]
	signal2.append(data[2*kk])
	signal2.append(data[2*kk+1])
	################################
	#black constellation
	if signal2 == [0,0]:
		phi2 =bphi4
	elif signal2 == [0,1]:
		phi2 =bphi1
	elif signal2 == [1,0]:
		phi2 =bphi3
	elif signal2 == [1,1]:
		phi2 =bphi2
	else:
		phi2 =0
	#################################
	for tt in range(T):
		rpt2=math.cos(2*math.pi *fk*tt)*math.cos(phi2)-math.sin(2*math.pi *fk*tt)*math.sin(phi2)
		ipt2 = math.cos(2*math.pi *fk*tt)*math.sin(phi2)+math.sin(2*math.pi *fk*tt)*math.cos(phi2)

		rpts2.append(rpt2*scale)
		ipts2.append(ipt2*scale)
	#################################
	R2.append(rpts2)
	I2.append(ipts2)

############################################

fR2=[]
fI2=[]

for i in range(T):
	sr2=0
	si2=0
	for  j in range(len(R)):
		sr2+= (R2[j])[i]
		si2+= (I2[j])[i]

	fR2.append(sr2)
	fI2.append(si2)

#############################################
X2 = np.arange(T)
yr2 =np.array(fR2)
yi2 =np.array(fI2)
##################################

###############################################################################
#end of continuous
####################################################################


######################################
plt.xlabel('ns')
plt.ylabel('real value')
plt.xticks(np.arange(0, 500, 10))
plt.xlim([0, 500])
plt.plot(X2, yr2, color="red")
plt.stem(X1, yr) 
plt.show() 
########################################
plt.xlabel('ns')
plt.ylabel('imaginary value')
plt.xticks(np.arange(0, 500, 10))
plt.xlim([0, 500])
plt.plot(X2, yi2, color="red")
plt.stem(X1, yi) 
plt.show() 

