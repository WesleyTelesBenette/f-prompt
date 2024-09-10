
from src.features.feature_clear import FeatureClear
from src.features.feature_exit import FeatureExit

class Features():
	__features_map = {
        'clear': FeatureClear,
        'cls': FeatureClear,
		'exit': FeatureExit
	}

	@staticmethod
	def features_list():
		return list(Features.__features_map.keys())

	@staticmethod
	def featur_start(inputs):
		Features.__features_map[inputs[0]].start(inputs[1:])
