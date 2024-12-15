import gestion.zona as Zona
from typing import Literal

class Animal:
    totalAnimales: int = 0
    animals_by_type: dict[str, int] = {}
    
    def __init__(self, name: str, age: int, habitat: str, gender: str, zone: Zona.Zona | None = None) -> None:
        self._nombre = name
        self._edad = age
        self._habitat = habitat
        self._genero = gender
        self._zona = zone
        Animal.totalAnimales += 1

    def movimiento(self) -> str:
        return "Desplazarse"
    
    def totalPorTipo(self) -> str:
        return (f"Mamíferos: {Animal.animals_by_type['Mamífero']}\nAves: {Animal.animals_by_type['Ave']}"
                + f"\nReptiles: {Animal.animals_by_type['Reptil']}\nPeces: {Animal.animals_by_type['Pez']}\n"
                + f"Anfibios: {Animal.animals_by_type['Anfibio']}")
    
    def __str__(self) -> str:
        if self._zona:
            return (f"Mi nombre es {self._nombre}, tengo una edad de"
                    f"{self._edad}, habito en {self._habitat}, mi genero es"
                    f"{self._genero} y la zona en la que me encuentro es"
                    f"{self._zona.nombre}."
                )

        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}."
   
    @classmethod
    def update_type(cls, type: Literal["Mamífero", "Ave", "Reptil", "Pez", "Anfibio"]) -> None:
        cls.animals_by_type[type] = cls.animals_by_type.get(type, 0) + 1

    def getNombre(self) -> str:
        return self._nombre
    
    def getEdad(self) -> int:
        return self._edad
    
    def getHabitat(self) -> str:
        return self._habitat
    
    def getGenero(self) -> str:
        return self._genero
    
    def getZona(self) -> Zona.Zona | None:
        return self._zona
    