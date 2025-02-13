import numpy as np
import matplotlib.pyplot as plt

alpha=3

def create(L,H):

	N=L.shape[0]
	for i in range(H.shape[0]):

		row= i%N
		for j in range(H.shape[1]):
			col=j%N

			if (i>=N) and (j>=N):
				H[i,j]= -L[row,col]
			else:
				H[i,j]= L[row,col]


	return H



w1=np.zeros((1,1))
w1[0,0]=1
#####################
w2=np.zeros((2,2))
w2=create(w1,w2)
#print(w2)
#######################
w4=np.zeros((4,4))
w4=create(w2,w4)
#print(w4)
######################
w8 =np.zeros((8,8))
w8=create(w4,w8)
##################
w16 =np.zeros((16,16))
w16=create(w8,w16)
########################
w32 =np.zeros((32,32))
w32=create(w16,w32)
######################
w64 =np.zeros((64,64))
w64=create(w32,w64)
######################
###############################################

Max=64
temp=[]
for u in range(Max):
	summ=0
	#################
	for j in range(Max):
		summ+=(w64[j,alpha+1] * w64[j,u])/64
	###################
	temp.append(summ)
#############################################

tim=np.arange(0, Max, 1)

plt.xlabel('u')
plt.ylabel('Gamma w(u)')
plt.xticks(np.arange(0, Max, 1))
plt.xlim([0, 63])
plt.plot(tim, temp, color="red") 
plt.show() 

