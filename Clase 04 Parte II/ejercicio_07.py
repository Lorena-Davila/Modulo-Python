"""
Intervención
"""

"""Usando propiedades de string"""
"""
Requisitos:
- Ingresar su nombre y apellido por consola
(variables distintas)
- Obtener el tamaño de tu nombre completo y muéstralo en consola
- Imprimir el resultado final, todo en mayúsculas: .upper()
- Indicar mediante condicionales si el tamaño del nombre es mayor o no al apellido ingresado
- Solamente ingresar el apellido paterno

correo: docente.cerseu.unmsm@gmail.com
asunto: Participación para práctica 02
tiempo máximo de entrega: sábado 27 11:59 pm
Enviar en un mismo correo: ejercicio_07, ejercicio_12 y ejercicio_20
"""
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido paterno: ")

nombre_completo = nombre + " " + apellido

print("El tamaño de tu nombre completo es:", len(nombre_completo))

print("Tu nombre completo en mayúsculas es:", nombre_completo.upper())

if len(nombre) > len(apellido):
    print("El nombre es más largo que el apellido.")
elif len(apellido) > len(nombre):
    print("El apellido es más largo que el nombre.")
else:
    print("El nombre y el apellido tienen la misma cantidad de letras.")
