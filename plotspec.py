import numpy as np
from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt

def plotspec(data, ts = 1, block = False):
	data = data[:-1]
	fft_data = fft(data)/float(len(data))
	fft_axis = fftfreq(len(data))
	plt.subplot(311)
	plt.plot(np.arange(0, len(data))*ts, data)
	plt.title('Time Domain')
	plt.ylabel('Amplitude')
	plt.subplot(312)
	plt.plot(fft_axis, np.abs(fft_data))

	fft_lim = fft_axis[ np.array([-1,0])+(len(fft_axis)+1)/2]

	plt.xlim(fft_lim)
	plt.title('Magnitude')
	plt.subplot(313)
	plt.plot(fft_axis, np.angle(fft_data)/np.pi)
	plt.xlim(fft_lim)
	plt.ylabel('Phase/pi')
	plt.title('Phase')
	plt.show(block = block)

def test():
	times = np.arange(0,1024)*1.0/44.1E3
	signal = np.sin(2*np.pi*44.1E3/44.0*times)
	plotspec(signal, 1.0/44.1E3)

if __name__ == '__main__':
	test()
