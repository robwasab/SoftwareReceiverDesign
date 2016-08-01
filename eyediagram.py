from   pulseshape  import pulseshape
import matplotlib.pyplot as plt
import numpy as np
import pdb
def eyediagram(data, M, symbols = 2):
	reverse = -(len(data) % (symbols*M))
	data = data[: reverse]
	rows = len(data)/(M*symbols)
	data = np.reshape(data, (rows, M*symbols))
	for data_row in data:
		plt.plot(data_row, color='blue')

	plt.xlim([0, M*symbols-1])

def test():
	binary = np.sign(np.random.randn(20))
	M = 100 
	signal = pulseshape(binary,M)
	noise  = 0.5*np.random.randn(len(signal))
	signal+= noise
	#pdb.set_trace()
	eyediagram(signal, M)
	plt.show(block = True)

if __name__ == '__main__':
	test()
