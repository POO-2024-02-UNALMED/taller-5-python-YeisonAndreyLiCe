
from __future__ import annotations
from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado: list[Mamifero] = []
    caballos: int = 0
    leones: int = 0

    def __init__(
        self,
        *args,
    ):
        self._pelaje, self._patas = args[-2:]
        super().__init__(*args[:-2])
        Animal.update_type("Mamífero")

    def cantidadMamiferos() -> int:
        return len(Mamifero.listado)

    @classmethod
    def crearCaballo(
        cls,
        *args,
    ) -> Mamifero:
        new = Mamifero(*args[:1], "pradera", *args[1:], True, 4)
        cls.listado.append(new)
        cls.caballos += 1
        return new

    @classmethod
    def crearLeon(
        cls,
        *args,
    ) -> Mamifero:
        new = Mamifero(*args[:1], "selva", *args[1:], True, 4)
        cls.listado.append(new)
        cls.leones += 1
        return new
    
    # getter
    def isPelaje(self) -> str:
        return self._pelaje
    
    def getPatas(self) -> int:
        return self._patas