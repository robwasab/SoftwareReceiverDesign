from pulseshape import pulseshape
from letters2pam import letters2pam

if __name__ == '__main__':
	pulseshape(letters2pam('hell'), 101, debug=True)
