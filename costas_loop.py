from scipy.signal import firwin
from letters2pam import letters2pam
import numpy as np
from numpy import pi
from plotspec import plotspec
from pulseshape import pulseshape
import matplotlib.pyplot as plt
from LowPass import LowPass
from Integrator import Integrator

def costa_lp_filter_sim():
	M = 101;
	fs = 44.1E3;
	msg = letters2pam('dead beef')
	baseband = pulseshape(msg, M)
	times = np.arange(0,len(baseband))/fs
	fc = fs/4.0
	tx = np.cos(2.0*pi*fc*times)*baseband
	#plotspec(tx, 1.0/fs, True)

	in_phase_lp = LowPass(1E3, fs)
	qu_phase_lp = LowPass(1E3, fs)
	in_phase_out = np.zeros(len(tx))
	qu_phase_out = np.zeros(len(tx))
	phases = np.zeros(len(tx))
	mu = 0.01

	vco_phase_integrator = Integrator(2.0*pi*(fc-5)/fs)

	for phase_off in np.arange(8, -1, -1)*pi/8.0:
	
		for n in range(0, len(tx)-1):
			t = times[n]
			#vco_phase = 2.0*np.pi*fc*t
			vco_phase = vco_phase_integrator.work(1.0)
			in_vco = 2.0*np.cos(vco_phase - phase_off + phases[n])
			qu_vco = 2.0*np.sin(vco_phase - phase_off + phases[n])
			in_phase_out[n] = in_phase_lp.work(in_vco*tx[n])
			qu_phase_out[n] = qu_phase_lp.work(qu_vco*tx[n])
			phases[n+1] = phases[n] - mu*in_phase_out[n]*qu_phase_out[n]

		plt.figure(1)
		plt.subplot(311)
		plt.title('Phase: %.3f'%(phase_off/pi))
		plt.plot(times, baseband)
		plt.ylim([-3, 3])
		plt.subplot(312)
		plt.plot(times, in_phase_out)	
		plt.ylim([-3, 3])
		plt.subplot(313)
		plt.plot(times, qu_phase_out)
		plt.ylim([-3, 3])
		plt.show(block = True)
if __name__ == '__main__':
	costa_lp_filter_sim()
