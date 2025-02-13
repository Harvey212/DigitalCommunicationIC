from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

dd = loadmat('HW5-4Rev.mat')
dat1=dd['OFDMRx1']
dat2=dd['OFDMRx2']

see1 = np.array(dat1)
data1=see1[0]

see2 = np.array(dat2)
data2=see2[0]

########################################
newd1=[]
for i in range(32, len(data1)):
	newd1.append(data1[i])
###############################
newd2=[]
for i in range(32, len(data2)):
	newd2.append(data2[i])
##########################################3


#######################################################################################3
#                                  4(a)
########################################################################################
fs = 128
fft_result = np.fft.fft(newd1)
frequencies = np.fft.fftfreq(len(newd1), d=1/fs)


#####################################################
newfaxis=[]
newf=[]
for i in range(64,frequencies.shape[0]):
	newfaxis.append(frequencies[i])
	newf.append(fft_result[i])
for i in range(64):
	newfaxis.append(frequencies[i])
	newf.append(fft_result[i])
#####################################################

# Plot the real part
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.stem(newfaxis, np.real(newf), basefmt=" ", linefmt="C0-", markerfmt="C0o")
plt.title('Real Part of FFT for OFDMRx1')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

# Plot the imaginary part
plt.subplot(2, 1, 2)
plt.stem(newfaxis, np.imag(newf), basefmt=" ", linefmt="C1-", markerfmt="C1o")
plt.title('Imaginary Part of FFT for OFDMRx1')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()
##################################################################

fft_result2 = np.fft.fft(newd2)
frequencies2 = np.fft.fftfreq(len(newd2), d=1/fs)


#####################################################
newfaxis2=[]
newf2=[]
for i in range(64,frequencies2.shape[0]):
	newfaxis2.append(frequencies2[i])
	newf2.append(fft_result2[i])
for i in range(64):
	newfaxis2.append(frequencies2[i])
	newf2.append(fft_result2[i])
#####################################################
# Positive frequencies
#half_length = len(newd1) // 2
#frequencies = frequencies[:half_length]
#fft_result_half = fft_result[:half_length]
#####################################################


# Plot the real part
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.stem(newfaxis2, np.real(newf2), basefmt=" ", linefmt="C0-", markerfmt="C0o")
plt.title('Real Part of FFT for OFDMRx2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

# Plot the imaginary part
plt.subplot(2, 1, 2)
plt.stem(newfaxis2, np.imag(newf2), basefmt=" ", linefmt="C1-", markerfmt="C1o")
plt.title('Imaginary Part of FFT for OFDMRx2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()
##################################################################


#####################################################################################################
#                                      4(b)
######################################################################################################
H1 = []
for i in range(len(newf)):
	if i%2 ==0:
		h1 = newf[i]/(1-3j)
		H1.append(h1)
	else:
		h1 = newf[i]/(3-1j)
		H1.append(h1)
#####################################

print('H1:')
print(H1)


H1abs=[]

for i in range(len(H1)):
	H1abs.append(abs(H1[i]))

plt.figure(figsize=(10, 6))
plt.plot(np.arange(128), H1abs)
plt.title('|Hk1| v.s subcarrier k')
plt.xlabel('subcarrier k')
plt.ylabel('|Hk1|')
plt.grid()
plt.show()
########################################

##########################################################################################################
#                                      4(c)
########################################################################################################
H4us=[]
H4u2s=[]

for i in range(len(newf2)):
	if i%4==0:
		h4u=newf2[i]/(1-3j)
		H4us.append(h4u)

	if i%4 ==2:
		h4u2s=newf2[i]/(3-1j)
		H4u2s.append(h4u2s)
#########################################

H2=[]
########################################3
H4u1s=[]
H4u3s=[]

maxcom=int(len(newf2)/4 )

for j in range((maxcom-1)):
	p1= H4us[j]
	np1=H4us[(j+1)]

	p2= H4u2s[j]
	############################### 
	pj1 = (p1+p2)/2
	pj3 = (p2+np1)/2

	H4u1s.append(pj1)
	H4u3s.append(pj3)
	################################
	H2.append(p1)
	H2.append(pj1)
	H2.append(p2)
	H2.append(pj3)
############################################3

lastp0=H4us[(maxcom-1)]
lastp2=H4u2s[(maxcom-1)]
lastp1= (lastp0 + lastp2)/2
H4u1s.append(lastp1)
#####################################
H2.append(lastp0)
H2.append(lastp1)
H2.append(lastp2)
#######################################

print('H2:')
print(H2)


H2abs=[]
for i in range(len(H2)):
	H2abs.append(abs(H2[i]))



plt.figure(figsize=(10, 6))
plt.plot(np.arange(127), H2abs)
plt.title('|Hk2| v.s subcarrier k')
plt.xlabel('subcarrier k')
plt.ylabel('|Hk2|')
plt.grid()
plt.show()

#################################################################################
#                               (4d)
#################################################################################
Hdiff=[]
for i in range(127):
	diff = H1[i] - H2[i]
	Hdiff.append(abs(diff))

plt.figure(figsize=(10, 6))
plt.plot(np.arange(127), Hdiff)
plt.title('|Hk1 - Hk2| v.s subcarrier k')
plt.xlabel('subcarrier k')
plt.ylabel('|Hk1 - Hk2|')
plt.grid()
plt.show()

print('|Hk1 - Hk2|')
print(Hdiff)
