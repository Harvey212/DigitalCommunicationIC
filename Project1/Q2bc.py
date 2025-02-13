import math

import matplotlib.pyplot as plt
import numpy as np

######################################################
#start of Q2 (b)
################################################################3
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
#pi/4 QPSK passband
#t=1.6 #us
t = 1.6 * pow(10,3) #ns

PiQPSKpts=[]

for i in range(8):
	signal=[]
	signal.append(data[2*i])
	signal.append(data[2*i+1])
	################################
	if i%2 ==0:
		#odd symbol
		#black constellation
		if signal == [0,0]:
			phi =bphi4
		elif signal == [0,1]:
			phi =bphi1
		elif signal == [1,0]:
			phi =bphi3
		elif signal == [1,1]:
			phi =bphi2
		else:
			phi =0
	else:
		#even symbol
		#white constellation
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
		rpt=math.cos(2*math.pi *fc*tt)*math.cos(phi)
		ipt = -math.sin(2*math.pi *fc*tt)*math.sin(phi)
		
		ptt = rpt+ipt
		PiQPSKpts.append(ptt)
############################################


###################################
#plot

sample = 1600
x = np.arange(sample)
y =np.array(PiQPSKpts)

plt.plot(x, y)
plt.xlabel('ns')
plt.ylabel('amplitude')
plt.show()
######################################################
#end of Q2 (b)
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