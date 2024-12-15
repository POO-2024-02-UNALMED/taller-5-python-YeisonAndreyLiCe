class Zoologico():
    
    def __init__(self, name: str, location: str, zones= None):
        self._nombre = name
        self._ubicacion = location
        self._zonas = zones or []
    
    def agregarZonas(self, zona):
        if not self._zonas:
            self._zonas = []
        self._zonas.extend([zona])

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            total += zona.cantidadAnimales()
        return total
    
    def getZona(self):
        return self._zonas
    
    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion