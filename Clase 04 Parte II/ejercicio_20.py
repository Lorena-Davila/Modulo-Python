"""Manejo de errores"""
"""
Requisitos:
- Crear una función la cuál va a evaluar una lista y un índice
- Habrá una exepción donde dentro de la función que sa a considerar 
una lista con 4 valores
- Cuando se va a modificar una de las posiciones no existentes
crear un nuevo índice y darle un valor de 0
- Mostrar la lista final

correo: docente.cerseu.unmsm@gmail.com
asunto: Participación para práctica 02
tiempo máximo de entrega: sábado 27 11:59 pm
Enviar en un mismo correo: ejercicio_07, ejercicio_12 y ejercicio_20
"""
def evaluar_lista(indice):
    lista = [10, 20, 30, 40]

    try:
        lista[indice] = lista[indice] + 1
        print("Lista actualizada:", lista)

    except IndexError:
        print("El índice", indice, "no existe, se creará con valor 0")
        lista.append(0)
        print("Lista actualizada:", lista)

    finally:
        print("Operación finalizada\n")

evaluar_lista(2)
evaluar_lista(4)

