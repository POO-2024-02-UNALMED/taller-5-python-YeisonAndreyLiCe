from __future__ import annotations
from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado: list[Anfibio]
    ranas: int
    salamandras: int
    def __init__(self, *args):
        super().__init__(*args[:-2])
        Animal.update_type("Anfibio")
        self._colorPiel, self._venenoso = args[-2:]

    def crearRana(
        self,
        *args,
    ) -> Anfibio:
        new = Anfibio(*args[:1], "selva", *args[1:],"rojo", True)
        Anfibio.listado.append(new)
        Anfibio.ranas += 1
        return new

    def crearSalamandra(
        self,
        *args,
    ) -> Anfibio:
        new = Anfibio(*args[:1], "selva", *args[:1], "rojo y amarillo", False)

        Anfibio.listado.append(new)
        Anfibio.salamandras += 1

        return new
    
    def movimiento(self) -> str:
        return "saltar"