import numpy as np
import random
import math
import cmath
import matplotlib.pyplot as plt


fs = 100 * pow(10,6)
cpnum=16

subcarnum=64
TB = 100 * pow(10,6)
################################################
#(4a)
#################################################
#bpsk=[random.choice([1, -1]) for _ in range(64)]
bpsk=[1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1]
print("BPSK data 𝑋k:")
#print(len(bpsk))
print(bpsk)
################################################
#(4b)
####################################################
N=64
points=[]
for n in range(N):
	ser=0
	###############################
	for k in range(N):
		ser+=cmath.exp(2*math.pi*(n/N)*k*1j)* bpsk[k]
	points.append(ser)
##################################

p2=points[(N-cpnum):N]

for i in range(len(points)):
	p2.append(points[i])
#####################
rp=[]
ip=[]

for i in range(len(p2)):
	see=p2[i]
	rp.append(see.real)
	ip.append(see.imag)
################################

tim=np.arange(-16, N, 1)

#print(tim)

plt.xlabel('n')
plt.ylabel('real value')
plt.xticks(tim)
plt.xlim([-16, N])
plt.plot(tim, rp, color="red")
plt.title("x[n] real part")  
plt.show()


plt.xlabel('n')
plt.ylabel('imaginary value')
plt.xticks(tim)
plt.xlim([-16, N])
plt.plot(tim, ip, color="red")
plt.title("x[n] imaginary part") 
plt.show()
################################################################333333
#(4c)
############################################################
h0=-0.6275966157352981+0.04201736349919818j
h1=0.5693649212482851+0.3118490684602431j
h2=-0.20218899894622525-0.023609172407679527j
h3=0.11379543934887607-0.3231510642514984j
h4=0.13966486533848485+0.06790215581585504j

#D=[0,10,40,80,100] ns
ntoui=[0,1,4,8,10]
####################################
#h[n] = summ {  hi x  delta[n-ntoui]     }
#h[n] has value only when n =[0,1,4,8,10] , and only has one of the ntoui
#h length is 5
###################################
#y[n] = h[n] convel x[n] = summ{  h[m] x X[n-m]   }
#y's n range from -16~ 73
#after 74 and above, all value is 0
####################################
#x[n] start from n=-16~63
#x length is 80
#########################################
upper=74
lower=-16
##################################

Ys=[]

for n in range(lower,upper): #till upper-1
	sw=0

	#####################################
	for m in ntoui:
		##########################
		if m ==0:
			h=h0
		elif m ==1:
			h=h1
		elif m ==4:
			h=h2
		elif m ==8:
			h=h3
		else:
			h=h4
		###############################3
		mm = n-m

		if (mm >= -16) and (mm<64):
			m2 = mm +16
			sw += h * p2[m2]
		else:
			sw+=0
	############################################
	Ys.append(sw)
#####################################################


rp2=[]
ip2=[]

for i in range(len(Ys)):
	see2=Ys[i]
	rp2.append(see2.real)
	ip2.append(see2.imag)
################################

tim2=np.arange(lower, upper, 1)

#print(tim)

###########################################################
plt.xlabel('n')
plt.ylabel('real value')
plt.xticks(tim2)
plt.xlim([lower, upper])
plt.plot(tim2, rp2, color="red")
plt.title("y[n] real part") 
plt.show()


plt.xlabel('n')
plt.ylabel('imaginary value')
plt.xticks(tim2)
plt.xlim([lower, upper])
plt.plot(tim2, ip2, color="red") 
plt.title("y[n] imaginary part")
plt.show()
###############################################################



#############################################
#(4d)
########################################################3
newy=[]

for i in range(16, 80):
	newy.append(Ys[i])
################################################

#newyr=[]
#for i in range(len(newy)):
#	newyr.append( (newy[i]).real )
##################################################3
fft_result = np.fft.fft(newy)
frequencies = np.fft.fftfreq(len(newy),1/(1*fs))



H1=[]
for i in range(len(fft_result)):
	h11= (fft_result[i]/bpsk[i])
	H1.append(h11)

print("Hk")
print(H1)

ind=np.arange(0,64)


###################################################[:len(frequencies)//2])#/len(H1)
plt.figure(figsize=(10, 5))
plt.plot(ind, np.abs(H1)) #frequencies[:len(frequencies)//2]
plt.title("Magnitude Spectrum of Hk in 4(d)")
plt.xlabel("index k") #index
plt.ylabel("Magnitude")
plt.show()

#[:len(frequencies)//2])
plt.figure(figsize=(10, 5))
plt.plot(ind, np.angle(H1)) #frequencies[:len(frequencies)//2]#/len(H1)
plt.title("Phase Spectrum of Hk in 4(d)")
plt.xlabel("index k")
plt.ylabel("Phase (Radians)")
plt.show()
#############################################

####################################################
#
#(4f)
##########################################################

















ntoui=[0,1,4,8,10]
####################################
#h[n] = summ {  hi x  delta[n-ntoui]     }
#h[n] has value only when n =[0,1,4,8,10] , and only has one of the ntoui
#h length is 5
###################################
#y[n] = h[n] convel x[n] = summ{  h[m] x X[n-m]   }
#y's n range from -16~ 73
#after 74 and above, all value is 0
####################################
#x[n] start from n=0~63
#########################################
#########################################
upper2=64
lower2=0
##################################

Zs=[]

for n in range(lower2,upper2): #till upper-1
	sw2=0

	#####################################
	for m in ntoui:
		##########################
		if m ==0:
			hh=h0
		elif m ==1:
			hh=h1
		elif m ==4:
			hh=h2
		elif m ==8:
			hh=h3
		else:
			hh=h4
		###############################3
		mm2 = n-m

		if (mm2 >= 0) and (mm2<64):
			sw2 += hh * points[mm2]
		else:
			sw2+=0
	############################################
	Zs.append(sw2)
#####################################################

fft_result2 = np.fft.fft(Zs)
frequencies2 = np.fft.fftfreq(len(Zs),1/(1*fs))#

H2=[]
for i in range(len(fft_result2)):
	h22= (fft_result2[i]/bpsk[i])
	H2.append(h22)

print("Hk'")
print(H2)

plt.figure(figsize=(10, 5))
plt.plot(ind, np.abs(H2)) #frequencies2[:len(frequencies2)//2]
plt.title("Magnitude Spectrum of Hk' in 4(f)")
plt.xlabel("index k")
plt.ylabel("Magnitude")
plt.show()


plt.figure(figsize=(10, 5))
plt.plot(ind, np.angle(H2)) #frequencies2[:len(frequencies2)//2]
plt.title("Phase Spectrum of Hk' in 4(f)")
plt.xlabel("index k")
plt.ylabel("Phase (Radians)")
plt.show()


#print(len(fft_result2))