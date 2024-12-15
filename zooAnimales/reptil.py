from __future__ import annotations
from zooAnimales.animal import Animal

class Reptil(Animal):
    listado: list[Reptil]
    iguanas: int
    serpientes: int
    def __init__(self, *args):
        super().__init__(*args[:-2])
        Animal.update_type("Reptil")
        self._colorEScamas, self._largoCola = args[-2:]

    def crearIguana(
        self,
        *args,
    ) -> Reptil:
        new = Reptil(*args[:1], "humedal", *args[1:],"verde", 3)
        Reptil.listado.append(new)
        Reptil.iguanas += 1
        return new

    def crearSerpiente(
        self,
        *args,
    ) -> Reptil:
        new = Reptil(*args[:1], "jungla", *args[1:],"blanco", 1)
        Reptil.listado.append(new)
        Reptil.serpientes += 1
        return new

    def movimiento(self) -> str:
        return "reptar"
    
    def cantidadReptiles(self) -> int:
        return Reptil.iguanas + Reptil.serpientes