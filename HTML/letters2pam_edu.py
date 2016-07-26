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
