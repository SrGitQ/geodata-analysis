from src.utils import Pipeline
import geopandas as gpd
import numpy as np
import pandas as pd


class Sun(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://raw.githubusercontent.com/gperaza/segregation/master/data/Base_SUN_2018.csv"
    route:str = "data/Base_SUN_2018.csv"

    def __prepare__(self):
        pass

    def __preprocessing__(self):
        self.geodata = pd.read_csv('data/Base_SUN.csv')

    def __anaylsis__(self):
        pass
