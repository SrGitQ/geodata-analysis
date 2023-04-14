from src.utils import Pipeline
from dataclasses import dataclass
import pandas as pd


@dataclass
class Censo10(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2010/datosabiertos/iter_nal_2010_csv.zip"
    file:str = "ITER_NALCSV10.csv"
    extract_route:str = "data/iter_nal_2010_csv/iter_00_cpv2010/conjunto_de_datos/iter_00_cpv2010.csv"

    def __anaylsis__(self):
        self.geodata['CVE_MUN2010'] = self.geodata['entidad'].str.cat(self.geodata['mun']) 
        self.geodata['CVE_MUN2010'] = pd.to_numeric(self.geodata['CVE_MUN2010'])
        #self.geodata = self.geodata.query("nom_loc == 'Total del Municipio'")
        self.geodata = self.geodata[['nom_mun', 'pobtot', 'CVE_MUN2010']]
        self.geodata = self.geodata.rename(columns={'pobtot': 'POBTOT2010'})

