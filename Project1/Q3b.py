import math

import matplotlib.pyplot as plt
import numpy as np

T=500 #ns
#fsub = 2*pow(10,6) #Hz   #subcarrier spacing
fsub = 2*pow(10,-3) #1/ns

#fs = 32*pow(10,6) #Hz #sampling rate

#Ts =31.25 #ns

data=[0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
k=[1,3,5,7]
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
###########
#
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
	for tt in range(T):
		rpt=math.cos(2*math.pi *fk*tt)*math.cos(phi)-math.sin(2*math.pi *fk*tt)*math.sin(phi)
		ipt = math.cos(2*math.pi *fk*tt)*math.sin(phi)+math.sin(2*math.pi *fk*tt)*math.cos(phi)

		rpts.append(rpt)
		ipts.append(ipt)
	#################################
	x = np.arange(T)
	yr =np.array(rpts)
	yi =np.array(ipts)
	##################################
	print(kk)
	plt.plot(x, yr)
	plt.xlabel('ns')
	plt.ylabel('real value')
	plt.show()
	###############################
	plt.plot(x, yi)
	plt.xlabel('ns')
	plt.ylabel('imaginary value')
	plt.show()

############################################
#
#
