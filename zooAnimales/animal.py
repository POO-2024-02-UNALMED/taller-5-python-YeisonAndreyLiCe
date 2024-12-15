from typing import Literal

class Animal:
    totalAnimales: int = 0
    animals_by_type: dict[str, int] = {}
    
    def __init__(self, name: str, age: int, habitat: str, gender: str = "F", zone = None) -> None:
        self._nombre = name
        self._edad = age
        self._habitat = habitat
        self._genero = gender
        self._zona = zone
        Animal.totalAnimales += 1

    def movimiento(self) -> str:
        return "Desplazarse"
    
    @classmethod
    def totalPorTipo(cls) -> str:
        return (
            f"Mamiferos: {cls.animals_by_type['Mamífero']}\n"
            f"Aves: {cls.animals_by_type['Ave']}\n"
            f"Reptiles: {cls.animals_by_type['Reptil']}\n"
            f"Peces: {cls.animals_by_type['Pez']}\n"
            f"Anfibios: {cls.animals_by_type['Anfibio']}"
            )
    
    def toString(self) -> str:
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
    
    def getZona(self):
        return self._zona
    