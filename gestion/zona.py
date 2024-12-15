import gestion.zoologico
from zooAnimales import animal

class Zona():
    
    def __init__(self, name: str, zoo: gestion.zoologico.Zoologico, animals: list[animal.Animal]):
        self._nombre = name
        self._zoo = zoo
        self._animales = animals

    def agregarAnimales(self, animal: list[animal.Animal]):
        self._animales.extend(animal)

    def cantidadAnimales(self):
        return len(self._animales)
    
    def getAnimales(self):
        return self._animales
    
    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo
    