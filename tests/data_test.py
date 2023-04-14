import unittest
import os


class RawDataTest(unittest.TestCase):

    def test_censo_1990_txt(self):
        file = 'ITER_NALTXT90.csv'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2000_txt(self):
        file = 'ITER_NALCSV00.csv'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2010_dbf(self):
        file = 'ITER_NALCSV10.csv'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2020_csv(self):
        file = 'ITER_NALCSV20.csv'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_base_sun_2018_csv(self):
        file = 'Base_SUN_2018.csv'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_mg_2020_integrado(self):
        file = '00mun.shp'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')

    def test_files_unwanted(self):
        wanted_files = ['ITER_NALTXT90.csv', 'ITER_NALCSV00.csv', 'ITER_NALCSV10.csv', 'ITER_NALCSV20.csv', 'Base_SUN_2018.csv', '00mun.shp', '00mun.shx']
        self.assertTrue(all([file in wanted_files for file in os.listdir('data')]), f'There are some files that are unwanted in the list: \n{wanted_files}\nfiles in the folder:\n{os.listdir("data")}')


if __name__ == "__main__":
    test = unittest.main()
