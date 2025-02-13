from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

Ng=32 #cyclic prefix
N=128
R= 32
L =64
#####################################
M=640
##########################################
dd = loadmat('HW4.mat')
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
			z1 = data[ind1]
		#####################
		if (ind2 <0) or (ind2 >= M):
			z2 =0
		else:
			z2 = np.conjugate(data[ind2])    
		########################
		res += z1 * z2
	########################################3
	PHI.append(abs(res))


plt.xlabel('delay')  
plt.ylabel('PHI DC(m)')
plt.title('(4a) magnitude of the delay and correlate result PHI DC(m)')
#####################################
plt.plot(MS, PHI, marker='o', linestyle='-', color='b')

peak_y = max(PHI)
peak_x = MS[PHI.index(peak_y)]

# Mark the peak point on the plot
plt.annotate(f'Peak ({peak_x}, {peak_y})', 
             xy=(peak_x, peak_y), 
             xytext=(peak_x, peak_y + 1),  # Adjust text position
             arrowprops=dict(facecolor='red', shrink=0.05),
             ha='center', color='red')

# Set ticks with step of 1 on both x and y axes
plt.xticks(range(0, M+1, 20))
plt.yticks(range(int(min(PHI)), int(max(PHI)) +1, 1))

# Show grid for readability
plt.grid(True)

# Show the plot
plt.show()

########################################################################################3



R2= 96
L2 =64
PHI2=[]

MS2=[]

for m in range(M):
	MS2.append(m)
	########################
	res2=0
	for r2 in range(R2):
		ind12=m-r2
		ind22=m-r2-L2

		########################3
		if (ind12 <0) or (ind12 >= M):
			z12=0
		else:
			z12 = data[ind12]
		#####################
		if (ind22 <0) or (ind22 >= M):
			z22 =0
		else:
			z22 = np.conjugate(data[ind22])    
		########################
		res2 += z12 * z22
	########################################3
	PHI2.append(abs(res2))


plt.xlabel('delay')  
plt.ylabel('PHI DC(m)')
plt.title('(4c) magnitude of the delay and correlate result PHI DC(m)')
#####################################
plt.plot(MS2, PHI2, marker='o', linestyle='-', color='b')

peak_y2 = max(PHI2)
peak_x2 = MS2[PHI2.index(peak_y2)]

# Mark the peak point on the plot
plt.annotate(f'Peak ({peak_x2}, {peak_y2})', 
             xy=(peak_x2, peak_y2), 
             xytext=(peak_x2, peak_y2 + 1),  # Adjust text position
             arrowprops=dict(facecolor='red', shrink=0.05),
             ha='center', color='red')

# Set ticks with step of 1 on both x and y axes
plt.xticks(range(0, M+1, 20))
plt.yticks(range(int(min(PHI2)), int(max(PHI2)) +1, 1))

# Show grid for readability
plt.grid(True)

# Show the plot
plt.show()
