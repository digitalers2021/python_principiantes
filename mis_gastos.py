# Estos son mis gastos
"""
Esto tambien es un comentario
pero me permite escribir un parrafo
mas extenso.
"""

# Python es un lenguaje que pretende ser simple
# https://es.wikipedia.org/wiki/Zen_de_Python
netflix = 5 ;
spotify = 5;
dolar = 150;
mis_gastos = (netflix + spotify) * dolar
print(mis_gastos)

print("Otra forma de mostrar mis gastos puede ser:")
print((netflix + spotify) * dolar)

# Aca vemos como podemos trabajar con variables
# y texto
Hola = "pepe"
saludo = "Hola mundo!"
print(saludo)

# Tipo de variables
# mensaje = saludo + mis_gastos # Esto da error porque son tipos de dato distintos
# print(mensaje)

# Tipo de datos basicos en python
# entero = int (integer)
# real = float (decimal)
# binario = bool (True or false, (1,0))
# texto = str (string)

# si yo quiero saber cuanto gasto por dia

cuanto_gasto_por_dia = mis_gastos / 30
print(cuanto_gasto_por_dia)

print("==== ACA HAGO LA DIVISION: ====")
cuanto_gasto_por_dia = mis_gastos / 31
print(cuanto_gasto_por_dia)
print(type(cuanto_gasto_por_dia))


print("==== ACA REASIGNO LA VARIABLE a otro tipo ====")
# yo puedo reasignar una variable Y CAMBIAR SU TIPO
cuanto_gasto_por_dia = "GASTAS UN MONTON de guita"
print(cuanto_gasto_por_dia)
# Hay palabras que son reservadas del lenguaje como
# por ej: "if"
# if = "pepe"  X esto no se puede

# Type
print(type(cuanto_gasto_por_dia))


# Tipo de dato bool
# ! CUIDADO es case sensitive
flag = True
night = False
print(type(flag))
print(type(night))


# Operadores logicos

(5 > 1) and (10 < 20) # esto es TRUE
# V            V      = V
(10 != 10) and (10 < 20) #
# F                F   = F

hoy = "Lunes"
gastos_mes = (netflix + spotify) * dolar
if gastos_mes < 2500:  # gastos_mes = 1500
    if hoy == "Miercoles":
        print("Pagar suscripcion")
        print(gastos_mes)
    else:
        print("Solo podemos suscribirnos los miercoles")
else:
    print("Conseguite un mejor trabajo porque no te alcanza")
    print(gastos_mes)





    print("FIN DEL PROGRAMA") # ESTO no SALE por la identicacion

print("ESTE SI ES EL FIN DEL PROGRAMA")

## Voy a decidir si me voy de vacaciones
# mis requirimientos son:
# Que sea asia
# QUe sea en julio o que haya mar
#
# ME fijo el mapa, y veo que India tiene:
lugar = "Asia" 
mes = "Marzo"
mar = False

if lugar == "Asia":
    if mes == "Julio" or mar == True:
        print("Me voy para alla ya")
else: 
    print("No hay vacaciones")


