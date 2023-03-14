from src.utils import Pipeline
import geopandas as gpd
import numpy as np
import pandas as pd
from src.utils.cords import dms2dd


class Censo00(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2000/microdatos/iter/00_nacional_2000_iter_txt.zip"
    route:str = "data/ITER_NALTXT00.csv"
    
    def __preprocessing__(self):
        self.geodata = gpd.read_file('data/ITER_NALTXT00.csv', encoding='utf-8', columns=["entidad",	"nom_ent",	"mun",	"nom_mun",	"loc",	"nom_loc",	"longitud",	"latitud",	"altitud",	"p_total",	"hombres",	"mujeres",	"pob_lee",	"pob_no_l",	"alfabet",	"analfbet",	"asis_esc",	"n_as_esc",	"asis6_es",	"n_as6_es",	"n_hab_esp",	"habla_esp",	"sin_ins",	"prim_inc",	"prim_com",	"ins_pprim",	"p_e_act",	"p_e_inac",	"pob_ocup",	"sec_prim",	"sec_sec",	"sec_ter",	"t_vivhab",	"viv_part",	"ocup_viv",	"prom_viv",	"prom_cua",	"pared_la",	"techo_la",	"piso_tie",	"viv_1_c",	"viv_2_c",	"c_agua_ent",	"c_drenaje",	"c_e_elect",	"viv_pprop"])

    def __anaylsis__(self):
        self.geodata['CVE_MUN2000'] = self.geodata.entidad.str.cat(self.geodata.mun) 
        self.geodata['CVE_MUN2000'] = pd.to_numeric(self.geodata['CVE_MUN2000'])
        self.geodata = self.geodata.query("nom_loc == 'TOTAL MUNICIPAL'")
        self.geodata = self.geodata[['nom_mun', 'pobtot', 'CVE_MUN2000']]
        self.geodata = self.geodata.rename(columns={'pobtot': 'POBTOT2000'})

        print(self.geodata)
