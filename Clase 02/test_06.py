"""
Requisitos:

1. Crear dos variables para los valores de nombre, profesión y ciudad
2. Crear dos variables para la remuneración de enero y febrero (mayor a 1500)
3. Crear 1 variable donde se sumará el ingreso de los dos meses, enero y febrero
4. Mostrar en pantalla el siguiente mensaje (Output):

"Hola soy 'nombre', soy 'profesión' y mi remuneración acumulada es de 'remunera_total'"

"""

nombre = "Lorena"
prof = "Estadistico"
ciudad = "Lima"

remuneracion_enero = 1600
remuneracion_febrero = 1800
remunera_total = remuneracion_enero + remuneracion_febrero

print("Hola soy {}, soy {} y mi remuneración acumulada es de {}".format(nombre, prof, remunera_total))
