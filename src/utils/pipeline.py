from dataclasses import dataclass
from src.utils.downloader import download
from src.utils.files import unzip_file
from src.utils.files import rm_file
from src.utils.files import auxiliar_files
import os


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
    route:str = ""

    def __download_data__(self):
        """
            This function will download the raw data from its source.
            # Parameters
            url:str 'www.abc.com/abc'
            # Output
            data:geopandas dataframe []
        """
        self.name = self.url.split('/')[-1]
        
        # Check if the data file is already created or it need to be created
        auxiliar_files()

        # Check if the file is in the data folder
        if not os.path.exists(self.route):
            print("derivated no ready", self.route)
            # Download raw data
            download(self.url, self.name)
        else:
            print("derivated already", self.route)

    def __prepare__(self):
        try:
            unzip_file(self.name, 'data')
            rm_file(self.name, 'data')
        except:
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
