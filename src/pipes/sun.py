from src.utils import Pipeline
import geopandas as gpd
import numpy as np
import pandas as pd


class Sun(Pipeline):
    """
    """
    def __prepare__(self):
        pass

    def __preprocessing__(self):
        self.geodata = pd.read_csv('data/Base_SUN.csv')

    def __anaylsis__(self):
        pass
