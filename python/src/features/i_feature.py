
from abc import ABC, abstractmethod

class IFeature(ABC):
	@abstractmethod
	def start(parameters = []):
		pass
