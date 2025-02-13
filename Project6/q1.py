from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

############################################
#(1a)
dd = loadmat('HW6-1a.mat')

#print(dd)
dat=dd['Hmatrix']
dat2=dd['y']
H = np.array(dat)# H
Y= np.array(dat2)# y

Hinv=np.linalg.inv(H)
xhat = np.matmul(Hinv, Y)

print("(1a) Gzf Y")
print(xhat)
###############################################3
#(1b)
dd2 = loadmat('HW6-1b.mat')

#print(dd2)
dat3=dd2['Hmatrix']
dat4=dd2['yprime']
H2 = np.array(dat3)# H
Y2= np.array(dat4)# y

Hinv2=np.linalg.inv(H2)
xhat2 = np.matmul(Hinv2, Y2)

print("(1b) Gzf Y")
print(xhat2)
#############################################3
#(1c)
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

#####################################################################33

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
######################################################################

######################################################################
bers=[]
for j in range(len(snrR)):
	snrdb=(snrR[j])/10

	#s2noise=pow(10,snrdb)

	V =  math.sqrt( ((Es)/(3*pow(10,snrdb))) )#


	prebits=''
	for ss in signals:
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
		xhat3 = np.matmul(Hinv, Y3)

		x1=xhat3[0]
		x2=xhat3[1]
		x3=xhat3[2]

		prebits += judge(x1)
		prebits += judge(x2)
		prebits += judge(x3)
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
print(len(bers))
print(len(snrR))


plt.plot(snrR, bers, label='bers', color='blue', marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('SNR in (db) in log scale')
plt.ylabel('BER in log scale')
plt.title('BER v.s SNR(db)')

plt.legend()
plt.grid(True)
plt.show()
