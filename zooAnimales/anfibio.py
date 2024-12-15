from __future__ import annotations
from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado: list[Anfibio] = []
    ranas: int = 0
    salamandras: int = 0
    def __init__(self, *args):
        super().__init__(*args[:-2])
        Animal.update_type("Anfibio")
        self._colorPiel, self._venenoso = args[-2:]

    @classmethod
    def crearRana(
        cls,
        *args,
    ) -> Anfibio:
        new = Anfibio(*args[:1], "selva", *args[1:],"rojo", True)
        cls.listado.append(new)
        cls.ranas += 1
        return new

    @classmethod
    def crearSalamandra(
        cls,
        *args,
    ) -> Anfibio:
        new = Anfibio(*args[:1], "selva", *args[:1], "rojo y amarillo", False)

        cls.listado.append(new)
        cls.salamandras += 1

        return new
    
    def movimiento(self) -> str:
        return "saltar"