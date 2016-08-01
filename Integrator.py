class Integrator(object):
	def __init__(self, ki = 1):
		self.lasty = 0
		self.ki = ki
		self.lastx = 0

	def value(self):
		return self.lasty

	def work(self, input):
		y = self.ki*self.lastx + self.lasty
		self.lasty = y
		self.lastx = input
		return y
