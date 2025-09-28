"""
Participación
"""
"""Programación funcional"""

"""
Requisitos:
- Crear una función que multiplicará 4 valores (int y floats)
- La función tendrá un parámetro o que contendrá un valor
- Mostrar 2 casos donde ese ingresó los valores donde uno no afectará el valor del parámetro
que ya contiene un valor y otro donde si lo estará afectando

correo: docente.cerseu.unmsm@gmail.com
asunto: Participación para práctica 02
tiempo máximo de entrega: sábado 27 11:59 pm
Enviar en un mismo correo: ejercicio_07, ejercicio_12 y ejercicio_20
"""
def multiplicar(a, b, c, d=2.5):
    return a * b * c * d

resultado_1 = multiplicar(0.25, 3,5 )
print("El parámetro 'd' mantiene su valor por defecto 2.5 siendo el resultado:", resultado_1)

resultado_2 = multiplicar(2, 3, 4, 1.25)
print("El parámetro 'd' se modifica y ahora vale 1.25 siendo el resultado:", resultado_2)
