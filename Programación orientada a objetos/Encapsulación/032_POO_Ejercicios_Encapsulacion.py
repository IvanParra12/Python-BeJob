# 1.- Crea una clase CuentaBancaria que tenga un atributo privado __saldo. 
# Implementa un método getter llamado get_saldo que devuelva el saldo actual. 
# Crea una instancia de CuentaBancaria y muestra el saldo usando el método getter.

"""class CuentaBancaria():
    
    #Métodos
    def __init__(self, saldo):
        self.__saldo = saldo
        
    #Getter
    def get_saldo(self):
        return self.__saldo

cuentaBancaria = CuentaBancaria(100)

print("Saldo inicial:", cuentaBancaria.get_saldo())"""


# 2.- Modifica la clase CuentaBancaria para que tenga un método setter llamado set_saldo 
# que permita modificar el saldo solo si el nuevo saldo es positivo. 
# Usa este método para intentar establecer un saldo negativo y observa el resultado.

"""class CuentaBancaria():
    
    #Métodos
    def __init__(self, saldo):
        self.__saldo = saldo
        
    #Getter
    def get_saldo(self):
        return self.__saldo
    
    #Setter
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("El saldo no puede ser negativo.")

cuentaBancaria = CuentaBancaria(100)
cuentaBancaria.set_saldo(-50)

print("Saldo Modificado:", cuentaBancaria.get_saldo())"""

# 3.- Crea una clase Empleado que tenga un atributo protegido _sueldo y un método 
# público mostrar_sueldo que imprima el sueldo. Crea una instancia de Empleado 
# y llama al método mostrar_sueldo.

"""class Empleado():
    
    #Métodos
    def __init__(self, sueldo):
        self._sueldo = sueldo
        
    def mostrar_sueldo(self):
        return self._sueldo
    
empleado = Empleado(1000)
print("Sueldo del empleado: ", empleado.mostrar_sueldo())"""

# 4.- Crea una clase Estudiante con atributos privados __nombre y __nota. 
# Implementa métodos getter para ambos atributos y un método setter para __nota 
# que solo permita valores entre 0 y 10. Crea una instancia de Estudiante, 
# establece y muestra sus valores usando los métodos adecuados.

"""class Estudiante():
    
    #Métodos
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota
    
    #Getter
    def get_nombre(self):
        return self.__nombre
    
    def get_nota(self):
        return self.__nota
    
    #Setters
    def set_nota(self, nota_nueva):
        
        self.__nota = nota_nueva if (nota_nueva >= 0 and nota_nueva <= 10) else "Valor incorrecto"
        
    
estudiante = Estudiante('Carlos Pérez Montoya', 8)
estudiante.set_nota(10)

print(f'Estudiante: {estudiante.get_nombre()}, nota: {estudiante.get_nota()}')"""

# 5.- Crea una clase Libro con un atributo privado __titulo y un método 
# privado __mostrar_titulo que imprime el título del libro. 
# Implementa un método público leer_titulo que llame al método 
# privado __mostrar_titulo. 
# Crea una instancia de Libro y llama al método leer_titulo.

"""class Libro():
    
    #Métodos
    def __init__(self, titulo):
        self.__titulo = titulo
        
    def __mostrar_titulo(self):
        return self.__titulo
    
    def leer_libro(self):
        return self.__mostrar_titulo()
    
libro = Libro('IT')
print(f'Titulo del libro: {libro.leer_libro()}')"""

# 6.- Crea una clase Zapatilla que tenga un atributo privado __color. 
# Implementa métodos getter y setter para el color, donde el setter 
# solo permita los colores "blanco", "negro" y "rojo". 
# Si se intenta establecer un color no válido, muestra un mensaje 
# indicando que el color no es válido y pide al usuario que elija 
# un color válido. 
# Crea una instancia de Zapatilla, permite al usuario elegir un color 
# y muestra el color de la zapatilla.

"""class Zapatilla():
    
    #Métodos
    def __init__(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color_nuevo):
        
        if color_nuevo in ["blanco", "negro", "rojo"]:
            
            self.__color = color_nuevo
        
        else:
            
            print('Color inválido')
            

zapato = Zapatilla('blanco')
print(f'Color inicial de la zapatilla: {zapato.get_color()}')

color = ""

while color not in ["blanco", "negro", "rojo"]:
    color = input('Introduce el color de la zapatilla: ').strip().lower()
    zapato.set_color(color)
    print(f'Color final de la zapatilla: {zapato.get_color()}')"""
    

# 7.- Crea una clase Zapatilla que tenga los atributos privados 
# __color, __precio, __talla y __stock. 
# Implementa métodos getter y setter para el color, la talla y el stock. 
# El setter del color solo permite "blanco", "negro" y "rojo", y el setter 
# de la talla permite tallas entre 36 y 45. El setter del stock debe aceptar 
# solo valores positivos. 
# El precio depende del color: "blanco" (60€), "negro" (65€) y "rojo" (70€). 
# Si el color, la talla o el stock no son válidos, muestra un mensaje indicando el error. 
# Crea una instancia de Zapatilla, permite al usuario elegir el color, 
# la talla y el stock, y muestra los detalles de la zapatilla.

class Zapatilla():
    
    #Métodos
    def __init__(self, color, talla, stock):
        self.__color = color
        self.__talla = talla
        self.__stock = stock
        self.__precio = self.__set_precio(color)
        
    #Getters
    def get_color(self):
        return self.__color
    
    def get_talla(self):
        return self.__talla
    
    def get_stock(self):
        return self.__stock
    
    def get_precio(self):
        return self.__precio
    
    #Setters
    def set_color(self, color_nuevo):
        
        if color_nuevo in ["blanco", "negro", "rojo"]:
            
            self.__color = color_nuevo
            self.__precio = self.__set_precio(color_nuevo)
        
        else:
            
            print('Color inválido')
            
    def set_talla(self, tallaNueva):
        
        if tallaNueva >= 36 and tallaNueva <= 45:
            self.__talla = tallaNueva
        else:
            print('Introduce una talla entre 36 y 45')   
    
    def set_stock(self, stockNuevo):
        
        if stockNuevo > 0:
            self.__stock = stockNuevo
        else:
            print('Introduce un valor de stock positivo')
            
    def __set_precio(self, color):
        precios = {
            "blanco": 60,
            "negro": 65,
            "rojo": 70
        }
        return precios.get(color, 0)
            
zapatilla = Zapatilla('verde', 37, 1)

# Mostrar el color, la talla, el stock y el precio iniciales
print(f"Color inicial de la zapatilla: {zapatilla.get_color()}, Talla: {zapatilla.get_talla()}, Stock: {zapatilla.get_stock()}, Precio: {zapatilla.get_precio()}€")

# Permitir al usuario elegir un nuevo color
nuevo_color = input("Elige un color para la zapatilla (blanco, negro, rojo): ").strip().lower()
zapatilla.set_color(nuevo_color)

# Intentar establecer un color hasta que sea válido
while zapatilla.get_color() != nuevo_color:
    nuevo_color = input("Elige un color para la zapatilla (blanco, negro, rojo): ").strip().lower()
    zapatilla.set_color(nuevo_color)
    
# Permitir al usuario elegir una nueva talla
nueva_talla = int(input("Elige una talla para la zapatilla (36-45): ").strip())
zapatilla.set_talla(nueva_talla)
    
# Intentar establecer una talla hasta que sea válida
while zapatilla.get_talla() != nueva_talla:
    nueva_talla = int(input("Elige una talla para la zapatilla (36-45): ").strip())
    zapatilla.set_talla(nueva_talla)

# Permitir al usuario elegir una nueva cantidad en stock
nuevo_stock = int(input("Elige la cantidad en stock para la zapatilla: ").strip())
zapatilla.set_stock(nuevo_stock)

# Intentar establecer una cantidad en stock hasta que sea válida
while zapatilla.get_stock() != nuevo_stock:
    nuevo_stock = int(input("Elige la cantidad en stock para la zapatilla: ").strip())
    zapatilla.set_stock(nuevo_stock)

# Mostrar el color, la talla, el stock y el precio final de la zapatilla
print(f"Color final de la zapatilla: {zapatilla.get_color()}, Talla: {zapatilla.get_talla()}, Stock: {zapatilla.get_stock()}, Precio: {zapatilla.get_precio()}€")
