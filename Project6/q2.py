from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath


#################################################################3
dd = loadmat('HW6-1b.mat')

dat=dd['Hmatrix']
dat2=dd['yprime']
H = np.array(dat)
Y = np.array(dat2)
##########################################3

#initialization
ytemp = Y
Htemp = H
rounds = H.shape[1]
###################################################################################3

for r in range(rounds):
	G1 = np.matmul(np.conjugate(Htemp.T), Htemp)
	G2 = np.matmul(np.linalg.inv(G1), np.conjugate(Htemp.T))              

	#########################################
	norms=[]
	for i in range(G2.shape[0]):
		norm=0

		for j in range(G2.shape[1]):
			se = G2[i][j]
			norm += (se.real) **2
			norm += (se.imag) **2
		####################################33
		norms.append(norm)

	##########################################
	smind=np.argmin(norms)
	##############################################
	grow=G2[smind, :]
	xalpha=np.matmul(grow, ytemp)

	hextract = Htemp[:,smind]
	hextract = hextract.reshape(hextract.shape[0],1)

	#print(xalpha)
	xalpha = xalpha.reshape(xalpha.shape[0],1)
	ytemp = ytemp - np.matmul(hextract , xalpha)

	Htemp = np.delete(Htemp, smind, axis=1)


	#############################################################
	if r ==0:
		print("(2a) Which signal should be detected first?")
		if smind==0:
			print("x(1)")
		elif smind==1:
			print("x(2)")
		else:
			print("x(3)")
		print("(2b) please write down your first detected output 𝑥^(alpha 1) after decision.:")
		print(xalpha)
	############################################################
		print("(2c) Please write down the equation 𝐲(1) = 𝐇(1) 𝐱(1):")
		print("𝐇(1):")
		print(Htemp)
		print("𝐲(1):")
		print(ytemp)
	if r==1:
		print("(2d) please write down the second detected output 𝑥^(alpha 1):")
		print(xalpha)
	if r ==2:
		print("(2e) Complete the detection for the remaining symbol:")
		print(xalpha)
##########################################################################################################

#(2f)
obnum=3000

snrR=[]
m=-30
for t in range(50):
	#snrR.append(t)
	#m+=1
	snrR.append(m)
	m+=1

#############################3
bit2wave = dict()
bit2wave['0101'] = 3 + 3j
bit2wave['0001'] = 1 + 3j
bit2wave['1001'] = -1 + 3j
bit2wave['1101'] = -3 + 3j

bit2wave['0100'] = 3 + 1j
bit2wave['0000'] = 1 + 1j
bit2wave['1000'] = -1 + 1j
bit2wave['1100'] = -3 + 1j

bit2wave['0110'] = 3 -1j
bit2wave['0010'] = 1 -1j
bit2wave['1010'] = -1 -1j
bit2wave['1110'] = -3 -1j

bit2wave['0111'] = 3 - 3j
bit2wave['0011'] = 1 - 3j
bit2wave['1011'] = -1 - 3j
bit2wave['1111'] = -3 - 3j
#############################################

bits = np.random.randint(0, 2, obnum*4)

#####################################################
ans=''
for i in range(bits.shape[0]):
	ans += str(bits[i])

xx=[]
for i in range(obnum):
	s0 = str(bits[(4*i)])
	s1 = str(bits[(4*i +1)])
	s2 = str(bits[(4*i +2)])
	s3 = str(bits[(4*i +3)])
	see = s0 + s1 + s2 + s3
	x=bit2wave[see]
	xx.append(x)
###############################################

batch = int(len(xx)/3)
signals=[]
for i in range(batch):
	signal=[]
	signal.append(xx[(3*i)])
	signal.append(xx[(3*i+1)])
	signal.append(xx[(3*i+2)])
	signals.append(signal)
######################3

def judge(myx):

	if myx.real >=0:
		if myx.real <=2:
			#1
			#################################
			if myx.imag >=0:
				if myx.imag <=2:
					#1j
					return '0000'
				else:
					#3j
					return '0001'
			else:
				if myx.imag >=-2:
					#-1j
					return '0010'
				else:
					#-3j
					return '0011'
			#################################3
		else:
			#3
			if myx.imag >=0:
				if myx.imag <=2:
					#1j
					return '0100'
				else:
					#3j
					return '0101'
			else:
				if myx.imag >=-2:
					#-1j
					return '0110'
				else:
					#-3j
					return '0111'
	else:
		if myx.real >= -2:
			#-1
			#################################
			if myx.imag >=0:
				if myx.imag <=2:
					#1j
					return '1000'
				else:
					#3j
					return '1001'
			else:
				if myx.imag >=-2:
					#-1j
					return '1010'
				else:
					#-3j
					return '1011'
			#################################3
		else:
			#-3
			if myx.imag >=0:
				if myx.imag <=2:
					#1j
					return '1100'
				else:
					#3j
					return '1101'
			else:
				if myx.imag >=-2:
					#-1j
					return '1110'
				else:
					#-3j
					return '1111'

################################################################
Es=0
myxi=[-3,-1,1,3]
myxq=[-3j, -1j, 1j, 3j]
myxx=[]
for xii in myxi:
	for xqq in myxq:
		myx=xii + xqq

		val=(myx.conjugate()) * myx

		Es +=val

Es = (Es/16).real
###########################################################################
bers=[]
for j in range(len(snrR)):
	#snr=snrR[j]

	snrdb=(snrR[j])/10
	#s2noise=pow(10,snrdb)
	V =  math.sqrt( ((Es)/(3*pow(10,snrdb))) )#

	prebits=''
	for ss in signals:
		Htemp = H

		rounds = H.shape[1]
		######################################
		#a0 = ss[0]
		#a1 = ss[1]
		#a2 = ss[2]
		#E= np.conj(a0)*a0 + np.conj(a1)*a1 + np.conj(a2)*a2
		#v=(E*(1/snr))/3
		#V=math.sqrt(v.real)
		rd1 = np.random.normal(0, V, 1)
		rd2 = np.random.normal(0, V, 1)
		rd3 = np.random.normal(0, V, 1)

		Y3=np.matmul(H, np.array(ss)) + np.array([rd1[0],rd2[0],rd3[0]])
		
		ytemp = Y3.reshape(Y3.shape[0],1)
		

		###################################################################
		xalphas=[]
		#SM=[]
		hh=[]
		##############################
		for r in range(rounds):
			G1 = np.matmul(np.conjugate(Htemp.T), Htemp)
			G2 = np.matmul(np.linalg.inv(G1), np.conjugate(Htemp.T))              

			#########################################
			norms=[]
			for i in range(G2.shape[0]):
				norm=0

				for j in range(G2.shape[1]):
					se = G2[i][j]
					norm += (se.real) **2
					norm += (se.imag) **2
					####################################33
				norms.append(norm)

			##########################################
			smind=np.argmin(norms)
			##############################################
			grow=G2[smind, :]
			xalpha=np.matmul(grow, ytemp)

			#print(xalpha)

			hextract = Htemp[:,smind]
			hextract = hextract.reshape(hextract.shape[0],1)

			xalpha = xalpha.reshape(xalpha.shape[0],1)
			#print(xalpha)
			xalphas.append(xalpha[0][0])

			ytemp = ytemp - np.matmul(hextract , xalpha)
			Htemp = np.delete(Htemp, smind, axis=1)

			#SM.append(smind)
			hh.append(hextract[0][0])
			
		###################################################################
		########################################################################3
		realind=[]
		for m in range(rounds):
			ch=hh[m]
			for p in range(rounds):
				if H[0][p] == ch:
					realind.append(p)
		#######################################################

		mymap={xalphas[0]: realind[0], xalphas[1]: realind[1], xalphas[2]: realind[2]}
		xalphas.sort(key=lambda x: mymap[x])

		prebits += judge(xalphas[0])
		prebits += judge(xalphas[1])
		prebits += judge(xalphas[2])
		############################################################
	################################################
		
	right=0
	wrong=0
	for k in range(bits.shape[0]):
		if prebits[k] == ans[k]:
			right +=1
		else:
			wrong +=1
	ber= (wrong/(right + wrong))
	##################################################
	bers.append(ber)


print("bers")
print(bers)

print(snrR)

plt.plot(snrR, bers, label='bers', color='blue', marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('SNR in (db) in log scale')
plt.ylabel('BER in log scale')
plt.title('BER v.s SNR(db)')

plt.legend()
plt.grid(True)
plt.show()
