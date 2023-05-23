from src.utils import Pipeline
from dataclasses import dataclass
import pandas as pd


@dataclass
class Sun(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://raw.githubusercontent.com/gperaza/segregation/master/data/Base_SUN_2018.csv"
    file:str = "Base_SUN_2018.csv"
    extract_route:str = ""


    def __preprocessing__(self):
        self.geodata = pd.read_csv(self.__file_data_route__(), encoding='ISO-8859-1')
    
    def __anaylsis__(self):
        self.geodata['CVEGEO'] = self.geodata.apply(lambda x:f"{str(x['CVE_MUN']).zfill(5)}", axis=1)
        self.geodata = self.geodata[['CVE_ENT', 'NOM_ENT', 'NOM_MUN', 'CVE_LOC', 'NOM_LOC', 'CVE_SUN', 'NOM_SUN', 'POB_2018', 'CVEGEO']]

