from numpy import sin,cos,pi,arctan
from Integrator import Integrator
import numpy as np
from scipy import signal
from LowPass import LowPass

class PLL(object):
	def __init__(self, k1=2.0/3.0, k2=1.0/16.0, k3=1.0/32.0, fc = 5E3, fs = 44.1E3):
		self.k1 = k1
		self.k2 = k2
		self.k3 = k3
		self.integrator1 = Integrator()
		self.integrator2 = Integrator()
		self.vco_integrator = Integrator()
		self.ilp = LowPass(1E3, fs)
		self.qlp = LowPass(1E3, fs)
		self.F = fc/fs
		self.mu = 0.01
		self.costa_phase = Integrator()

	def work(self, input):
		cos_vco = cos(self.vco_integrator.value() + self.costa_phase.value())
		sin_vco = sin(self.vco_integrator.value() + self.costa_phase.value())
		
		#COSTA SECTION
		in_phase = self.ilp.work(sin_vco*input)
		qu_phase = self.qlp.work(cos_vco*input)
		phase_adj = -self.mu * in_phase * qu_phase
		self.costa_phase.work(phase_adj)

		#PLL SECTION
		pll_error = input * cos_vco
		s1 = pll_error
		s3 = self.k1*s1 + self.integrator1.work(s1*self.k1*self.k2+self.integrator2.work(s1*self.k1*self.k2*self.k3))
		self.vco_integrator.work(s3 + 2.0*pi*self.F)
		return (cos_vco, pll_error, in_phase, qu_phase, self.costa_phase.value())
	
