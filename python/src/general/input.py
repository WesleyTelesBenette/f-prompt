
from src.features.features import Features

class Input():
	@staticmethod
	def get_input():
		comand = input('\n <:: ')
		comand_list = comand.split(' ')
		return comand_list

	@staticmethod
	def input_processing(inputs):
		if (inputs[0] in Features.featurs_list()):
			Features.featur_start(inputs)
		else:
			print('Comand invalid!')
