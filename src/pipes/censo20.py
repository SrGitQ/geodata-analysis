from src.utils import Pipeline
from dataclasses import dataclass


@dataclass
class Censo20(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2020/microdatos/iter/ITER_NAL_2020_csv.zip"
    file:str = "ITER_NALCSV20.csv"
    extract_route:str = "data/ITER_NAL_2020_csv/ITER_NALCSV20.csv"

    def __anaylsis__(self):
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

