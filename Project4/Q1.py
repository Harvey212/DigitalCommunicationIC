import random
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

N=32
#H = []
#############################################
#(a)
Cm=[]
m= 3
for n in range(N):
	cc = cmath.exp( 2* math.pi *(m/N)*n*1j)
	Cm.append(cc)
##############################################

thetas=[]
CHs=[]
trb=(-1/2)*(math.pi)
for n in range(N+1):
	##################################
	Ar=[]

	for k in range(N):
		ar = cmath.exp( math.pi*k*math.sin(trb) *1j)
		Ar.append(ar)
	################################
	#At = [1] 
	################################
	see1 =np.reshape(np.transpose(np.array(Ar)) , (N,-1))
	see2 =np.reshape(np.matrix(Cm).getH(), (-1,N)  )

	CH = np.matmul(see2, see1)
	CHs.append(abs(CH.item() ) )
	thetas.append(trb)
	trb = trb + (1/32)*(math.pi)
###############################################################

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.plot(np.array(thetas), np.array(CHs))

# Set title and labels
ax.set_title("Beam Pattern", va='bottom')
ax.set_theta_zero_location("N")  # 0 degrees at the top
ax.set_theta_direction(-1)  # Clockwise angles

# Show plot
plt.show()
####################################################################
#(b)
print("(1b)")

MM=[]
thetar = (1/4) * math.pi
#thetat = (1/6) * math.pi
Ar2=[]

for kk in range(N):
	ar2 = cmath.exp( math.pi*kk*math.sin(thetar) *1j)
	Ar2.append(ar2)
	
SEE1 =np.reshape(np.transpose(np.array(Ar2)) , (N,-1))

CH2s = []
MM = []
#Phis=[]
for mm in range(-16,16):
	MM.append(mm)

	#phi =np.arcsin((2*m)/N)
	#Phis.append(phi)
	########################################	
	Cmm2=[]
	for n in range(N):
		cc2 = cmath.exp( 2* math.pi *(mm/N)*n*1j)
		Cmm2.append(cc2)
	#######################################
		
	SEE2 =np.reshape(np.matrix(Cmm2).getH(), (-1,N)  )
	CH2 = np.matmul(SEE2, SEE1)
	CH2s.append(abs(CH2.item() ) )
		
###############################################################
plt.plot(MM, CH2s, marker='o', linestyle='-')  # Line with markers
plt.xlabel('m')  # Label for x-axis
plt.xticks(range(-16, 16, 1))

plt.ylabel('|Cm H |')  # Label for y-axis
plt.title('(1b) |Cm H | vs m Plot') # Plot title
plt.show()

mam=11
psi =np.arcsin((2*mam)/N)

print("|Cm H |")
print(CH2s)
print("thetar value: {} ,m value: {} , psi value: {}".format(thetar ,mam ,psi) )
##############################################


#(c)
print("(1c)")

thetar1 = (1/4) * math.pi
thetar2 = thetar1 +0.4
alpha1 = 0.4 -0.7j
alpha2 = 0.2 +0.3j
L=2

Vec3 =[]

for kk in range(N):
	v1 = cmath.exp( math.pi*kk*math.sin(thetar1) *1j) *alpha1* (1/math.sqrt(L))
	v2 = cmath.exp( math.pi*kk*math.sin(thetar2) *1j) * alpha2 * (1/math.sqrt(L))
	v3 = v1+v2

	Vec3.append(v3)
##########

SS1 =np.reshape(np.transpose(np.array(Vec3)) , (N,-1))

#print(SS1.shape)


CH3s =[]
MM3 = []
for mm3 in range(-16,16):
	MM3.append(mm3)

	Cmm3=[]
	for n3 in range(N):
		cc3 = cmath.exp( 2* math.pi *(mm3/N)*n3*1j)
		Cmm3.append(cc3)
	#######################################
		
	SS2 =np.reshape(np.matrix(Cmm3).getH(), (-1,N)  )

	#print(SS2.shape)

	CH3 = np.matmul(SS2, SS1)
	CH3s.append(abs(CH3.item() ) )
		
###############################################################
plt.plot(MM3, CH3s, marker='o', linestyle='-')  # Line with markers
plt.xlabel('m')  # Label for x-axis
plt.xticks(range(-16, 16, 1))

plt.ylabel('|Cm H |')  # Label for y-axis
plt.title('(1c) |Cm H | vs m Plot') # Plot title
plt.show()


############################################

mam1=11
mam2=15
psi1 =np.arcsin((2*mam1)/N)
psi2 =np.arcsin((2*mam2)/N)

print("|Cm H |")
print(CH3s)
print("thetar1 value: {} ,m1 value: {} , psi1 value: {}".format(thetar1 ,mam1 ,psi1) )

print("thetar2 value: {} ,m2 value: {} , psi2 value: {}".format(thetar2 ,mam2 ,psi2) )

