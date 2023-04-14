from src.utils import Pipeline
from dataclasses import dataclass


@dataclass
class Sun(Pipeline):
    """
    """
    geodata = {}
    url:str = "https://raw.githubusercontent.com/gperaza/segregation/master/data/Base_SUN_2018.csv"
    file:str = "Base_SUN_2018.csv"
    extract_route:str = ""

