from src.utils import Pipeline
from dataclasses import dataclass
import pandas as pd


@dataclass
class Censo00(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2000/datosabiertos/cgpv2000_iter_00_csv.zip"
    file:str = "ITER_NALCSV00.csv"
    extract_route:str = "data/cgpv2000_iter_00_csv/cgpv2000_iter_00/conjunto_de_datos/cgpv2000_iter_00.csv"

    def __anaylsis__(self):
        self.geodata['CVE_MUN2000'] = self.geodata['entidad'].str.cat(self.geodata['mun']) 
        self.geodata['CVE_MUN2000'] = pd.to_numeric(self.geodata['CVE_MUN2000'])
        self.geodata = self.geodata.query("nom_loc == 'TOTAL MUNICIPAL'")
        self.geodata = self.geodata[['nom_mun', 'p_total', 'CVE_MUN2000']]
        self.geodata = self.geodata.rename(columns={'p_total': 'POBTOT2000'})

