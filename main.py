from src.utils import Pipeline
from src.pipes import Censo, Marcogeo, Sun


class Analysis(Pipeline):
    """
        pass
    """
    geodata:dict[str, dict | str | int | float | None] = {}

    def __parallel_process__(self):
        censo_1990 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/1990/microdatos/iter/00_nacional_1990_iter_txt.zip')
        # censo_2000 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/2000/microdatos/iter/00_nacional_2000_iter_txt.zip')
        # censo_2010 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/2010/microdatos/iter/00_nacional_2010_iter_dbf.zip')
        # censo_2020 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/2020/microdatos/iter/ITER_NAL_2020_csv.zip')
        # marcogeo = Marcogeo(url='https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463807469/mg_2020_integrado.zip')
        # sun = Sun(url='https://github.com/gperaza/segregation/blob/master/data/Base_SUN_2018.csv')

        censo_1990.run()

    def __anaylsis__(self):
        self.geodata = {}

    def run(self):
        self.__parallel_process__()
        self.__anaylsis__()

        return self.geodata

if __name__ == "__main__":
    print('Running the analysis')
    analysis = Analysis().run()
