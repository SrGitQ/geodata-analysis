import requests
import os

def auxiliar_files():
    """
        This function will check if all the auxiliar files exist, the files will
        be created just in negative case.
    """
    print("Files and analysis will be generated at... ", os.path.dirname)
    files_list = os.listdir()
    if 'data' not in files_list:
        os.mkdir('data')

def download(url:str="", name:str=''):
    """
        download data from url, and storage into files with the given name.
    """
    # Data will be obtained
    source = requests.get(url).content

    # Check and create the auxiliar files
    auxiliar_files()

    # Write the data into the proper file
    open(name, "wb").write(source)
