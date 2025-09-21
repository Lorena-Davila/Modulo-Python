"""
Nombres y Apellidos: Lorena Sofia Davila Anchivilca
Requisitos:

1. Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string que contiene
valor numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable numérica.
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica
 y la variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado de la parte entera de los variables enteras: //
6. Obtener una potencia usando una de las variables flotantes y la variable entera como potencia
"""""

# 1. Crear variables
entero1 = 15
entero2 = 4
flotante1 = 6.5
flotante2 = 3.7
cadena1 = "Sofia"
cadena2 = "Davila"
cadena_num = "9"
booleano = True

# 2. Suma de una variable entera con la variable numérica
suma1 = entero1 + int(cadena_num)
print("Suma de entero1 + cadena_num:", suma1)

# 3. Suma de 2 enteros + string numérico (convertido) + flotante
suma2 = entero1 + entero2 + int(cadena_num) + flotante1
print("Suma de entero1 + entero2 + cadena_num + flotante1:", suma2)

# 4. Módulo de las variables enteras
modulo = entero1 % entero2
print("Módulo (entero1 % entero2):", modulo)

# 5. Parte entera de la división entre enteros
division_entera = entero1 // entero2
print("Parte entera (entero1 // entero2):", division_entera)

# 6. Potencia usando flotante y un entero como exponente
potencia = flotante1 ** entero2
print("Potencia (flotante1 ** entero2):", potencia)
