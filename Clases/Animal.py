class Animal:
    def __init__(self, especie,raza, edad):
        self.especie = especie
        self.raza = raza
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} es un {self.especie} de {self.edad} años"    
    
    def getNombre(self):
        return self.nombre
    
    def getEspecie(self):
        return self.especie
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setEspecie(self, especie):
        self.especie = especie

    def setEdad(self, edad):
        self.edad = edad
        