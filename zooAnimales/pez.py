from __future__ import annotations
from zooAnimales.animal import Animal

class Pez(Animal):
    listado: list[Pez]
    salmones: int
    bacalaos: int
    def __init__(self, *args):
        super().__init__(*args[:-2])
        Animal.update_type("Pez")
        self._colorEscamas, self._cantidadAletas = args[-2:]

    def crearSalmon(
        self,
        *args,
    ) -> Pez:
        new = Pez(*args[:1], "oceano", *args[1:],"rojo", 6)
        Pez.listado.append(new)
        Pez.salmones += 1
        return new

    def crearBacalao(
        self,
        *args,
    ) -> Pez:
        new = Pez(*args[:1], "oceano", *args[1:],"gris", 6)
        Pez.listado.append(new)
        Pez.bacalaos += 1
        return new

    def movimiento(self) -> str:
        return "nadar"
    
    def cantidadPeces(self) -> int:
        return Pez.salmones + Pez.bacalaos
    
    # getter
    def getColorEscamas(self) -> str:
        return self._colorEscamas
    
    def getCantidadAletas(self) -> int:
        return self._cantidadAletas