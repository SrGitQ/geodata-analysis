from src.utils import Pipeline
import geopandas as gpd
import numpy as np
import pandas as pd
from src.utils.cords import dms2dd


class Censo10(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2010/microdatos/iter/00_nacional_2010_iter_dbf.zip"
    route:str = "data/ITER_NALDBF10.dbf"
    
    def __preprocessing__(self):
        self.geodata = gpd.read_file('data/ITER_NALDBF10.dbf', encoding='utf-8')

    def __anaylsis__(self):
        self.geodata['CVE_MUN2010'] = self.geodata.entidad.str.cat(self.geodata.mun) 
        self.geodata['CVE_MUN2010'] = pd.to_numeric(self.geodata['CVE_MUN2010'])
        self.geodata = self.geodata.query("nom_loc == 'Total del Municipio'")
        self.geodata = self.geodata[['nom_mun', 'pobtot', 'CVE_MUN2010']]
        self.geodata = self.geodata.rename(columns={'pobtot': 'POBTOT2010'})
