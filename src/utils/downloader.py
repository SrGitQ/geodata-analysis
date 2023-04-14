import requests

def download(url:str="", path:str=""):
    """
        download data from url, and storage into files with the given name.
    """
    # Data will be obtained
    print('Downloading... ', path)
    source = requests.get(url).content

    # Write the data into the proper file
    open(path, "wb").write(source)
    print('Download completed...', path)

