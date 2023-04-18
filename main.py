from src.utils import Pipeline
from src.pipes import Censo90, Censo00, Censo10, Censo20, Marcogeo, Sun
from multiprocessing import Pool
import geopandas as gpd
import pandas as pd
from src.utils.files import auxiliar_files
import os
import shutil

def process(source):
    source.run()

class Analysis(Pipeline):
    """
        Analysis
    """
    geodata= {}

    def __parallel_process__(self):
        self.sources = {
            #"censo_1990" : Censo90(),
            #"censo_2000" : Censo00(),
            #"censo_2010" : Censo10(),
            #"censo_2020" : Censo20(),
            "marcogeo" : Marcogeo(),
            "sun" : Sun()
        }
        for source in self.sources:
            self.sources[source].run()
            #print(self.sources[source].geodata)
        # with Pool(len(self.sources)) as p:
        #     p.map(process, self.sources)

    
    def __prepare__(self):
        
        names = os.listdir('data')
        for name in names:
            if '.txt' in name:
                os.rename('data/'+name, 'data/'+name.replace('.txt', '.csv'))
            if '.csv' not in name and not '.shx' in name and not '.shp' in name:
                print('removing the file: ', name)
                try:
                    os.remove('data/'+name)
                except:
                    shutil.rmtree('data/'+name)
                else:
                    pass
        

    def __anaylsis__(self):
        print(self.sources["marcogeo"].geodata, self.sources["sun"].geodata)
        self.geodata = pd.merge(self.sources["marcogeo"].geodata, self.sources["sun"].geodata, left_on = 'CVEGEO', right_on = 'CVE_MUN')
        #self.geodata = pd.merge(self.sources["censo_1990"].geodata, self.geodata, how = "right", left_on = 'CVE_MUN90', right_on = 'CVEGEO')
        #self.geodata = pd.merge(self.sources["censo_2000"].geodata, self.geodata, how = "right", left_on = 'CVE_MUN2000', right_on = 'CVEGEO')
        #self.geodata = pd.merge(self.sources["censo_2010"].geodata, self.geodata, how = "right", left_on = 'CVE_MUN2010', right_on = 'CVEGEO')
        #self.geodata = pd.merge(self.sources["censo_2020"].geodata, self.geodata, how = "right", left_on = 'CVE_MUN2020', right_on = 'CVEGEO')
#, 'POBTOT90', 'POBTOT2000', 'POBTOT2010', 'POB_2018', 'POBTOT2020'
        self.geodata = self.geodata[['CVEGEO','nom_mun', 'geometry_y', 'LATITUD', 'LONGITUD','CVE_SUN', 'NOM_SUN']]

        self.geodata = gpd.GeoDataFrame(self.geodata, geometry='geometry_y')

        convert_dict = {
            'POBTOT90': float,
            'POBTOT2000': float,
            'POBTOT2010': float,
            'POBTOT2020': float,
        }
 
        #self.geodata = self.geodata.astype(convert_dict)

        with open('municipios.geojson' , 'w') as file:
            file.write(self.geodata.to_json()) #pylint: disable=no-data-type

    def run(self):
        # Check if the data file is already created or it need to be created
        auxiliar_files()
        self.__parallel_process__()
        self.__prepare__()
        self.__anaylsis__()

        return self.geodata

if __name__ == "__main__":
    print('Running the analysis')
    analysis = Analysis().run()
