"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehiculo():
    
    #Métodos
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return f'Vehiculo de {self.ruedas} ruedas y de color {self.color}'
    
class Coche(Vehiculo):
    
    #Métodos
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return super().__str__() + f', con una velocidad de {str(self.velocidad)} km/hr'
    
class Bicicleta(Vehiculo):
    
    #Métodos
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return super().__str__() + f', tipo: {self.tipo}'


# Creamos un objeto de la clase Vehiculo
vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)

# Creamos un objeto de la clase hija Coche
coche = Coche('Azul', 4, 150)
print(coche)

# Creamos un objeto de la clase hija Bicicleta
bicicleta = Bicicleta('Blanca', 2, 'Urbano')
print(bicicleta)
