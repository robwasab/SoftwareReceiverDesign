from scipy.signal import convolve, hamming
import numpy as np
import matplotlib.pyplot as plt
import pdb
from letters2pam import letters2pam
from LowPass import LowPass

def pulseshape(signal, M, debug = False):
	mup = np.zeros(M*len(signal))
        mup[np.arange(0,len(mup),M)] = signal	
	mup_analog = convolve(hamming(M), mup)

	if debug:
		plt.subplot(311)
		plt.stem(signal)
		plt.title('Data Sequence')
		plt.subplot(312)
		plt.plot(mup)
		plt.title('Oversampling')
		plt.subplot(313)
		plt.plot(mup_analog)
		plt.title('Convolution with Pulse Shape')
		plt.show(block=True)
	return mup_analog

if __name__ == '__main__':
	pulseshape(letters2pam('hell'), 101, True)
