import numpy as np
import matplotlib.pyplot as plt


s=[1,1,-1,1,1, -1,1,-1,-1,-1, 1,1,1,1,-1,1]

K=[]
RES=[]

for k in range(-16,17):
	res=0
	K.append(k)
	for n in range(16):
		res+=s[n] * s[((n+k)%16)]
	##########################
	RES.append(res/16)
####################################

print("PHI(k)")
print(RES)
plt.xlabel('k')  
plt.ylabel('PHI(k)')
plt.title('(2) magnitude of the delay and correlate result PHI(k)')
#####################################
plt.plot(K, RES, marker='o', linestyle='-', color='b')

plt.xticks(range(-16, 17, 1))
plt.yticks(range(int(min(RES)), int(max(RES)) +1, 1))

plt.grid(True)
plt.show()