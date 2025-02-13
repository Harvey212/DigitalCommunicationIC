import numpy as np
import matplotlib.pyplot as plt



s=3

num=s+1 # 4,binary:0000100

temp=[0,0,0,0,0,0,0,1,0]

#1,4,8,9
roun=511#20
output=[]
for r in range(roun):
	#print(temp[8])
	output.append(temp[8])
	x9=temp[0]
	x8=temp[1]
	x4=temp[5]
	x1=temp[8]

	inp=((x1^x4)^x8)^x9
	###########################
	newtemp=[]
	newtemp.append(inp)
	for j in range(8):
		newtemp.append(temp[j])
	##########################
	temp = newtemp
#####################################
D=[]

for k in range(len(output)):
	op=output[k]
	dn=pow(-1,op)
	D.append(dn)
######################################
N=511#20
phisl=[]
####################################

for l in range(-N,N+1,1):
	s1=0
	s2=0
	summ=0
	##############################
	for n in range(N):
		s1=D[n]
		############################
		tempn=(n+l)%N
		##############################
		s2= D[tempn]
		##############################
		summ += (s1*s2)/N
	################################
	phisl.append(abs(summ))
##############################################




#print(len(phisl))
tim=np.arange(-N, N+1, 1)

plt.xlabel('l')
plt.ylabel('|Phis(l)|')
plt.xticks(np.arange(-N, N+1, 1))
plt.xlim([-N, N])
plt.plot(tim, phisl, color="red") 
plt.show() 




