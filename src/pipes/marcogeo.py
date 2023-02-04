from src.utils import Pipeline
from src.utils.files import unzip_file
import geopandas as gpd
import numpy as np
import pandas as pd


class Marcogeo(Pipeline):
    """
    """
    def __prepare__(self):
        try:
            unzip_file(self.name)
            rm_file(self.name)
        except:
            pass

    def __preprocessing__(self):
        pass

    def __anaylsis__(self):
        pass
