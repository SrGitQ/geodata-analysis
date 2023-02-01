import requests
from src.utils.files import auxiliar_files
import os

def download(url:str="", name:str=""):
    """
        download data from url, and storage into files with the given name.
    """
    # Naming the file
    print('spread... ', name)

    # Check and create the auxiliar files
    auxiliar_files()
    
    # check files
    print('checking...', name)
    if name.replace('.zip', '') in [f.replace('.csv', '').replace('.dbf', '').replace('.txt', '') for f in os.listdir('data')]:
        print('already: ', name)
        return

    # Data will be obtained
    print('Downloading... ', name)
    source = requests.get(url).content


    # Write the data into the proper file
    open("data/"+name, "wb").write(source)
