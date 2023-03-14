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
        self.geodata = gpd.read_file('data/ITER_NALCSV20.csv', encoding='utf-8')

    def __anaylsis__(self):
        self.geodata['CVE_MUN2020'] = self.geodata.ENTIDAD.str.cat(self.geodata.MUN) 
        self.geodata = self.geodata[['NOM_MUN', 'NOM_LOC', 'POBTOT', 'geometry', 'CVE_MUN2020', 'LATITUD', 'LONGITUD']]
        self.geodata = self.geodata.rename(columns={'POBTOT': 'POBTOT2020'})
        self.geodata = self.geodata[self.geodata['NOM_LOC'].str.contains("Localidades de una vivienda")==False]
        self.geodata = self.geodata[self.geodata['NOM_LOC'].str.contains("Localidades de dos viviendas")==False]
