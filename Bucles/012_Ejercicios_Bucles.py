# 1.- Escribe un programa que sume todos los números enteros del 1 al 100 usando un bucle for.

"""suma = 0

for i in range (1, 101):
    suma += i
    
print(suma)"""

# 2.- Utiliza un bucle for para generar e imprimir la lista de los cuadrados 
# de los primeros 10 números enteros (1 al 10).

"""lista = []

for num in range(1, 11):
    lista.append(num*num)
    
print(lista)"""

# 3.- Dado un string, utiliza un bucle for para contar cuántas veces aparece la 
# letra 'a' en el string.

"""linea = input('Escribe algo: ')
contador = 0

for i in linea:
    if i == 'a':
        contador += 1
        
print(f'La letra a aparece: {contador} veces en la palabra {linea}')"""

# 4.- Escribe un programa que imprima la tabla de multiplicar del número 7, 
# desde el 7x1 hasta el 7x10, usando un bucle for.

"""for i in range (1, 11):
    print(f'7x{i} = {7*i}')"""


# 5. - Escribe un script que cuente desde 1 hasta un número n proporcionado por 
# el usuario, imprimiendo cada número.

"""numero = int(input('Escribe un numero: '))
lista = []
i = 0

while (i != numero):
    i += 1
    lista.append(i)

print(lista)"""


# 6.- Crea un programa que sume números introducidos por el usuario hasta que el 
# usuario introduzca 0. Al final, el programa debe mostrar la suma total.

"""salir = False
suma = 0

while salir != True:
    num = int(input('Introduce tantos numeros como quieras (0 para salir): '))
    if num != 0:
        suma += num
    else:
        salir = True
    
print(f'La suma total es {suma}')"""


# 7.- Implementa un programa que le pida al usuario introducir números hasta que 
# introduzca el número 5. Cuando eso ocurra, el programa debe imprimir un 
# mensaje indicando que se encontró el número 5

"""salir = False

while salir != True:
    num = int(input('Introduce tantos numeros como quieras: (5 para salir)'))
    if num == 5:
        print('Se encontró el número 5')
        salir = True"""
        
# 8.- Escribe un script que solicite al usuario su edad y asegúrate de que el 
# número proporcionado esté entre 1 y 100. Si el número está fuera de ese rango, 
# pídele que lo introduzca nuevamente.

salir = False

while salir != True:
    edad = int(input('Introduce tu edad: '))
    
    if edad < 1 or edad > 100:
        print('Introduce una edad válida')
    else: 
        print('Edad válida')
        salir = True
    
    