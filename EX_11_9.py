# Excercise 11.9
# Consider the baseband communication system in Figure 11.9
# The difference equation relating the symbols m[k] to the 
# T-spaced equalizer input u[k] for the chosen baud-timing 
# factor epsilon is
#
# u[k] = 0.04m[k-p] + 1.00m[k-1-p] + 0.60m[k-2-p] + 0.38m[k-3-p]
# where p is a nonnegative integer. 
#
# The equalizer is given by
# y[k] = u[k] + alpha*u[k-1]
#
# Suppose alpha = -0.4 and the message source is binary +/-. 
# Is the system from the source symbols m[k] to the equalizer
# output y[k] open-eye?

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from pulseshape import pulseshape
from eyediagram import eyediagram
from plotspec import plotspec

p = 33
channel_b   = [0.0]*p + [0.04, 1., 0.6, 0.38]

equalizer_b = [1, -0.4]

combined_b  = signal.convolve(channel_b, equalizer_b)

channel_w,   channel_H   = signal.freqz(channel_b)
equalizer_w, equalizer_H = signal.freqz(equalizer_b)
combined_w,  combined_H  = signal.freqz(combined_b)

plt.figure(1)

plt.subplot(311)
plt.plot(channel_w/np.pi, abs(channel_H))

plt.subplot(312)
plt.plot(equalizer_w/np.pi, abs(equalizer_H))

plt.subplot(313)
plt.plot(combined_w/np.pi, abs(combined_H))

num = 100
binary = np.sign(np.random.randn(num)) + 2.0*np.sign(np.random.randn(num))
M = 100 
msg = pulseshape(binary,M)

out = signal.convolve(combined_b, msg)
plt.figure(2)
plotspec(out)

plt.figure(3)
eyediagram(out, M)


#eyediagram(signal, M)

	


plt.show()
