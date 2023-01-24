import unittest
import os


class RawDataTest(unittest.TestCase):

    def test_censo_1990_zip(self):
        file = '00_nacional_1990_iter_txt.zip'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2000_zip(self):
        file = '00_nacional_2000_iter_txt.zip'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2010_zip(self):
        file = '00_nacional_2010_iter_dbf.zip'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2020_zip(self):
        file = 'ITER_NAL_2020_csv.zip'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_mg_2020_integrado_zip(self):
        file = 'mg_2020_integrado.zip'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_base_sun_2018_csv(self):
        file = 'Base_SUN_2018.csv'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')


if __name__ == "__main__":
    test = unittest.main()
