"""
Requisitos:

1. Crear 4 variables, entre enteros, booleans, string.
2. Realizar el uso de condicionales de las variables, para 2 casos true y 2 casos false.
3. En casos que valide True imprimir el valor de las otras dos variables.
4. En dos condicionales comparar entre variables (< >)

"""
"Enteros"
var_01 = -3
var_02 = 6
"booleans"
var_03 = True
var_04 = False
"string"
var_05 = "diferentes"

if var_01 < var_02:
    print("-3 < 6 es: {}".format(var_03))

if not var_01 > var_02:
    print("-3 > 6 es: {}".format(var_04))

if not var_01 >= var_02:
    print("-3 >= 6 es: {}".format(var_04))

if var_01 < var_02:
    print("-3==6 son:", var_05)


