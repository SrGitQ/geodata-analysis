from src.utils import Pipeline
from dataclasses import dataclass
import pandas as pd


@dataclass
class Censo00(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://www.inegi.org.mx/contenidos/programas/ccpv/2000/datosabiertos/cgpv2000_iter_00_csv.zip"
    file:str = "ITER_NALCSV00.csv"
    extract_route:str = "data/cgpv2000_iter_00_csv/cgpv2000_iter_00/conjunto_de_datos/cgpv2000_iter_00.csv"

    #def __preprocessing__(self):
    #    self.geodata = pd.read_csv(self.__file_data_route__(), encoding='ISO-8859-1', sep='\t', names=["entidad","nom_ent","mun","nom_mun","loc","nom_loc","longitud","latitud","altitud","pobtot","pmascul","pfemeni","pob0_4","p5_mas","pob6_14","pob12_","pob15_","pob15_17","pob15_24","pobf15_49","pob18_","pmasc18_","pfemen18_","psderss","pcderss","pderimss","pderiste","pnacent","pnacoent","p5_res95","p5_reso95","pcondisc","pcdismot","pcdisaud","pcdisvis","pcdismen","pcdislen","psindisc","p6_14slee","p6_14nlee","p15_alfab","p15_analf","p5_asiesc","p5_naesc","p6_14aesc","p6_14naesc","p15_17aesc","p15_24aesc","p15_24nesc","p15_sinstr","p15_sprima","p15_cprima","p15_pospri","p15_ssecu","p15_csecu","p15_sinsec","p15_consec","p15_cmedss","p18_smedsu","p18_cmedsu","p18_csuper","gradoesco","psolter12_","pcasada12_","p5_hli","p5_hliyne","p5_hliye","p5_catolic","p5_ncatoli","p5_sinreli","pecoactiv","pecoinact","pocupada","pocusecp","pocusecs","pocusect","pocuningr","p_1sm","p1_2sm","p2_5sm","p6_10sm","p10_sm","pnotraba","p_32htra","p33_40htr","p41_48htr","p48_htr","totvivhab","vivparhab","ocuvivpar","pro_ovp","pro_ocvp","vp_pardes","vp_tecdes","vp_pisdes","vp_ccuart","vp2_5cuar","vp_2cuar","v_1cuarto","vp_cocgas","vp_coclen","vp_coccar","vp_cocpet","vp_sersan","vp_aguent","vp_drenaj","vp_electr","vp_dreagu","vp_dreele","vp_aguele","vp_agdrel","vp_noade","vp_propia","vp_ppagad","vp_ppagan","vp_rentad","vp_cbiene","vp_sbiene","vp_radio","vp_tv","vp_video","vp_refri","vp_lavad","vp_telef","vp_boiler","vp_autom","tothog","hogjefm","hogjeff","pobhog","phogjefm","phogjeff"])

    def __anaylsis__(self):
        self.geodata = self.geodata.rename(columns={'pobtot':'p_total'})
        self.geodata = self.geodata[['entidad', 'nom_ent', 'mun', 'nom_mun', 'loc', 'nom_loc', 'p_total']]
        self.geodata = self.geodata.query('nom_loc.str.contains("TOTAL MUNICIPAL")')
        self.geodata['CVEGEO'] = self.geodata.apply(lambda x:f'{str(x["entidad"]).zfill(2)}{str(x["mun"]).zfill(3)}', axis=1)
        
        self.geodata = self.geodata[['CVEGEO', 'p_total']]
        self.geodata.columns = ['CVEGEO', 'P_TOTAL_2000']
        self.geodata.drop_duplicates(subset=['CVEGEO'], inplace=True)
        """
        self.geodata['CVE_MUN2000'] = self.geodata['entidad'].str.cat(self.geodata['mun']) 
        self.geodata['CVE_MUN2000'] = pd.to_numeric(self.geodata['CVE_MUN2000'])
        self.geodata = self.geodata.query("nom_loc == 'TOTAL MUNICIPAL'")
        self.geodata = self.geodata[['nom_mun', 'p_total', 'CVE_MUN2000']]
        self.geodata = self.geodata.rename(columns={'p_total': 'POBTOT2000'})
        """

