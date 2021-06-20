#Python principiantes - Modulo 3 - Laboratorio 3
#Consigna:
#Forzar el ingreso de solo números. Crear un programa que
#pida una edad, verificar que el ingreso por input sea un
#número entero. En caso contrario volver a pedir el ingreso.
#Después decidir si por la edad la persona es mayor o menor
#de edad.

def comprobacion_Edad():
    edad=input("Por favor ingrese su edad")
    comprobacion_entero=edad.isdecimal()
    while comprobacion_entero:

        
            print("el numero ingresado es valido") 
            break
    while comprobacion_entero is False:
        print("el numero ingresado es un decimal no valido")
        return
        

    edad_entero=int(edad)
    if edad_entero>=18:
        print("edad valida")
    else:
        print("no tiene la edad suficiente")

comprobacion_Edad()

