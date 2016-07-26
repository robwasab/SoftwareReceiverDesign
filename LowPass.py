import numpy as np

class LowPass(object):
	def __init__(self, fc, fs, Q = 0.7071):
		#Biquad filter
		self.a0 = self.a1 = self.a2 = 0
		self.b0 = self.b1 = self.b2 = 0
		self.x1 = self.x2 = 0
		self.y1 = self.y2 = 0
		A = 1.0
		omega = 2.0*np.pi*fc/fs
		sn = np.sin(omega)
		cs = np.cos(omega)
		alpha = sn / (2.0*Q)
		beta  = np.sqrt(A+A)
		self.init_lp(A, omega, sn, cs, alpha, beta)
		self.b0 /= self.a0
		self.b1 /= self.a0
		self.b2 /= self.a0
		self.a1 /= self.a0
		self.a2 /= self.a0

	def init_lp(self, A, omega, sn, cs, alpha, beta):
		self.b0 = (1.0 - cs) / 2.0
		self.b1 =  1.0 - cs
		self.b2 = (1.0 - cs) / 2.0
		self.a0 =  1.0 + alpha
		self.a1 = -2.0 * cs
		self.a2 =  1.0 - alpha
	
	def work(self, x):
		y = self.b0 * x + self.b1 * self.x1 + self.b2 * self.x2 - self.a1 * self.y1 - self.a2 * self.y2
		self.x2, self.x1 = self.x1, x
		self.y2, self.y1 = self.y1, y
		return y
