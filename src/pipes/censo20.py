from src.utils import Pipeline
from dataclasses import dataclass
import pandas as pd
from src.utils import dms2dd


@dataclass
class Censo20(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2020/microdatos/iter/ITER_NAL_2020_csv.zip"
    file:str = "ITER_NALCSV20.csv"
    extract_rolse:str = "data/ITER_NAL_2020_csv/ITER_NALCSV20.csv"

    def __preprocessing__(self):
        self.geodata = pd.read_csv(self.__file_data_route__(), encoding='UTF-8-SIG')

    def __anaylsis__(self):
        self.geodata = self.geodata[['ENTIDAD', 'NOM_ENT', 'MUN', 'NOM_MUN', 'LOC', 'NOM_LOC', 'POBTOT', 'LONGITUD', 'LATITUD']]
        self.geodata['LATITUD'] = self.geodata['LATITUD'].fillna(method='backfill')
        self.geodata['LONGITUD'] = self.geodata['LONGITUD'].fillna(method='backfill')
        self.geodata.columns = ['entidad', 'nom_ent', 'mun', 'nom_mun', 'loc', 'nom_loc', 'p_total', 'longitud', 'latitud']
        self.geodata = self.geodata.query('nom_loc.str.contains("Total del Municipio")')
        self.geodata['CVEGEO'] = self.geodata.apply(lambda x:f'{str(x["entidad"]).zfill(2)}{str(x["mun"]).zfill(3)}', axis=1)
        self.geodata = self.geodata[['CVEGEO', 'p_total', 'longitud', 'latitud']]
        self.geodata.columns = ['CVEGEO', 'P_TOTAL_2020', 'LONGITUD', 'LATITUD']
        self.geodata.drop_duplicates(subset=['CVEGEO'], inplace=True)
        self.geodata['LATITUD'] = self.geodata['LATITUD'].apply(dms2dd)
        self.geodata['LONGITUD'] = self.geodata['LONGITUD'].apply(dms2dd)

        """
        self.geodata['CVE_MUN2020'] = self.geodata['ENTIDAD'].str.cat(self.geodata['MUN']) 
        self.geodata = self.geodata[['NOM_MUN', 'NOM_LOC', 'POBTOT', 'geometry', 'CVE_MUN2020', 'LATITUD', 'LONGITUD']]
        self.geodata = self.geodata.rename(columns={'POBTOT': 'POBTOT2020'})
        self.geodata = self.geodata[self.geodata['NOM_LOC'].str.contains("Localidades de una vivienda")==False]
        self.geodata = self.geodata[self.geodata['NOM_LOC'].str.contains("Localidades de dos viviendas")==False]

        n = 2
        # Using DataFrame.tail() to Drop top two rows
        self.geodata = self.geodata.tail(self.geodata.shape[0]-n)

        self.geodata['LATITUD'] = self.geodata['LATITUD'].apply(dms2dd)
        self.geodata['LONGITUD'] = self.geodata['LONGITUD'].apply(dms2dd)

        self.geodata['LATITUD'] = self.geodata['LATITUD'].fillna(method='backfill')
        self.geodata['LONGITUD'] = self.geodata['LONGITUD'].fillna(method='backfill')

        self.geodata = self.geodata.query("NOM_LOC == 'Total del Municipio'")
        """

