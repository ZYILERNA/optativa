#Ejercicio de Getter y Setter
#Compuesto por: Ricardo Zhen

class Pollo:
    def __init__(self, raza, peso, color):
        self._raza = raza
        self._peso = peso
        self._color = color
        
    # Getter para raza
    def get_raza(self):
        return self._raza
    
    # Setter para raza
    def set_raza(self, raza):
        self._raza = raza
    
    # Getter para peso
    def get_peso(self):
        return self._peso
    
    # Setter para peso
    def set_peso(self, peso):
        self._peso = peso
    
    # Getter para color
    def get_color(self):
        return self._color
    
    # Setter para color
    def set_color(self, color):
        self._color = color


#Ejemplos de uso

Pollo1 = Pollo("Sedosa",2,"Pardo")

print(Pollo1.get_raza())
print(f"El peso del pollo es: ", Pollo1.get_peso(), " kl")
print(f"El color del pollo es: ",Pollo1.get_color())


Pollo1.set_raza("Rojiza")
print(Pollo1.get_raza())

Pollo1.set_color("negro")
print(Pollo1.get_color())











""""

     
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    # Getter para nombre
    def get_nombre(self):
        return self._nombre
    
    # Setter para nombre
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    # Getter para edad
    def get_edad(self):
        return self._edad
    
    # Setter para edad
    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad no puede ser negativa")

# Ejemplo de uso
persona = Persona("Juan", 25)
print(persona.get_nombre())  # Salida: Juan
print(persona.get_edad())    # Salida: 25

persona.set_nombre("Pedro")
persona.set_edad(30)
print(persona.get_nombre())  # Salida: Pedro
print(persona.get_edad())    # Salida: 30

# Intentar asignar una edad negativa
persona.set_edad(-5)  # Salida: La edad no puede ser negativa
"""
