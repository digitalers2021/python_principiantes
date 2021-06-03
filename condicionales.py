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
        print("Es en asia, pero no cumple otras condiciones")
else: 
    print("No hay vacaciones")


# Agrego la condicion de que NO puede ser lluvioso
lluvioso = False
if lugar == "Asia" and (mes == "Marzo" or mar == False):
    if not lluvioso:
        print("Me voy para alla ya")
    else:
        print("Que lastima llegaste hasta aca.. pero es lluvioso")
else:
    print("No hay vacaciones para usted")



comprar_bebida = "juego tang" # cerveza, vodka, fernet, whisky, coca cola
if comprar_bebida == "vino":
    print("Bien la compro para tomar en casa")
elif comprar_bebida == "cerveza":
    print("Bien la compro para tomar en casa")
elif comprar_bebida == "vodka":
    print("Bien la compro para tomar en casa")
elif comprar_bebida == "fernet":
    print("Bien la compro para tomar en casa")
elif comprar_bebida == "whisky":
    print("Bien la compro para tomar en casa")
else:
    print("Caso default, no estas eligiendo una bebida con alcohol")

print("Fin del programa")