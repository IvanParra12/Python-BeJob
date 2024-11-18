# 1.- Escribe un programa que pregunte al usuario su edad y muestre por pantalla 
# si es mayor de edad o no.

"""edad = int(input('Introduce tu edad: '))

if edad >= 18:
    print('Es mayor de edad')
else:
    print('No es mayor de edad')"""

# 2.- Una tienda ofrece descuentos basados en el total de compra. 
# Si la compra es mayor a $100, el descuento es del 10%. Si es mayor a $500, 
# el descuento es del 20%. Crea un programa que calcule el total a pagar 
# después del descuento.

"""compra = float(input('Introduce el total de la compra: '))

if compra >= 500:
    descuento = compra * 0.20
    print('El total a pagar es: ', compra - descuento)

elif compra >= 100:
    descuento = compra * 0.10
    print('El total a pagar es: ', compra - descuento)

else:
    print('El total a pagar es: ', compra)"""
    
# 3.- Solicita dos números al usuario y determina cuál de los dos es mayor o si son iguales.

"""num1 = int(input('Introduce el primer numero: '))
num2 = int(input('Introduce el segundo numero: '))

if num1 == num2:
    print('Los numeros son iguales')

else:
    if num1 < num2:
        print('El numero 2 es mayor que el numero 1')
    else:
        print('El numero 1 es mayor que el numero 2')"""

# 4.- Escribe un script que solicite una calificación al usuario (0 - 100). 
# Si la calificación es mayor o igual a 90, imprime "Excelente", si es mayor 
# o igual a 70 y menor que 90, imprime "Bueno", si es mayor o igual a 50 y 
# menor que 70, imprime "Suficiente", y si es menor que 50, imprime "Insuficiente".

"""calificacion = int(input('Introduce la calificacion (0-100): '))

if calificacion >= 90:
    
    print('Excelente')
    
elif calificacion >= 70 < 90:
    
    print('Bueno')
    
elif calificacion >= 50 < 70:
    
    print('Suficiente')
    
elif calificacion < 50:
    print('Insuficiente')"""
    
# 5.- Un almacén da un descuento del 15% si la compra del cliente supera los 1000 Euros. 
# Escribe un programa que pida el total de la compra y calcule el descuento 
# (si aplica) y el total a pagar.

"""compra = float(input('Introduce el total de la compra: '))

if compra > 1000:
    
    descuento = compra * 0.15
    
    print('El descuento es de ', descuento, '€')
    print('El total a pagar es de ', compra - descuento, '€')

else:
    print('El total a pagar es de ', compra, '€')"""
    
# 6.- Escribe un programa que pida al usuario un número del 1 al 7 y muestre el día 
# de la semana correspondiente. Si el número no está en ese rango, debe 
# indicar que el número es inválido.

"""numero = int(input('Introduce un número del 1 al 7: '))

if numero == 1:
    print('Lunes')
elif numero == 2:
    print('Martes')
elif numero == 3:
    print('Miércoles')
elif numero == 4:
    print('Jueves')
elif numero == 5: 
    print('Viernes') 
elif numero == 6:
    print('Sábado')
elif numero == 7: 
    print('Domingo')
else:
    print('Número inválido')"""
    
# 7.- Escribe un programa que pida la edad del usuario y clasifique a las personas en diferentes categorías (niño, adolescente, adulto, adulto mayor). Supón los siguientes rangos de edad:

# Niño: Menos de 13 años.
# Adolescente: De 13 a 19 años.
# Adulto: De 20 a 64 años.
# Adulto mayor: 65 años o más.

"""edad = int(input('Introduce tu edad: '))

if edad >= 65:
    
    print('Adulto mayor')
    
elif edad >= 20 < 64:
    
    print('Adulto')
    
elif edad >= 13 < 19:
    
    print('Adolescente')
    
elif edad < 13:
    print('Niño')"""


# 8.- Escribe un programa que sugiera qué ponerse basado en la temperatura actual 
# (en grados Celsius) que el usuario introduce. Considera:

# Menos de 10°C: Abrigo y bufanda.
# De 10°C a 20°C: Suéter ligero.
# Más de 20°C: Camiseta.

"""temp = int(input('Introduce la temperatura actual en grados Celsius: '))

if temp > 20:
    print('Podrías llevas una camiseta')
elif temp >= 10 < 20:
    print('Podrías llevar un suéter ligero')
elif temp < 10:
    print('Podrías llevar un abrigo y una bufanda')"""
    

# 9.- Programa un sistema que categorice los ingresos anuales de una persona 
# como 'bajo', 'medio' o 'alto'. Define tú mismo los límites de cada categoría.

ingresos = float(input('Introduce tus ingresos anuales brutos: '))

if ingresos < 20000:
    print("Tus ingresos son bajos.")
else:
    if ingresos < 50000:
        print("Tus ingresos son medios.")
    else:
        print("Tus ingresos son altos.")