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

	def compare_codes(self, guess_list):
		'''
		Compare the guess colors with the secret code
		and check if the values are the same
		'''
		self.compare_list_position = zip(self.secret_code, guess_list)
		self.no_matches_position_list = []
		self.output_list = []

		self.check_position()
		self.check_value_exist(guess_list)
		self.check_defaul_values()

	def check_position(self):
		for i, z in self.compare_list_position:
			if i == z:
				self.output_list.append(self.color_value("red"))
			else:
				self.no_matches_position_list.append((i, z))

	def check_value_exist(self, guess_list):
		for i, z in self.no_matches_position_list:
			if i in guess_list:
				self.output_list.append(self.color_value("yellow"))

	def check_defaul_values(self):
		while len(self.output_list)<4:
			self.output_list.append(self.color_value("default"))


	def color_value(self, value):
		'''
		The red value is asignated if the position and the
		guess value are the same, if the position is not the same
		but the guess value yes if asignate yellow
		'''

		return {"red": 3, "yellow": 8, "default": 0}.get(value)

	def get_hints(self):
		return self.output_list
