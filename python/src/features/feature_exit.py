
from src.features.feature_clear import FeatureClear
from src.features.i_feature import IFeature

class FeatureExit(IFeature):
	def start(p):
		FeatureClear().start(p)
		exit()
