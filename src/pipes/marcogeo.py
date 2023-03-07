from src.utils import Pipeline
from src.utils.files import rm_file, unzip_file
import geopandas as gpd
import numpy as np
import pandas as pd


class Marcogeo(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463807469/mg_2020_integrado.zip"
    route:str = "data/conjunto_de_datos"

    def __prepare__(self):
        try:
            unzip_file(self.name)
            rm_file(self.name)
        except:
            pass

    def __preprocessing__(self):
        self.geodata = gpd.read_file('data/conjunto_de_datos/00mun.shp')

    def __anaylsis__(self):
        self.geodata['CVEGEO'] = pd.to_numeric(self.geodata['CVEGEO'])
