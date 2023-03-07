from src.utils import Pipeline
import geopandas as gpd
import numpy as np
import pandas as pd
from src.utils.cords import dms2dd


class Censo20(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2020/microdatos/iter/ITER_NAL_2020_csv.zip"
    route:str = "data/ITER_NALCSV20.csv"
    
    def __preprocessing__(self):
        self.geodata = gpd.read_file('data/ITER_NALCSV20.csv')#Change
        self.geodata = self.geodata.MUN.str.cat(self.geodata.LOC)
        self.geodata = self.geodata[['NOM_LOC', 'POBTOT', 'geometry', 'CVE_MUN']]

    def __anaylsis__(self):
        self.geodata['LATITUD'] = self.geodata['LATITUD'].apply(dms2dd)
        self.geodata['LONGITUD'] = self.geodata['LONGITUD'].apply(dms2dd)
        self.geodata = gpd.GeoDataFrame(self.geodata, geometry=gpd.points_from_xy(self.geodata.LONGITUD, self.geodata.LATITUD))

        print(self.geodata)
