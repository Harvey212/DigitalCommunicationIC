from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

#(1a)
Ng=32 #cyclic prefix
N=128
R= 96
L =64
#####################################
M=640
##########################################
dd = loadmat('HW4-2.mat')
dat=dd['OFDMTx']
see = np.array(dat)
data=see[0]

PHI=[]
MS=[]

for m in range(M):
	MS.append(m)
	########################
	res=0
	for r in range(R):
		ind1=m-r
		ind2=m-r-L

		########################3
		if (ind1 <0) or (ind1 >= M):
			z1=0
		else:
			z1 = data[ind1] * cmath.exp(1j * 2* math.pi * 5.7 *(ind1/N))
		#####################
		if (ind2 <0) or (ind2 >= M):
			z2 =0
		else:
			z2 = np.conjugate(data[ind2]  * cmath.exp(1j * 2* math.pi * 5.7 *(ind2/N))   )    
		########################
		res += z1 * z2
	########################################3
	PHI.append(abs(res))


plt.xlabel('delay')  
plt.ylabel('PHI DC(m)')
plt.title('(1a) magnitude of the delay and correlate result PHI DC(m)')
#####################################
plt.plot(MS, PHI, marker='o', linestyle='-', color='b')

peak_y = max(PHI)
peak_x = MS[PHI.index(peak_y)]


plt.annotate(f'Peak ({peak_x}, {peak_y})', 
             xy=(peak_x, peak_y), 
             xytext=(peak_x, peak_y + 1),  
             arrowprops=dict(facecolor='red', shrink=0.05),
             ha='center', color='red')

plt.xticks(range(0, M+1, 20))
plt.yticks(range(int(min(PHI)), int(max(PHI)) +1, 1))

plt.grid(True)
plt.show()

########################################################################################3


#(1c)

res2=0

DC=160
for rr in range(R):
	ind1=DC-rr
	ind2=DC-rr-L

	########################3
	if (ind1 <0) or (ind1 >= M):
		Z1=0
	else:
		Z1 = data[ind1] * cmath.exp(1j * 2* math.pi * 5.7 *(ind1/N))
	#####################
	if (ind2 <0) or (ind2 >= M):
		Z2 =0
	else:
		Z2 = np.conjugate(data[ind2]  * cmath.exp(1j * 2* math.pi * 5.7 *(ind2/N))   )    
	########################
	res2 += Z1 * Z2
	########################################3
###########################

ang = cmath.phase(res2)
esp= ang * (N/(2*math.pi * L))

print("epsilon : {}".format(esp))
