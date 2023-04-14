from dataclasses import dataclass
from src.utils.downloader import download
from src.utils.files import unzip_file
import geopandas as gpd
import pandas as pd
import shutil
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
    file:str = ""
    extract_route:str = ""

    def __source_route__(self):
        """
            It will return the source route inside the data folder,
            if the file downloaded is a zip, the route will point to that zip,
            the same as contrary case.
        """
        return 'data/'+self.url.split('/')[-1]

    def __file_data_route__(self):
        return 'data/'+self.file

    def __download_data__(self):
        """
            This function will download the raw data from its source.
            # Parameters
            url:str 'www.abc.com/abc'
            # Output
            data:geopandas dataframe []
        """

        # Check if the file is in the data folder
        if not os.path.exists(self.__file_data_route__()):
            print("derivated no ready", self.__file_data_route__())
            # Download raw data
            download(url=self.url, path=self.__source_route__())
        else:
            print("derivated already", self.__file_data_route__())

    def __mv_file_from_source__(self):
        """
            Take the raw data file from its source folder, and move
            to the data folder.
        """
        shutil.move(self.extract_route, self.__file_data_route__())

    def __prepare__(self):
        try:
            # if the data is a zip file it can be unzipped
            unzip_file(path=self.__source_route__())

            if self.extract_route != "":
                self.__mv_file_from_source__()
        except:
            pass

    def __preprocessing__(self):
        if '.csv' in self.file:
            try:
                self.geodata = pd.read_csv(self.__file_data_route__(), encoding='utf-8')
            except:
                self.geodata = pd.read_csv(self.__file_data_route__(), sep='\t', encoding='latin1')
        else:
            self.geodata = gpd.read_file(self.__file_data_route__(), encoding='utf-8')

    def __anaylsis__(self):
        pass

    def run(self):
        """
            This will run all the methods of the pipeline and return the result
        """
        self.__download_data__()
        self.__prepare__()
        self.__preprocessing__()
        print('preprocessing ended', self.file)
        # self.__anaylsis__()

        # return self.geodata
