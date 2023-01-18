from dataclasses import dataclass
from src.utils.downloader import download


@dataclass
class Pipeline:
    """
        This class will execute all the basic methods of a pipeline
        - load data
        - preprocess data
        - prepare data
        - analysis
        these methods can be rewriten for several uses
    """
    result:any = None # type: ignore

    def __load_data__(self, url:str=""):
        """
            This function will download the raw data from its source.
            # Parameters
            url:str 'www.abc.com/abc'
            # Output
            data:geopandas dataframe []
        """

        # download the raw data and retur
        return download(url)

    def __preprocessing__(self):
        pass

    def __prepare__(self):
        pass

    def __anaylsis__(self):
        self.result = None

    def run(self):
        """
            Will run all the methods of the pipeline and return the result
        """
        self.__load_data__()
        self.__preprocessing__()
        self.__prepare__()
        self.__anaylsis__()

        return self.result
