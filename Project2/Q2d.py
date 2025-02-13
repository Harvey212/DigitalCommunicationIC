import numpy as np
import matplotlib.pyplot as plt
import random
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

c1=w64[:,alpha+1]
c2=w64[:,14]
####################################
#c1=w64[:,alpha+1]
#c2=w64[:,13]
#print(sum(c2))

#print(c1)
#print(sum(c1))
###########################
##################################
#random.seed(13)
#data=[]

#for i in range(8):
#	d = random.random()

#	if d > .5:
#		data.append(1)
#	else:
#		data.append(-1)
############################################
d=[-1, 1, 1, 1, -1, -1, 1, -1]

#print('before spreading.')

#plt.xlabel('sequence')
#plt.ylabel('value')
#plt.xticks(np.arange(0, 8, 1))
#plt.xlim([0, 8])
#plt.stem(np.arange(0, 8, 1), d) 
#plt.show() 
###################################################
y=[]

for i in range(len(d)):
	di=d[i]

	for j in range(len(c1)):
		c1i=c1[j]
		y.append(di*c1i)
###########################################
for i in range(4):
	y.append(0)

#############################################

p=[]

for i in range(8):
	summ=0
	for j in range(64):
		summ+= (d[i]*c1[j]*c2[j])/64#(y[64*i+j])*(c2[j])/64
	

	##################################
	p.append(summ)
############################################



##############################################
print('after disspreading.')

plt.xlabel('sequence')
plt.ylabel('value')
plt.xticks(np.arange(0, 8, 1))
plt.xlim([0, 8])
plt.stem(np.arange(0, 8, 1), p) 
plt.show() 
