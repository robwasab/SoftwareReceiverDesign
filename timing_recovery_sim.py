import matplotlib.pyplot as plt
import numpy as np
from   scipy import convolve
from   letters2pam import letters2pam
from   pulseshape import pulseshape
from   pulseshape import srrc
from   sys import float_info
import pdb

def quantize(x, alphabet = [-3, -1, 1, 3]):
	least_error = float_info.max
	closest = alphabet[0]

	for letter in alphabet:
		error = letter - x
		error*= error
		if error < least_error:
			closest = letter
			least_error = error
	return closest

# oversampling factor
M = 100 

# srrc 
beta = 0.5

pam = letters2pam("synchonize synchornize synchornize synchornize synchronize synchronize synchronize synchronize synchronize synchronize synchronize synchronize synchronize synchronize synchronize synchronize hello world timing synchronization hello world") 
tx, matched_filter = pulseshape(pam, M, beta = 0.5, return_filter = True)

# channel impulse response
channel = 1

# receive side
rx = convolve(matched_filter, tx)

sample_offset = M * np.random.rand() 
down_sample   = np.zeros(int(len(rx)/M))
taus = np.zeros(int(len(rx)/M))

u = M 
k = 0
tau = 0
m_integrator = 0

while True:
	n = round(m_integrator + tau) + sample_offset
	if n >= len(rx) - 1:
		break

	m_integrator += M

	down_sample[k] = rx[n]
	taus[k] = tau
	k += 1

	if k > len(taus) - 1:
		break
	derivative = (quantize(rx[n]) - rx[n]) 
	derivative *= (rx[n+1] - rx[n-1])
	tau = tau + u * derivative 
	print tau
	
plt.figure(1)
plt.plot(rx)

plt.figure(2)
plt.stem(down_sample)

plt.figure(3)
plt.plot(taus)
plt.show()
