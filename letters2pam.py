import numpy as np
import itertools

def letters2pam(s):
	return list(itertools.chain(*[[int(pair[0] + pair[1],2)*2-3 for pair in np.reshape(list('{:08b}'.format(ord(c))),(4,2))]  for c in s]))

def test():
	tests ={'dead': [-1, 1, -1, -3, -1, 1, -1, -1, -1, 1, -3, -1, -1, 1, -1, -3], \
		'DEAD': [-1, -3, -1, -3, -1, -3, -1, -1, -1, -3, -3, -1, -1, -3, -1, -3],\
		'beef': [-1, 1, -3, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1],\
		'BEEF': [-1, -3, -3, 1, -1, -3, -1, -1, -1, -3, -1, -1, -1, -3, -1, 1] }

	for test in tests:
		try:
			assert(tests[test] == letters2pam(test))
		except Exception as e:
			print test
			raise e
if __name__ == '__name__':
	test()
