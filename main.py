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
    geodata = {}

    def __parallel_process__(self):
        self.sources = {
            "censo_1990" : Censo90(),
            "censo_2000" : Censo00(),
            "censo_2010" : Censo10(),
            "censo_2020" : Censo20(),
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
        # Merging all the censuses
        # -> 1990, 2000
        self.geodata = pd.merge(self.sources['censo_1990'].geodata, self.sources['censo_2000'].geodata, left_on="CVEGEO", right_on="CVEGEO")
        # -> 1990, 2000, 2010
        self.geodata = pd.merge(self.geodata, self.sources['censo_2010'].geodata, left_on="CVEGEO", right_on="CVEGEO")
        # -> 1990, 2000, 2010, 2020
        self.geodata = pd.merge(self.geodata, self.sources['censo_2020'].geodata, left_on="CVEGEO", right_on="CVEGEO")

        # Merging SUN
        self.sources["sun"].geodata['CVEGEO'] = self.sources["sun"].geodata['CVEGEO'].astype('int64')
        self.geodata['CVEGEO'] = self.geodata['CVEGEO'].astype('int64')
        self.geodata = pd.merge(self.sources["sun"].geodata, self.geodata, left_on="CVEGEO", right_on="CVEGEO")

        # Merging Polygons

        # Exporting as geojson
        with open('municipios.geojson', 'w') as file:
            file.write(self.geodata.to_json())
        # Exporting as csv
        with open('municipios.csv', 'w') as file:
            file.write(self.geodata.to_csv())

    def run(self):
        # Check if the data file is already created or it need to be created
        auxiliar_files()
        self.__parallel_process__()
        #self.__prepare__()
        self.__anaylsis__()

        return self.geodata

if __name__ == "__main__":
    print('Running the analysis')
    analysis = Analysis().run()
