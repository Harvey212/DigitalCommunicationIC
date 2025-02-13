import math
import cmath

import matplotlib.pyplot as plt
import numpy as np


#############################


##########################################
d1=[0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
d2=[1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0]
d3=[]
for d in d1:
	d3.append(d)
for d in d2:
	d3.append(d)
#############################################3 
M=8
N=4

#T=500 #ns
#fsub = 2*pow(10,-3) #1/ns
#Ts =31.25 #ns

#periodn=int(T/Ts)
#totaln=periodn*N

#############################################
#phase=[]

#for i in range(len(d3)):
#	if d3[i]==0:
#		phase.append(0)
#	else:
#		phase.append(math.pi)
##########################################
Xdd=np.zeros((M, N),dtype=np.complex_) #
Xtf=np.zeros((M, N),dtype=np.complex_)#,dtype=np.complex_
####################################
rp=0
ip=0
####################
for j in range(N):
	for i in range(M):
		k = j*M +i

		if d3[k]==0:
			#rp=math.cos(0)
			#ip=math.sin(0)
			Xdd[i,j]=1#cmath.exp(0j)
		else:
			Xdd[i,j]=-1#cmath.exp(math.pi*1j)

#######################################################
#Xtf=np.fft.ifft2(Xdd)

################################################################
#for mm in range(M):
#	for nn in range(N):
		#############################################################################3
#		s1=0
#		for k in range(N):
#			for l in range(M):
#				s1 += Xdd[l,k]*cmath.exp(2*math.pi*((nn*k)/N - (mm*l)/M)*1j)
		########################################################################## 
#		Xtf[mm,nn] = s1/math.sqrt(N*M)
################################################################


############################################################
#temp=[]
#for n in range(totaln):
#	j= int(n/periodn)

	
	####################################
	#to carry 𝑥𝐵𝐵(𝑛𝑇𝑠) for each subcarrier
#	ss=0
	###################################
#	for i in range(M):
#		fk = fsub *i		
#		s=Xtf[i,j]*cmath.exp(2*math.pi*fk*n*Ts*1j)
#		ss+=s
	########################
#	temp.append(ss)
	####################################
#################################################################
#IFFT
temp=[]
for nn in range(N):
	#j= int(n/periodn)

	
	####################################
	#to carry 𝑥𝐵𝐵(𝑛𝑇𝑠) for each subcarrier
	ss=0
	###################################
	for mm in range(M):
		#fk = fsub *i		
		#s=Xtf[i,j]*cmath.exp(2*math.pi*fk*n*Ts*1j)
		s=(Xdd[mm,nn]*cmath.exp(2*math.pi*(mm/M)*nn*1j) )/M
		ss+=s
	########################
	temp.append(ss)
	####################################





#temp2=np.array(temp)
#temp3 = np.fft.ifft(temp2)
#print(temp3) 
#########################
#tim=[]
#for n in range(totaln):
#	t1=Ts * n
#	tim.append(t1)
######################
tim=[]
for t1 in range(N):
	#t1=Ts * n
	tim.append(t1)



#for i in range(len(temp)):
#	print(temp[i])


#print(temp)

RR=[]
II=[]

for i in range(len(temp)):
	see=temp[i]
	RR.append(see.real)
	II.append(see.imag)
############################3
######################################
plt.xlabel('time slot n')
plt.ylabel('real value')
plt.xticks(np.arange(0, 4))
plt.xlim([0, 4])
plt.plot(tim, RR, color="red")
plt.show() 
########################################
#plt.xlabel('ns')
#plt.ylabel('imaginary value')
#plt.xticks(np.arange(0, T*N, T))
#plt.xlim([0, T*N])
#plt.plot(tim, II, color="red")
#plt.show() 


plt.xlabel('time slot n')
plt.ylabel('imaginary value')
plt.xticks(np.arange(0, 4))
plt.xlim([0, 4])
plt.plot(tim, II, color="red")
plt.show() 
