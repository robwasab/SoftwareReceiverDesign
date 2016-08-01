from   scipy.signal import firwin
from   letters2pam import letters2pam
import numpy as np
from   numpy import pi
from   plotspec import plotspec
from   pulseshape import pulseshape
import matplotlib.pyplot as plt
from   PLL import PLL

def costa_lp_filter_sim():
	M = 101;
	fs = 44.1E3;
	msg = letters2pam('dead beef')
	baseband = pulseshape(msg, M)
	times = np.arange(0,len(baseband))/fs
	fc = fs/4.0
	tx = np.cos(2.0*pi*fc*times)*baseband
	pll = PLL()
	in_phase = np.zeros(len(tx))
	qu_phase = np.zeros(len(tx))
	cos_vco  = np.zeros(len(tx))
	for phase_off in np.arange(8, -1, -1)*pi/8.0:
	
		for n in range(0, len(tx)-1):
			signal = np.cos(2.0*pi*fc*times[n]+phase_off)*baseband[n]
			cos_vco[n], pll_error, in_phase[n], qu_phase[n], costa_phase = pll.work(signal)
			
		plt.figure(1)
		plt.subplot(411)
		plt.title('Phase: %.3f'%(phase_off/pi))
		plt.plot(times, baseband)
		plt.ylim([-3, 3])
		plt.subplot(412)
		plt.plot(times, in_phase)	
		plt.ylim([-3, 3])
		plt.subplot(413)
		plt.plot(times, qu_phase)
		plt.ylim([-3, 3])
		plt.subplot(414)
		plt.plot(times, cos_vco)

		plt.show(block = True)
if __name__ == '__main__':
	costa_lp_filter_sim()
