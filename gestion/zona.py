from zooAnimales import animal

class Zona():
    
    def __init__(self, name: str, zoo = None, animals: list[animal.Animal] = None):
        self._nombre = name
        self._zoo = zoo
        self._animales = animals

    def agregarAnimales(self, animal: list[animal.Animal]):
        if not self._animales:
            self._animales = []
        self._animales.extend([animal])

    def cantidadAnimales(self):
        return len(self._animales)
    
    def getAnimales(self):
        return self._animales
    
    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo
    