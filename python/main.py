
from src.general.input import Input

class Program():
	def __init__(self):
		self.main()
    
	def main(self):
		while(True):
			inputs = Input.get_input()
			Input.input_processing(inputs)

if (__name__ == '__main__'):
	Program()
