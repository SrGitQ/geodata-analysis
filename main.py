from src.utils import Pipeline
from src.pipes import Censo, Marcogeo, Sun
from multiprocessing import Pool
import os

def process(source:'Pipeline'):
    source.run()


class Analysis(Pipeline):
    """
        Analysis
    """
    geodata:dict[str, dict | str | int | float | None] = {}

    def __parallel_process__(self):
        censo_1990 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/1990/microdatos/iter/00_nacional_1990_iter_txt.zip', route='data/ITER_NALTXT90.csv')
        censo_2000 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/2000/microdatos/iter/00_nacional_2000_iter_txt.zip', route='data/ITER_NALTXT00.csv')
        censo_2010 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/2010/microdatos/iter/00_nacional_2010_iter_dbf.zip', route='data/ITER_NALDBF10.dbf')
        censo_2020 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/2020/microdatos/iter/ITER_NAL_2020_csv.zip', route='data/ITER_NALCSV20.csv')
        marcogeo = Marcogeo(url='https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463807469/mg_2020_integrado.zip', route='data/mg_2020_integrado/conjunto_de_datos')
        sun = Sun(url='https://raw.githubusercontent.com/gperaza/segregation/master/data/Base_SUN_2018.csv', route='data/Base_SUN_2018.csv')

        sources = [censo_1990, censo_2000, censo_2010, censo_2020, marcogeo, sun]

        with Pool(len(sources)) as p:
            p.map(process, sources)
    
    def __prepare__(self):
        
        names = os.listdir('data')
        for name in names:
            if '.txt' in name:
                os.rename('data/'+name, 'data/'+name.replace('.txt', '.csv'))

    def __anaylsis__(self):
        self.geodata = {}

    def run(self):
        self.__parallel_process__()
        self.__prepare__()
        self.__anaylsis__()

        return self.geodata

if __name__ == "__main__":
    print('Running the analysis')
    analysis = Analysis().run()
