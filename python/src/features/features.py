
from src.features.feature_clear import FeatureClear
from src.features.feature_exit import FeatureExit

class Features():
	__featurs_map = {
        'clear': FeatureClear,
		'exit': FeatureExit
	}

	@staticmethod
	def featurs_list():
		return list(Features.__featurs_map.keys())

	@staticmethod
	def featur_start(inputs):
		Features.__featurs_map[inputs[0]].start(inputs[1:])
