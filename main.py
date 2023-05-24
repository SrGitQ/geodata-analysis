from src.utils import Pipeline
from src.pipes import Censo90, Censo00, Censo10, Censo20, Marcogeo, Sun
from multiprocessing import Pool
import geopandas as gpd
import pandas as pd
import rasterio as rio
from rasterio import mask
import numpy as np
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
        self.sources['marcogeo'].geodata['CVEGEO'] = self.sources['marcogeo'].geodata['CVEGEO'].astype('int64')
        self.geodata = pd.merge(self.geodata, self.sources['marcogeo'].geodata, left_on='CVEGEO', right_on='CVEGEO')
        
        def mts_built_per_year_and_classification(df, years=range(1975, 2025, 5)):
            results = []
            
            for year in years:#range(1975, 2025, 5):#
                raster_url = f'http://tec-expansion-urbana-p.s3.amazonaws.com/GHSL/GHS_BUILT_S/GHS_BUILT_S_E{year}_GLOBE_R2022A_54009_100_V1_0.tif'
                with rio.open(raster_url) as src:

                    mun = []
                    for id_, polygon in enumerate(df['geometry']):
                        clip = mask.mask(src, [polygon], crop=True)[0][0]
                        clip_ = np.where(clip == src.nodata, 0, clip)
                        mts_built = clip_.sum()

                        def custom_round(value):
                            return 1 if round(value, 2) >= 0.2 else 0
                        mts_built_up_binary = np.vectorize(custom_round)(clip_/(100*100))
                        
                        mun.append([mts_built, mts_built_up_binary])
                        print(f"clipping the polygon -{id_}- in the year -{year}-")


                    results.append(mun)
                    src.close()
            mts_built = [[zone[0] for zone in year] for year in results]
            subsets = [[zone[-1] for zone in year] for year in results]
            rasters_with_class = []
            for zone in range(0, len(subsets[0])):
                current_zone = [subsets[0][zone]]
                for year in range(1, len(subsets)):
                    current_zone.append(subsets[year][zone])
                    print(f'creating rasters at zone: {zone} in the year: {year}')
                rasters_with_class.append(np.sum(current_zone, axis=0))
            return mts_built, rasters_with_class
        
       # self.geodata = self.geodata.query("NOM_SUN == 'Guadalajara'")
        mts_built, rasters_with_class = mts_built_per_year_and_classification(self.geodata)
        for i, year in enumerate(range(1975, 2025, 5)):
            self.geodata[f'mts_built_up_{year}'] = mts_built[i]

        #self.geodata['subset'] = rasters_with_class
        # transforming to geopandas dataframe to easy export

        self.geodata = self.geodata[['NOM_SUN', 'CVE_ENT_x', 'NOM_ENT', 'CVE_MUN', 'NOM_MUN', 'CVE_LOC', 'NOM_LOC',
       'CVE_SUN', 'POB_2018', 'P_TOTAL_1990',
       'P_TOTAL_2000', 'P_TOTAL_2010', 'P_TOTAL_2020', 'CVEGEO', 'NOMGEO', 'mts_built_up_1975', 'mts_built_up_1980',
       'mts_built_up_1985', 'mts_built_up_1990', 'mts_built_up_1995', 'mts_built_up_2000',
       'mts_built_up_2005', 'mts_built_up_2010', 'mts_built_up_2015', 'mts_built_up_2020', 'LONGITUD', 'LATITUD']]
        
        self.geodata.columns = ['NOM_SUN', 'CVE_ENT', 'NOM_ENT', 'CVE_MUN', 'NOM_MUN', 'CVE_LOC', 'NOM_LOC',
       'CVE_SUN', 'POB_2018', 'P_TOTAL_1990',
       'P_TOTAL_2000', 'P_TOTAL_2010', 'P_TOTAL_2020', 'CVEGEO', 'NOMGEO', 'mts_built_up_1975', 'mts_built_up_1980',
       'mts_built_up_1985', 'mts_built_up_1990', 'mts_built_up_1995', 'mts_built_up_2000',
       'mts_built_up_2005', 'mts_built_up_2010', 'mts_built_up_2015', 'mts_built_up_2020', 'LONGITUD', 'LATITUD']
        calculations = {
            'NOM_SUN':"first", 
            'CVE_ENT':"first", 
            'NOM_ENT':"first", 
            'CVE_MUN':"first", 
            'NOM_MUN':"first", 
            'CVE_LOC':"first", 
            'NOM_LOC':"first", 
            'POB_2018':"sum", 
            'P_TOTAL_1990':"sum",
            'P_TOTAL_2000':"sum",
            'P_TOTAL_2010':"sum",
            'P_TOTAL_2020':"sum",
            'CVEGEO':"first",
            'NOMGEO':"first",
            'mts_built_up_1975':"sum",
            'mts_built_up_1980':"sum",
            'mts_built_up_1985':"sum", 
            'mts_built_up_1990':"sum", 
            'mts_built_up_1995':"sum", 
            'mts_built_up_2000':"sum",
            'mts_built_up_2005':"sum", 
            'mts_built_up_2010':"sum", 
            'mts_built_up_2015':"sum", 
            'mts_built_up_2020':"sum", 
            'LONGITUD':"first", 
            'LATITUD':"first"
        }
        self.geodata = self.geodata.query("CVE_SUN.str.contains('M')").groupby(by="CVE_SUN").agg(calculations).reset_index()

        #self.geodata = self.geodata[["CVE_ENT_x","NOM_ENT","NOM_MUN","CVE_LOC","NOM_LOC","CVE_SUN","NOM_SUN","POB_2018","CVEGEO","P_TOTAL_1990","P_TOTAL_2000","P_TOTAL_2010","P_TOTAL_2020","LONGITUD","LATITUD","CVE_MUN","NOMGEO"]]
        #self.geodata = gpd.GeoDataFrame(self.geodata, crs="ESRI:54009")
        # Exporting as geojson
        #with open('municipios.geojson', 'w') as file:
        #    file.write(self.geodata.to_json())
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
