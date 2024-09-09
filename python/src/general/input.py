
from src.featurs.featurs import Featurs

class Input():
	@staticmethod
	def get_input():
		comand = input('\n <:: ')
		comand_list = comand.split(' ')
		return comand_list

	@staticmethod
	def input_processing(inputs):
		if (inputs[0] in Featurs.featurs_list()):
			pass
		else:
			print('Comand invalid!')
