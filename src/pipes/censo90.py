from src.utils import Pipeline
from dataclasses import dataclass
import pandas as pd


@dataclass
class Censo90(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/1990/microdatos/iter/00_nacional_1990_iter_txt.zip"
    file:str = "ITER_NALTXT90.csv"
    extract_route:str = "data/00_nacional_1990_iter_txt/ITER_NALTXT90.txt"
    

    def __anaylsis__(self):
        self.geodata['entidad'] = self.geodata['entidad'].astype(str)
        self.geodata['mun'] = self.geodata['mun'].astype(str)
        self.geodata['mun'] = self.geodata['mun'].str.zfill(3)
        self.geodata['CVE_MUN90'] = self.geodata['entidad'].str.cat(self.geodata['mun']) 
        self.geodata['CVE_MUN90'] = pd.to_numeric(self.geodata['CVE_MUN90'])
        self.geodata = self.geodata.query("nom_loc == 'TOTAL MUNICIPAL'")
        self.geodata = self.geodata[['nom_mun', 'p_total', 'CVE_MUN90']]
        self.geodata = self.geodata.rename(columns={'p_total': 'POBTOT90'})
