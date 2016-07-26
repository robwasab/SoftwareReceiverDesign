import numpy as np
import itertools

def letters2pam(s):
	return list(itertools.chain(*[[int(pair[0] + pair[1],2)*2-3 for pair in np.reshape(list('{:08b}'.format(ord(c))),(4,2))]  for c in s]))

def educational():
	s = 'dead'
	print ['{:08b}'.format(ord(c)) for c in s ]
	# >>
	# ['01100100', '01100101', '01100001', '01100100']

	print [list('{:08b}'.format(ord(c))) for c in s ]
	# >>
	# [['0', '1', '1', '0', '0', '1', '0', '0'], 
	#  ['0', '1', '1', '0', '0', '1', '0', '1'], 
	#  ['0', '1', '1', '0', '0', '0', '0', '1'], 
	#  ['0', '1', '1', '0', '0', '1', '0', '0']]
	
	print [np.reshape(list('{:08b}'.format(ord(c))),(4,2)).tolist() for c in s ]
	# >>
	# [[['0', '1'], 
	#   ['1', '0'], 
	#   ['0', '1'], 
	#   ['0', '0']], 
	#  [['0', '1'], 
	#   ['1', '0'],
	#   ['0', '1'], 
	#   ['0', '1']], 
	#  [['0', '1'], 
	#   ['1', '0'], 
	#   ['0', '0'], 
	#   ['0', '1']], 
	#  [['0', '1'], 
	#   ['1', '0'], 
	#   ['0', '1'], 
	#   ['0', '0']]]

	print [[''.join(pair) for pair in np.reshape(list('{:08b}'.format(ord(c))),(4,2)).tolist()] for c in s ]
	# >>
	# [['01', '10', '01', '00'], ['01', '10', '01', '01'], ['01', '10', '00', '01'], ['01', '10', '01', '00']]
	
	# convert each bit pair to a decimal number, these will represent amplitudes
	print [[int(''.join(pair),2) for pair in np.reshape(list('{:08b}'.format(ord(c))),(4,2)).tolist()] for c in s ]
	# >>
	# [[1, 2, 1, 0], [1, 2, 1, 1], [1, 2, 0, 1], [1, 2, 1, 0]]

	# shift and scale each number to -3, -1, 1, 3
	print [[int(''.join(pair),2)*2-3 for pair in np.reshape(list('{:08b}'.format(ord(c))),(4,2)).tolist()] for c in s ]
	# >>
	# [[-1, 1, -1, -3], [-1, 1, -1, -1], [-1, 1, -3, -1], [-1, 1, -1, -3]]

	# combine all the elements into one list with itertools
	import itertools
	print list(itertools.chain(*[[int(''.join(pair),2)*2-3 for pair in np.reshape(list('{:08b}'.format(ord(c))),(4,2)).tolist()] for c in s ]))
	# >>
	# [-1, 1, -1, -3, -1, 1, -1, -1, -1, 1, -3, -1, -1, 1, -1, -3]
	
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
if __name__ == '__main__':
	test()
	educational()
