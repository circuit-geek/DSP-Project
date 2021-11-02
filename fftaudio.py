import scipy.io.wavfile as wavfile
from scipy.fft import fft
import scipy.fftpack as fftpk
import numpy as np
import matplotlib.pyplot as plt
s_rate, signal = wavfile.read("PinkPanther30.wav")

#in time domain
duration = len(signal)/s_rate
time = np.arange(0, duration, 1/s_rate)
plt.plot(time,signal)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()

#in frequency domain
FFT = abs(fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))
plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()