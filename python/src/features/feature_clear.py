
import os
from src.features.i_feature import IFeature

class FeatureClear(IFeature):
    def start(p):
        if (os.name == 'nt'):
            os.system('cls')
        else:
        	os.system('clear')
