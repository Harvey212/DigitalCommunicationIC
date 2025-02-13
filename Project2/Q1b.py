import math
import numpy as np
import cmath
import matplotlib.pyplot as plt


N=63
u1=29

u2=34
Omegasl=[]
Snu=[]
Snu2=[]
######################################
for n in range(N):
	s=cmath.exp((math.pi*n*(n+1)*u1*1j)/N)
	Snu.append(s)
#######################################
######################################
for n in range(N):
	s=cmath.exp((math.pi*n*(n+1)*u2*1j)/N)
	Snu2.append(s)
#######################################



#########################################
for l in range(-N,N+1,1):
	s1=0
	s2=0
	s3=0
	summ=0
	##############################
	for n in range(N):
		s1=Snu[n]
		############################
		tempn=0
		tempn=(n-l)%N
		##############################
		s2= np.conj(Snu2[tempn])
		##############################
		summ += (s1*s2)/N
	################################
	Omegasl.append(abs(summ))
##############################################
#print(phisl)


#print(len(phisl))
tim=np.arange(-N, N+1, 1)

#print(tim)

plt.xlabel('l')
plt.ylabel('|Omegas(l)|')
plt.xticks(np.arange(-N, N+1, 3))
plt.xlim([-N, N])
plt.plot(tim, Omegasl, color="red") 
plt.show() 

