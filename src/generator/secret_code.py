#! /usr/bin/env python
import random

class SecretCode(object):
	def __init__(self):
		self.secret_code = self.generate_secret_code()

	def generate_secret_code(self):
		code = []
		for id_colors in range(4):
			code.append(random.randint(0, 7))

		return code

	def get_secret_code(self):
		return self.secret_code

	def compare_codes(self, anotherlist):
		for i in self.secret_code:
			for z in anotherlist:
				if i == z:
					print z