from Producto import Producto

class Inventario():
    
    # Constructor
    def __init__(self):
        self.__productos = []
    
    # Getter
    def get_productos(self):
        return self.__productos
    
    # Agregar un producto
    def agregar_producto(self):
        try:
            # Capturar datos
            nombre = input('Introduce el nombre del producto: ')
            categoria = input('Introduce la categoria del producto: ')
            precio = float(input('Introduce el precio del producto: '))
            cantidad = int(input('Introduce la cantidad de stock del producto: '))

            # Validar datos
            nombre_validado = Producto.validar_string(nombre)
            categoria_validada = Producto.validar_string(categoria)
            precio_validado = Producto.validar_precio(precio)
            cantidad_validada = Producto.validar_cantidad(cantidad)

            # Crear producto validado
            producto = Producto(nombre_validado, categoria_validada, precio_validado, cantidad_validada)

            # Verificar duplicados
            for i in self.get_productos():
                if i.get_nombre().strip().lower() == producto.get_nombre().strip().lower():
                    raise ValueError('Producto ya introducido, intenta agregar uno nuevo')

            # Agregar al inventario
            self.__productos.append(producto)  # Usamos el atributo privado
            print('Producto introducido correctamente!')

        except (ValueError, TypeError) as e:
            print(f"Error al agregar el producto: {e}")
    
    # Actualizar un producto
    def actualizar_producto(self, nombre_producto):
        producto = None
        
        for i in self.get_productos():
            if i.get_nombre() == nombre_producto:
                producto = i
                break
        
        if not producto:
            raise ValueError('El producto no existe en el inventario')
        
        print("¿Qué desea modificar del producto?")
        print("1. Precio")
        print("2. Cantidad en stock")
        op = int(input("Ingrese el número de su elección: "))
        
        if op == 1:
            precio = float(input('Introduce el nuevo precio: '))
            try:
                precio_validado = Producto.validar_precio(precio)
                producto.set_precio(precio_validado)
                print('Precio actualizado correctamente!')
            except (ValueError, TypeError) as e:
                print(f'No se ha podido actualizar el precio: {e}')
                
        elif op == 2:
            cantidad = int(input('Introduce la nueva cantidad de stock: '))
            try:
                cantidad_validada = Producto.validar_cantidad(cantidad)
                producto.set_cantidad(cantidad_validada)
                print('Cantidad de stock actualizada correctamente!')
            except (ValueError, TypeError) as e:
                print(f'No se ha podido actualizar la cantidad: {e}')
        
        else:
            print('Introduce una opción válida (1 o 2)')
    
    # Eliminar producto por nombre    
    def eliminar_producto(self, nombre_producto):
        try:
            nombre_validado = Producto.validar_string(nombre_producto)
        except ValueError as e:
            print(e)
            
        producto = None
        
        for i in self.get_productos():
            if i.get_nombre() == nombre_validado:
                producto = i
                break
        
        if not producto:
            raise ValueError('El producto no existe en el inventario')
        
        try:
            self.__productos.remove(producto)
            print('Producto borrado correctamente!')
        except (ValueError, TypeError) as e:
                print(f'No se ha podido borrar el producto: {e}')
    
    # Mostrar inventario
    def mostrar_inventario(self):
        if not self.get_productos():
            print('El inventario está vacío!')
        else:
            for producto in self.get_productos():
                print(producto)
    
    # Buscar producto por nombre
    def buscar_producto(self, nombre_producto):
        try:
            nombre_validado = Producto.validar_string(nombre_producto)
        except ValueError as e:
            print(e)
            
        producto = None
        
        for i in self.get_productos():
            if i.get_nombre() == nombre_validado:
                producto = i
                break
        
        if not producto:
            raise ValueError('El producto no existe en el inventario')
        
        print(f'Producto encontrado: {producto}')              
        
                
                
                
            