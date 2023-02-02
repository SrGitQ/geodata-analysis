import requests

def download(url:str="", name:str=""):
    """
        download data from url, and storage into files with the given name.
    """
    # Data will be obtained
    print('Downloading... ', name)
    source = requests.get(url).content

    # Write the data into the proper file
    open("data/"+name, "wb").write(source)
