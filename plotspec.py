import numpy as np
from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt

def plotspec(data, ts):
	fft_data = fft(data)
	fft_axis = fftfreq(len(data))
	plt.subplot(311)
	plt.plot(np.arange(0, len(data))*ts, data)
	plt.title('Time Domain')
	plt.ylabel('Amplitude')
	plt.subplot(312)
	plt.plot(fft_axis, np.abs(fft_data))
	plt.title('Magnitude')
	plt.subplot(313)
	plt.plot(fft_axis, np.angle(fft_data)/np.pi)
	plt.ylabel('Phase/pi')
	plt.title('Phase')
	plt.show(block = False)

def test():
	times = np.arange(0,1024)*1.0/44.1E3
	signal = np.sin(2*np.pi*44.1E3/44.0*times)
	plotspec(signal, 1.0/44.1E3)

if __name__ == '__main__':
	test()
