from Inventario import Inventario
from Producto import Producto

inventario = Inventario()

seguir = True

while seguir != False:
    """
    Menú principal.
    """
    print("\n" + "="*35)
    print(" Sistema de Gestión de Inventario ")
    print("="*35)
    print("1. Agregar un producto")
    print("2. Actualizar un producto")
    print("3. Eliminar un producto")
    print("4. Mostrar inventario")
    print("5. Buscar un producto")
    print("6. Salir")
    print("="*35)
    
    op = input('Selecciona una opción: ')
    
    if op == '1':
        
        inventario.agregar_producto()

    elif op == '2':
        nombre = input('Introduce el nombre del producto a modificar: ')
        
        try:
            inventario.actualizar_producto(nombre)
        except ValueError as e:
            print(e)
            
    elif op == '3':
        nombre = input('Introduce el nombre del producto a eliminar: ')
        
        try:
            inventario.eliminar_producto(nombre)
        except ValueError as e:
            print(e)
    
    elif op == '4':
        inventario.mostrar_inventario()
        
    elif op == '5':
        nombre = input('Introduce el nombre del producto que quieres buscar: ')
        
        try:
            inventario.buscar_producto(nombre)
        except ValueError as e:
            print(e)
    
    elif op == '6':
        print('Saliendo de la gestión de inventario')
        seguir = False
    
    else:
        print('Introduce una opción válida')