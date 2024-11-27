
# 1.- Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
# las cuales heredan de la clase Padre Vehiculo.
# La clase padre debe tener los siguientes atributos y métodos

# Vehiculo (Clase Padre):
# -Atributos (color, ruedas)
# -Métodos ( __init__() y __str__ )

# Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de Vehículo):
# -Atributos ( velocidad (km/hr) )
# -Métodos ( __init__() y __str__() )

# Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de Vehículo):
# -Atributos ( tipo (urbana/montaña/etc )
# -Métodos ( __init__() y __str__() )


"""class Vehiculo():
    
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
print(bicicleta)"""

# 2. - Crea una clase base llamada SerVivo con un método respirar que 
# devuelva "Estoy respirando". 
# Luego, crea una clase derivada llamada Animal que herede de SerVivo 
# y añada un método moverse que devuelva "Me estoy moviendo". 
# Finalmente, crea una clase derivada llamada Perro que herede 
# de Animal y sobrescriba el método moverse para devolver "Estoy corriendo". 
# Crea una instancia de Perro y muestra los resultados de los métodos.

"""class SerVivo():
    
    #Métodos
    def respirar(self):
        return 'Estoy respirando'

class Animal(SerVivo):
    
    #Métodos
    def moverse(self):
        return 'Me estoy moviendo'

class Perro(Animal):
    
    #Métodos
    def moverse(self):
        return 'Estoy corriendo'
    
perro = Perro()

print(perro.moverse())
print(perro.respirar())"""

# 3. - Crea una clase base llamada Dispositivo con un método encender que 
# devuelva "El dispositivo está encendido". 
# Luego, crea una clase derivada llamada Computadora que herede de Dispositivo 
# y añada un método procesar_datos que devuelva "Procesando datos". 
# Finalmente, crea una clase derivada llamada Laptop que herede de 
# Computadora y sobrescriba el método procesar_datos para devolver 
# "Procesando datos en la laptop". 
# Crea una instancia de Laptop y muestra los resultados de los métodos.

"""class Dispositivo():
    
    #Métodos
    def encender(self):
        return 'El dispositivo está encendido'
    
class Computadora(Dispositivo):
    
    #Métodos
    def procesar_datos(self):
        return 'Procesando datos'
    
class Laptop(Computadora):
    
    #Métodos
    def procesar_datos(self):
        return 'Procesando datos en la laptop'

laptop = Laptop()

print(laptop.encender())
print(laptop.procesar_datos())"""

# 4.- Crea una clase base llamada Vehiculo con un atributo marca y un método arrancar. 
# Luego, crea una clase derivada llamada Coche que herede de Vehiculo y añada 
# un atributo numero_puertas y un método abrir_puertas. 
# Crea una instancia de Coche y muestra sus atributos y métodos.

class Vehiculo:
    
    #Métodos
    def __init__(self, marca):
        self.marca = marca
        
    def arrancar(self):
        return 'El vehiculo está arrancando'
    
class Coche(Vehiculo):
    
    #Métodos
    def __init__(self, marca, numero_puertas):
        super().__init__(marca)
        self.numero_puertas = numero_puertas
    
    def abrir_puertas(self):
        return f'Abrir {self.numero_puertas} puertas'
    
coche = Coche('Cupra', 5)

print(f'Marca del coche: {coche.marca}')
print(coche.arrancar())
print(f'El coche tiene {coche.numero_puertas} puertas')
print(coche.abrir_puertas())