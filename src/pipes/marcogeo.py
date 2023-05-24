from src.utils import Pipeline
from dataclasses import dataclass
import geopandas as gpd
import shutil


@dataclass
class Marcogeo(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463807469/mg_2020_integrado.zip"
    file:str = "00mun.shp"
    extract_route:str = "data/mg_2020_integrado/conjunto_de_datos/00mun.shp"

    # def __mv_file_from_source__(self):
    #     super().__mv_file_from_source__() 
    #     shutil.move(self.extract_route.replace('.shx', '.shp'), self.__file_data_route__().replace('.shx', '.shp'))

    def __preprocessing__(self):
        self.geodata = gpd.read_file(self.__file_data_route__(), encoding='utf-8')
        self.geodata.crs = "MEXICO_ITRF_2008_LCC"
        self.geodata = self.geodata.to_crs("ESRI:54009")
 
    def __anaylsis__(self):
        pass

