
from __future__ import annotations
from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado: list[Mamifero]
    caballos: int
    leones: int
    def __init__(
        self,
        *args,
    ):
        self._pelaje, self._patas = args[-2:]
        super().__init__(*args[:-2])
        Animal.update_type("Mamífero")

    def cantidadMamiferos(self) -> int:
        return len(self.listado)

    def crearCaballo(
        self,
        *args,
    ) -> Mamifero:
        new = Mamifero(*args[:1], "pradera", *args[1:], True, 4)
        Mamifero.listado.append(new)
        Mamifero.caballos += 1
        return new

    def crearLeon(
        self,
        *args,
    ) -> Mamifero:
        new = Mamifero(*args[:1], "selva", *args[1:], True, 4)
        Mamifero.listado.append(new)
        Mamifero.leones += 1
        return new