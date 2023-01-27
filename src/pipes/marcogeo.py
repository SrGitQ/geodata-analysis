from src.utils import Pipeline
from src.utils.files import unzip_file


class Marcogeo(Pipeline):
    """
    """
    def __prepare__(self):
        route_inside = 'data/'+self.name
        unzip_file(route_inside, route_inside.replace('.zip', ''))

    def __preprocessing__(self):
        pass

    def __anaylsis__(self):
        pass
