def auxiliar_files():
    """
        This function will check if all the auxiliar files exist, the files will
        be created just in negative case.
    """
    import os

    # print("Files and analysis will be generated at... ", os.getcwd()+"/data")
    files_list = os.listdir()
    if 'data' not in files_list:
        os.mkdir('data')
    
def rm_file(file:str="", route:str="data"):
    """
        Delete the files unwanted, mainly .zip files.
    """
    import os
    try:
        os.remove(route+'/'+file)
    except:
        import shutil
        shutil.rmtree(route+'/'+file)
        print('Unexpected operation')


def unzip_file(file:str="", route:str="data"):
    """
        Unzip the files that contains the raw data.
    """
    import zipfile

    with zipfile.ZipFile(route+'/'+file, 'r') as zip_ref:
        zip_ref.extractall(route)
