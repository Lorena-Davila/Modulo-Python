"""
Lista de python - Participación
"""
"""
Requisitos:
- Crear dos listas vacías
- Agregar los datos de nombre, apellido paterno, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edades de ambas listas
- Sumar las listas y mostrar el resultado en la terminal
- Mostrar de forma inversa la suma de ambas listas
- Actualizar la nueva lista eliminando la edad de la primera y el apellido del segundo
(Utilizar cualquiera de los métodos de eliminación)
- Actualizar la profesión del segundo usuario
"""

"""
Actualización de valores por índice en la lista
usuario_2[2] = 35
usuario_1[0] = "Mario" 
print(usuario_2)
print(usuario_1)
"""


"""
Hora de entrega máxima: 6:00 pm
Correo: docente.cerseu.unmsm@gmail.com
Asunto: Participación a práctica 02
Adjuntar su archivo .py con su solución
"""
lista1 = []
lista2 = []

lista1.extend(["Lorena", "Davila", 20, "Estadistico"])
lista2.extend(["Anthony", "Carrillo", 30, "Ingeniero"])

print("Lista 1:", lista1)
print("Lista 2:", lista2)

suma_edades = lista1[2] + lista2[2]
print("La suma de las edades es:", suma_edades)

lista_total = lista1 + lista2
print("Lista nueva lista:", lista_total)

# Mostrar de forma inversa la nueva lista
lista_total.reverse()
print("Mostrar nueva lista de forma inversa:",lista_total)

# Eliminar la edad del primer usuario (índice 2)
#    y el apellido del segundo usuario (índice 5 en lista_total)
del lista_total[2]
del lista_total[4]

print("Lista después de eliminar edad y apellido:", lista_total)

# Actualizar la profesión del segundo usuario
lista_total[-1] = "Profesor"

print("Lista actualizada:", lista_total)