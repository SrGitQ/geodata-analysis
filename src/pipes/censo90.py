from src.utils import Pipeline
import geopandas as gpd
import numpy as np
import pandas as pd
from src.utils.cords import dms2dd


class Censo90(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/1990/microdatos/iter/00_nacional_1990_iter_txt.zip"
    route:str = "data/ITER_NALTXT90.csv"
    
    def __preprocessing__(self):
        self.geodata = pd.read_csv('data/ITER_NALCSV90.csv', sep="\t" , encoding='latin-1')
        

    def __anaylsis__(self):
        self.geodata['entidad'] = self.geodata['entidad'].astype(str)
        self.geodata['mun'] = self.geodata['mun'].astype(str)
        self.geodata['mun'] = self.geodata['mun'].str.zfill(3)
        self.geodata['CVE_MUN90'] = self.geodata.entidad.str.cat(self.geodata.mun) 
        self.geodata['CVE_MUN90'] = pd.to_numeric(self.geodata['CVE_MUN90'])
        self.geodata = self.geodata.query("nom_loc == 'TOTAL MUNICIPAL'")
        self.geodata = self.geodata[['nom_mun', 'p_total', 'CVE_MUN90']]
        self.geodata = self.geodata.rename(columns={'p_total': 'POBTOT90'})
