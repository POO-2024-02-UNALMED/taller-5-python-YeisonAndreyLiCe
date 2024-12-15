from __future__ import annotations
from zooAnimales.animal import Animal

class Ave(Animal):
    listado: list[Ave]
    halcones: int
    aguilas: int
    def __init__(self, *args):
        self.coloresPlumas = args[-1:]
        super().__init__(*args[:-1])
        Animal.update_type("Ave")

    def cantidadAves(self) -> int:
        return len(self.listado)

    def movimiento(self) -> str:
        return "volar"

    def crearHalcon(
        self,
        *args,
    ) -> Ave:
        new = Ave(*args[:1], "montañas", *args[1:], "café glorioso")
        Ave.halcones += 1
        Ave.listado.append(new)
        return new

    def crearAguila(
        self,
        *args,
    ) -> Ave:
        new = Ave(*args[:1], "montañas", *args[1:],"blanco y amarillo")
        Ave.listado.append(new)
        Ave.aguilas += 1
        return new