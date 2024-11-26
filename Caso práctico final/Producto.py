#Clase Producto

class Producto():
    
    #Constructor
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = self.validar_string(nombre)
        self.__categoria = self.validar_string(categoria)
        self.__precio = self.validar_precio(precio)
        self.__cantidad = self.validar_cantidad(cantidad)
        
    def __str__(self):
        return f'Nombre del producto: {self.get_nombre()}, categoria: {self.get_categoria()}, precio: {self.get_precio()}€, cantidad en stock: {self.get_cantidad()}'
    #Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_categoria(self):
        return self.__categoria
    
    def get_precio(self):
        return self.__precio
    
    def get_cantidad(self):
        return self.__cantidad
    
    #Setters
    def set_nombre(self, nombreNuevo):
        self.__nombre = self.validar_string(nombreNuevo)
        
    def set_categoria(self, categoriaNueva):
        self.__categoria = self.validar_string(categoriaNueva)
    
    def set_precio(self, precioNuevo):
        self.__precio = self.validar_precio(precioNuevo)
    
    def set_cantidad(self, cantidadNueva):
        self.__cantidad = self.validar_cantidad(cantidadNueva)
        
    #Métodos de validación
    @staticmethod
    def validar_string(valor):
        if valor.isnumeric():
            raise TypeError("El nombre o la categoria deben ser un string")
        
        if not valor.strip():
            raise ValueError("El valor no puede estar vacío")
        return valor

    
    @staticmethod
    def validar_precio(precio):
        if not isinstance(precio, float):
            raise TypeError('Introduce un valor válido (float)')
        if precio <= 0:
            raise ValueError("Introduce un precio mayor que 0")
        return precio
    
    @staticmethod
    def validar_cantidad(cantidad):
        if not isinstance(cantidad, int):
            raise TypeError('Introduce un valor válido (int)')
        if cantidad < 0:
            raise ValueError("Introduce una cantidad mayor o igual a 0")
        return cantidad