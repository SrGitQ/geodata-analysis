import unittest
import os


class RawDataTest(unittest.TestCase):

    def test_censo_1990_txt(self):
        file = 'ITER_NALTXT90.txt'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2000_txt(self):
        file = 'ITER_NALTXT00.txt'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2010_dbf(self):
        file = 'ITER_NALDBF10.dbf'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_censo_2020_csv(self):
        file = 'ITER_NALCSV20.csv'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_base_sun_2018_csv(self):
        file = 'Base_SUN_2018.csv'
        self.assertTrue(file in os.listdir('data'), f'the file {file} is not at /data')
    
    def test_mg_2020_integrado(self):
        files = [
            '00a.cpg',
            '00a.dbf',
            '00a.prj',
            '00a.shp',
            '00a.shx',
            '00ent.cpg',
            '00ent.dbf',
            '00ent.prj',
            '00ent.shp',
            '00ent.shx',
            '00l.cpg',
            '00l.dbf',
            '00l.prj',
            '00l.shp',
            '00l.shx',
            '00lpr.cpg',
            '00lpr.dbf',
            '00lpr.prj',
            '00lpr.shp',
            '00lpr.shx',
            '00mun.cpg',
            '00mun.dbf',
            '00mun.prj',
            '00mun.shp',
            '00mun.shx',
        ]
        for file in files:
            self.assertTrue(file in os.listdir('data/MG_2020_Integrado/conjunto_de_datos'), f'the file {file} is not at /data')


if __name__ == "__main__":
    test = unittest.main()
