from src.utils import Pipeline
from src.pipes import Censo, Marcogeo, Sun


class Analysis(Pipeline):
    """
        pass
    """
    geodata:dict[str, dict | str | int | float | None] = {}

    def __parallel_process__(self):
        censo_1990 = Censo(url='https://www.inegi.org.mx/contenidos/programas/ccpv/1990/microdatos/iter/00_nacional_1990_iter_txt.zip')
        # censo_2000 = Censo(url='')
        # censo_2010 = Censo(url='')
        # censo_2020 = Censo(url='')
        # marcogeo = Marcogeo(url='')
        # sun = Sun(url='')

        censo_1990.run()

    def __anaylsis__(self):
        self.geodata = {}

    def run(self):
        self.__parallel_process__()
        self.__anaylsis__()

        return self.geodata

if __name__ == "__main__":
    print('running the analysis')
    analysis = Analysis().run()
