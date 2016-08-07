from   scipy.signal import convolve, hamming
import numpy as np
from   numpy import sqrt, power, sin, cos, pi
import matplotlib.pyplot as plt
import pdb
from   letters2pam import letters2pam
from   LowPass import LowPass

def pulseshape(signal, M, **varargin):
	debug = False
	ps = hamming(M)
	#SRRC variables
	beta = -1
	symbol_delay = 3
	return_filter = False

	for key in varargin:
		if key == 'debug':
			debug = varargin[key]
		elif key == 'ps':
			ps = varargin[key]
		elif key == 'beta':
			beta = float(varargin[key])
		elif key == 'symbol_delay':
			symbol_delay = int(varargin[key])
		elif key == 'return_filter' or key == 'return_ps':
			return_filter = True
	if beta != -1:
		ps = srrc(symbol_delay, beta, M)

	mup = np.zeros(M*len(signal))
        mup[np.arange(0,len(mup),M)] = signal	
	mup_analog = convolve(ps, mup)

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
	
	if return_filter:
		return (mup_analog, ps)
	return mup_analog

# Ported from MATLAB Software Receiver Design
def srrc(syms, beta, P, t_off = 0):
	# Generate a Square-Root Raised Cosine Pulse
	# 'syms' is 1/2 the length of srrc pulse in symbol durations
	# 'beta' is the rolloff factor: beta=0 gives the sinc function
	# 'P' is the oversampling factor
	# 't_off' is the phase (or timing) offset
	# sampling indices as a multiple of T/P
	k=np.arange(-syms*P+1e-8+t_off,syms*P+1e-8+t_off+1);           
	if beta == 0:
		beta=1e-8 # numerical problems if beta=0

	P = float(P)
	s = 4.0*beta/sqrt(P)*(cos((1.0+beta)*pi*k/P) + sin((1.0-beta)*pi*k/P) / (4.0*beta*k/P)) / (pi*(1.0-16.0*power(beta*k/P,2.0)))
	return s

if __name__ == '__main__':
	plt.figure(1)
	pulseshape(letters2pam('hell'), 101, debug = True, beta = 0.5)

