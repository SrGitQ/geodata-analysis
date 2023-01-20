import requests
from src.utils.files import auxiliar_files

def download(url:str=""):
    """
        download data from url, and storage into files with the given name.
    """
    # Naming the file
    name = url.split('/')[-1]
    print('Downloading... ', name)

    # Data will be obtained
    source = requests.get(url).content

    # Check and create the auxiliar files
    auxiliar_files()

    # Write the data into the proper file
    open("data/"+name, "wb").write(source)
