from __future__ import annotations
from zooAnimales.animal import Animal

class Reptil(Animal):
    listado: list[Reptil] = []
    iguanas: int = 0
    serpientes: int = 0
    def __init__(self, *args):
        super().__init__(*args[:-2])
        Animal.update_type("Reptil")
        self._colorEScamas, self._largoCola = args[-2:]
    
    @classmethod
    def crearIguana(
        cls,
        *args,
    ) -> Reptil:
        new = Reptil(*args[:1], "humedal", *args[1:],"verde", 3)
        cls.listado.append(new)
        cls.iguanas += 1
        return new

    @classmethod
    def crearSerpiente(
        cls,
        *args,
    ) -> Reptil:
        new = Reptil(*args[:1], "jungla", *args[1:],"blanco", 1)
        cls.listado.append(new)
        cls.serpientes += 1
        return new

    def movimiento(self) -> str:
        return "reptar"
    
    def cantidadReptiles(self) -> int:
        return Reptil.iguanas + Reptil.serpientes