import numpy as np
import matplotlib.pyplot as plt
from   pulseshape import pulseshape
from   eyediagram import eyediagram

num = 100
binary = np.sign(np.random.randn(num)) #+ 2.0*np.sign(np.random.randn(num))
M = 100
N = 5
ps_x = np.arange(-N*M,N*M)/float(M)
ps  = np.sinc(ps_x)
plt.figure(1)
plt.plot(ps_x, ps)

msg = pulseshape(binary,M,ps=ps)

plt.figure(2)
eyediagram(msg, M)
plt.show()
