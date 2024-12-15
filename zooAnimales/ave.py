from __future__ import annotations
from zooAnimales.animal import Animal

class Ave(Animal):
    listado: list[Ave] = []
    halcones: int = 0
    aguilas: int = 0
    def __init__(self, *args):
        self.coloresPlumas = args[-1:]
        super().__init__(*args[:-1])
        Animal.update_type("Ave")

    def cantidadAves(self) -> int:
        return len(self.listado)

    def movimiento(self) -> str:
        return "volar"

    @classmethod
    def crearHalcon(
        cls,
        *args,
    ) -> Ave:
        new = Ave(*args[:1], "montañas", *args[1:], "café glorioso")
        cls.halcones += 1
        cls.listado.append(new)
        return new

    @classmethod
    def crearAguila(
        cls,
        *args,
    ) -> Ave:
        new = Ave(*args[:1], "montañas", *args[1:],"blanco y amarillo")
        cls.listado.append(new)
        cls.aguilas += 1
        return new