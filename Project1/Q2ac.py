import math

import matplotlib.pyplot as plt
import numpy as np



######################################################
#start of Q2 (a)
################################################################3

#######################################################
T=200 #ns
#fc = 20 #Mhz #10^6 pt/s
#fc = 20* pow(10,6) #pt/s
fc = 20 * pow(10,-3) #pt/ns

data=[0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]

######################################################
#white constellation
wphi1=0
wphi2=math.pi/2
wphi3=math.pi
wphi4=math.pi*(3/2)
#####################################

#black constellation
bphi1=math.pi*(1/4)
bphi2=math.pi*(3/4)
bphi3=math.pi*(5/4)
bphi4=math.pi*(7/4)
########################################
phi=0
rpt=0
ipt=0
ptt=0
###########
#QPSK baseband
#t=1.6 #us
t = 1.6 * pow(10,3) #ns

QPSKr=[]
QPSKi=[]
for i in range(8):
	signal=[]
	signal.append(data[2*i])
	signal.append(data[2*i+1])
	################################
	if signal == [0,0]:
		phi =wphi1
	elif signal == [0,1]:
		phi =wphi2
	elif signal == [1,0]:
		phi =wphi4
	elif signal == [1,1]:
		phi =wphi3
	else:
		phi =0
	#################################
	for tt in range(T):
		rpt=math.cos(phi)#math.cos(2*math.pi *fc*tt)*math.cos(phi*tt)
		QPSKr.append(rpt)

		ipt =math.sin(phi)# -math.sin(2*math.pi *fc*tt)*math.sin(phi*tt)
		QPSKi.append(ipt)
############################################
#OQPSK xq(t) delay T/2 for baseband
OQKPSKi=[]

for tt in range(int(T/2)):
	OQKPSKi.append(0)

for tt in range(int(t-T/2)):
	poq=QPSKi[tt]
	OQKPSKi.append(poq)

##################################################
#to calculate OQPSK passband
OQKPSKPts =[]

for tt in range(int(t)):
	ptt=  QPSKr[tt]* math.cos(2*math.pi *fc*tt)  - OQKPSKi[tt] *math.sin(2*math.pi *fc*tt)
	OQKPSKPts.append(ptt)

#print(len(OQKPSKPts))
#print(OQKPSKPts)
###################################
#plot

sample = 1600
x = np.arange(sample)
y =np.array(OQKPSKPts)

plt.plot(x, y)
plt.xlabel('ns')
plt.ylabel('amplitude')
plt.show()

######################################################
#end of Q2 (a)
################################################################3


######################################################
#start of Q2 (c)
################################################################3
#####################################################################333
fft_signal = np.fft.fft(y)
freqs = np.fft.fftfreq(len(y),1/fc)#
power_spectrum = np.abs(fft_signal) ** 2
power_spectrum_db = 10 * np.log10(power_spectrum)
idx = np.where(freqs >= 0)
freqs = freqs[idx]
power_spectrum_db = power_spectrum_db[idx]

plt.figure(figsize=(10, 6))
plt.plot(freqs, power_spectrum_db, color='blue')
plt.title("Power Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.show()

######################################################
#end of Q2 (c)
################################################################3