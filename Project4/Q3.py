import random
import cmath
import math
import matplotlib.pyplot as plt

NN=[]
THETAE=[]

PHASE=[]

for n in range(200):
	NN.append(n)
	s = random.randint(0, 3)

	##############################
	if s==0:
		phi = math.pi* (1/4) 
	elif s==1:
		phi = math.pi* (3/4)
	elif s==2:
		phi = math.pi* (5/4)
	else:
		phi = math.pi* (7/4)   
	###################################

	pp= 2*math.pi *(n/500)# your true phase of the subcarrier, not related to data 
	PHASE.append(pp)
	##########################################


	pn= math.cos(phi) + math.sin(phi)*1j
	sn=pn*cmath.exp(1j * 2*math.pi*(1/500)*n)
	########################################
	if sn.real <0:
		din =-1
	else:
		din =1
	##############################
	if sn.imag <0:
		dqn =-1
	else:
		dqn =1
	##################################
	thetae = sn.real * dqn - sn.imag * din
	dn = din + dqn * 1j
	#####################
	THETAE.append(thetae)

########################################################

plt.plot(NN, THETAE, marker='o', linestyle='-', color='b')


plt.xticks(range(min(NN), max(NN) + 1, 10))
plt.yticks(range(int(min(THETAE)), int(max(THETAE)) + 1, 1))


plt.xlabel('n')  
plt.ylabel('thetae (n)')
plt.title('thetae (n) versus time n')

# Display grid to make reading values easier
plt.grid(True)

# Show the plot
plt.show()
#################################################################



plt.plot(NN, PHASE, marker='o', linestyle='-', color='b')


plt.xticks(range(min(NN), max(NN) + 1, 10))
plt.yticks(range(int(min(PHASE)), int(max(PHASE)) + 1, 1))


plt.xlabel('n')  
plt.ylabel('true phase rotation')
plt.title('true phase rotation versus time n')

# Display grid to make reading values easier
plt.grid(True)

# Show the plot
plt.show()