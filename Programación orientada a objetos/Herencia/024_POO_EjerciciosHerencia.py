
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

"""class Vehiculo:
    
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
print(coche.abrir_puertas())"""

# 5.- Crea una clase base llamada Animal con un atributo nombre y un método hacer_sonido. 
# Luego, crea una clase derivada llamada Perro que herede de Animal y añada 
# un atributo raza y un método ladrar. Crea una instancia de Perro y muestra sus atributos y métodos.

"""class Animal():
    
    #Métodos
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return 'El animal hace un sonido'
    
class Perro(Animal):
    
    #Métodos
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
        
    def ladrar(self):
        return 'Ladrando'

perro = Perro('Bigotes', 'Salchicha')

# Mostrar atributos y métodos
print(perro.nombre)  # Hereda el atributo nombre
print(perro.hacer_sonido())  # Hereda el método hacer_sonido
print(perro.raza)  # Atributo propio de Perro
print(perro.ladrar())  # Método propio de Perro"""

# 6.- Crea una clase base llamada Persona con atributos nombre y edad, y un método saludar. 
# Luego, crea una clase derivada llamada Estudiante que herede de Persona y 
# añada un atributo carrera y un método estudiar. 
# Crea una instancia de Estudiante y muestra sus atributos y métodos.

"""class Persona():
    
    #Métodos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
class Estudiante(Persona):
    
    #Métodos
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        
    def estudiar(self):
        return f'Estoy estudiando {self.carrera}'
    
# Crear una instancia de Estudiante
estudiante = Estudiante("Pedro", 18, "Ingeniería")

# Mostrar atributos y métodos
print(estudiante.nombre)  # Hereda el atributo nombre
print(estudiante.edad)  # Hereda el atributo edad
print(estudiante.saludar())  # Hereda el método saludar
print(estudiante.carrera)  # Atributo propio de Estudiante
print(estudiante.estudiar())  # Método propio de Estudiante"""

# 7.- Crea una jerarquía de clases para un sistema de trabajo en una empresa. 
# Comienza con una clase base Persona (abuelo), luego crea una clase 
# derivada Empleado (padre) que herede de Persona, y finalmente, una 
# clase Gerente (hija) que herede de Empleado. 
# Además, añade una clase Habilidad que represente habilidades adicionales 
# que un empleado puede tener. 
# Haz que Gerente herede tanto de Empleado como de Habilidad (herencia múltiple).

# Asegúrate de:

# Utilizar atributos y métodos en cada clase.
# Sobrescribir métodos en las clases derivadas.
# Utilizar super() para llamar a métodos de las clases base.
# Mostrar el uso de la herencia múltiple.

# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Clase derivada de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad) 
        self.salario = salario

    def presentarse(self):
        # Sobrescribir método presentarse y usar super()
        return super().presentarse() + f" Soy empleado y gano {self.salario} euros al año."

    def trabajar(self):
        return "Estoy trabajando."

# Otra clase base para herencia múltiple
class Habilidad:
    def __init__(self, habilidades):
        self.habilidades = habilidades

    def mostrar_habilidades(self):
        return f"Tengo las siguientes habilidades: {', '.join(self.habilidades)}"

# Clase derivada de Empleado y Habilidad (herencia múltiple)
class Gerente(Empleado, Habilidad):
    def __init__(self, nombre, edad, salario, habilidades, departamento):
        Empleado.__init__(self, nombre, edad, salario)
        Habilidad.__init__(self, habilidades)
        self.departamento = departamento

    def presentarse(self):
        # Sobrescribir método presentarse y usar super() para Empleado y Persona
        return super().presentarse() + f" Soy gerente del departamento de {self.departamento}."

    def trabajar(self):
        # Sobrescribir método trabajar
        return "Estoy supervisando a los empleados."

# Crear instancias y mostrar el uso de los métodos
persona = Persona("Juan", 50)
empleado = Empleado("Ana", 30, 35000)
gerente = Gerente("Carlos", 40, 60000, ["Liderazgo", "Gestión de proyectos"], "IT")

# Mostrar presentaciones
print(persona.presentarse())
print(empleado.presentarse())
print(gerente.presentarse())

# Mostrar trabajo
print(empleado.trabajar())
print(gerente.trabajar())

# Mostrar habilidades del gerente
print(gerente.mostrar_habilidades())