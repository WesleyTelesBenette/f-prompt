
from src.general.input import Input;

class Program():
	def __init__(self):
		self.main();
    
	def main(self):
		while(True):
			input = Input.get_input()
			Input.input_processing(input)

if (__name__ == '__main__'):
	Program()
