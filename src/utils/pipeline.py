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
    geodata = {}
    url:str = ""

    def __download_data__(self):
        """
            This function will download the raw data from its source.
            # Parameters
            url:str 'www.abc.com/abc'
            # Output
            data:geopandas dataframe []
        """

        # download raw data
        download(self.url)

    def __prepare__(self):
        pass

    def __preprocessing__(self):
        pass

    def __anaylsis__(self):
        self.geodata = {}

    def run(self):
        """
            This will run all the methods of the pipeline and return the result
        """
        self.__download_data__()
        self.__prepare__()
        self.__preprocessing__()
        self.__anaylsis__()

        return self.geodata
