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

    def __preprocessing__(self):
        self.geodata = pd.read_csv(self.__file_data_route__(), encoding='UTF-8-SIG')

    def __anaylsis__(self):
        self.geodata = self.geodata.rename(columns={'pobtot':'p_total'})
        self.geodata = self.geodata[['entidad', 'nom_ent', 'mun', 'nom_mun', 'loc', 'nom_loc', 'p_total']]
        self.geodata = self.geodata.query('nom_loc.str.contains("Total del Municipio")')
        self.geodata['CVEGEO'] = self.geodata.apply(lambda x:f'{str(x["entidad"]).zfill(2)}{str(x["mun"]).zfill(3)}', axis=1)
        self.geodata = self.geodata[['CVEGEO', 'p_total']]
        self.geodata.columns = ['CVEGEO', 'P_TOTAL_2010']
        self.geodata.drop_duplicates(subset=['CVEGEO'], inplace=True)

        """
        self.geodata['CVE_MUN2010'] = self.geodata['entidad'].str.cat(self.geodata['mun']) 
        self.geodata['CVE_MUN2010'] = pd.to_numeric(self.geodata['CVE_MUN2010'])
        #self.geodata = self.geodata.query("nom_loc == 'Total del Municipio'")
        self.geodata = self.geodata[['nom_mun', 'pobtot', 'CVE_MUN2010']]
        self.geodata = self.geodata.rename(columns={'pobtot': 'POBTOT2010'})
        """

