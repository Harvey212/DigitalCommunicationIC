import numpy as np
import matplotlib.pyplot as plt

h0=-0.6275966157352981+0.04201736349919818j
h1=0.5693649212482851+0.3118490684602431j
h2=-0.20218899894622525-0.023609172407679527j
h3=0.11379543934887607-0.3231510642514984j
h4=0.13966486533848485+0.06790215581585504j

D=[0,10,40,80,100]
#################################################
#hh=[h0,h1,h2,h3,h4]
#h = np.array(hh)
#tau = np.array(D)
###################################################

###########################################################################
#frequencies = np.linspace(-100000000, 100000000, 1000)
#omega = 2 * np.pi * frequencies       

# Compute the frequency domain channel response H(ω)
#H = np.zeros_like(omega, dtype=complex)  # Initialize H(ω) as a complex array
#for i in range(len(h)):
#    H += h[i] * np.exp(-1j * omega * tau[i])


####################################################################
# Plot the magnitude and phase of the channel frequency response
#plt.figure(figsize=(12, 6))

# Magnitude plot
#plt.subplot(1, 2, 1)
#plt.plot(frequencies, np.abs(H))
#plt.title('Magnitude of Frequency Response')
#plt.xlabel('Frequency (Hz)')
#plt.ylabel('|H(ω)|')
#plt.grid(True)

# Phase plot
#plt.subplot(1, 2, 2)
#plt.plot(frequencies, np.angle(H))
#plt.title('Phase of Frequency Response')
#plt.xlabel('Frequency (Hz)')
#plt.ylabel('Phase H(ω) (radians)')
#plt.grid(True)

#plt.tight_layout()
#plt.show()
################################################################################



sampling_rate = 200 *pow(10,6)  # Sampling rate in Hz

#sampling_rate = 200e6


#duration = 1  # Duration in seconds
t = np.linspace(0, 1, 101)

# Define delta function positions (e.g., impulses at certain indices)
#delta_positions = D#[100, 300, 500, 700, 900]  # positions of delta functions
signal = np.zeros_like(t, dtype=complex)
#signal[delta_positions] = 1  # Create delta functions (impulses) at these positions
signal[D[0]]=h0
signal[D[1]]=h1
signal[D[2]]=h2
signal[D[3]]=h3
signal[D[4]]=h4







fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)

###################################################################
# Shift zero frequency component to the center
fft_result = np.fft.fftshift(fft_result)
frequencies = np.fft.fftshift(frequencies)

# Limit frequency range to -100 MHz to 100 MHz
freq_range = (-100e6, 100e6)
mask = (frequencies >= freq_range[0]) & (frequencies <= freq_range[1])

# Plot magnitude spectrum
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(frequencies[mask], np.abs(fft_result[mask]) / len(signal))
plt.title("Magnitude Spectrum within -100 MHz to 100 MHz")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

# Plot phase spectrum
plt.subplot(2, 1, 2)
plt.plot(frequencies[mask], np.angle(fft_result[mask]))
plt.title("Phase Spectrum within -100 MHz to 100 MHz")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (Radians)")
plt.tight_layout()
plt.show()


