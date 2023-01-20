from src.utils import Pipeline
from src.pipes import Censo, Marcogeo, Sun


class Analysis(Pipeline):
    """
        pass
    """
    result:any = None# type: ignore
    
    def __parallel_process__(self):
        censo_90 = Censo()

    def __anaylsis__(self):
        self.result = None

    def run(self):
        self.__parallel_process__()
        self.__anaylsis__()

        return self.result

if __name__ == "__main__":
    analysis = Analysis().run()
