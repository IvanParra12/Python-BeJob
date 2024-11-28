# 1.- Crea una clase DivisorSeguro con un método divide que realice una división entre dos números 
# y maneje la excepción de división por cero.

"""class DivisionPorCeroError(Exception):
    def __init__(self, mensaje="No se puede dividir entre cero"):
        super().__init__(mensaje)

class DivisorSeguro:
    def divide(self, num1, num2):
        try:
            if num2 == 0:
                raise DivisionPorCeroError()
            return num1 / num2
        except DivisionPorCeroError as e:
            print(f"Error: {e}")
            
# Ejemplo de uso
divisor = DivisorSeguro()
print(divisor.divide(10, 2))  # Salida esperada: 5.0
print(divisor.divide(10, 0))  # Salida esperada: Error: No se puede dividir entre cero"""

# 2.- Crea una clase Persona con un método set_edad que valide que la edad no sea negativa. 
# Si se proporciona una edad negativa, lanza una excepción personalizada.

"""class EdadNegativaError(Exception):
    def __init__(self, mensaje="La edad no puede ser negativa"):
        super().__init__(mensaje)

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = None

    def set_edad(self, edad):
        try:
            if edad < 0:
                raise EdadNegativaError()
            self.edad = edad
        except EdadNegativaError as e:
            print(f"Error: {e}")

# Ejemplo de uso
persona = Persona("Juan")
persona.set_edad(25)  # Salida esperada: Ningún error
print(persona.edad)  # Salida esperada: 25
persona.set_edad(-5)  # Salida esperada: Error: La edad no puede ser negativa"""

# 3.- Crea una clase Calculadora con un método calcula_raiz que calcule la raíz cuadrada de un número. 
# Si el número es negativo, lanza una excepción personalizada.

"""import math

class ExcepcionNumeroNegativo(Exception):
    
    #Constructor
    def __init__(self, mensaje = 'El número no puede ser negativo'):
        super().__init__(mensaje)
        
class Calculadora():
    
    #Métodos
    def calcula_raiz(self, num):
        
        try:
            if num < 0:
                raise ExcepcionNumeroNegativo
            
            return math.sqrt(num)
        
        except ExcepcionNumeroNegativo as e:
            print(e)
            
# Ejemplo de uso
calc = Calculadora()
print(calc.calcula_raiz(16))  # Salida esperada: 4.0
print(calc.calcula_raiz(-4))  # Salida esperada: Error: No se puede calcular la raíz cuadrada de un número negativo"""

# 4.- Crea una clase IngresoSeguro con un método solicitar_numero que solicite al 
# usuario ingresar un número entero. Si el usuario ingresa un valor no numérico, 
# maneja la excepción y vuelve a solicitar el número.

"""class IngresoSeguro():
    
    #Métodos
    def solicitar_numero(self):
        
        while True:
            
            try:
                num = int(input('Introduce un número: '))
                return num
            
            except ValueError:
                print('No se pueden introducer valores no numéricos')

# Ejemplo de uso
ingreso = IngresoSeguro()
numero = ingreso.solicitar_numero()  # Salida esperada: Sigue solicitando hasta que se ingrese un número entero
print(f"Número ingresado: {numero}")"""

# 5.- Crea una clase ArchivoSeguro con un método leer_archivo 
# que intente leer un archivo de texto. Si el archivo no existe, 
# maneja la excepción e informa al usuario.

class ArchivoSeguro():
    
    #Métodos
    def leer_archivo(self, nombre_archivo):
        
        try:
            with open(nombre_archivo, 'r') as archivo:
                return archivo.read()
            
        except FileNotFoundError:
            print('Archivo no encontrado')

# Ejemplo de uso
archivo_seguro = ArchivoSeguro()
contenido = archivo_seguro.leer_archivo("archivo.txt")  # Salida esperada: Error: El archivo no fue encontrado si el archivo no existe
print(contenido)