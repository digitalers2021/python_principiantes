# Clase 4
# funciones
# una funcion puede tener parametros de entrada y de salida (E/S, I/O)

# puedo definir una funcion con la palabra reservada "def"
def saludar():
    print("Hola mundo!")

# Vemos entonces que se neceista definir primero la funcion,
# y luego recien podemos llamar
saludar()


# parametrizacion
# como vimos con mi_lista.sort(reverse=True)
def saludar_params(mensaje):
    print("EL mensaje es: ", mensaje)

mi_parametro = "Chau mundo"
saludar_params(mi_parametro)

saludar_params(mensaje="Es otro mensaje")
saludar_params(mensaje=mi_parametro)

def saludar_defect(mensaje="Hola mundo!"):
    print(mensaje)


saludar_defect()
saludar_defect(mensaje="Te cambio el valor por defecto")

saludar_defect(len(mi_parametro))

# Valores de retorno
respuesta = saludar_params(mensaje="Otro saludo mas")
print("La respuesta de saludar_params(), es: ", respuesta)
print(type(respuesta))


