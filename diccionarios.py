
# dict       Key   : Value     Key     :  Value ....
alumno = { "nombre": "Pepe", "apellido": "Rodriguez", "edad": 30}

def saludar(un_alumno):
    print("Hola ", un_alumno["nombre"], un_alumno["apellido"], ". Como estas?")


saludar(alumno)

# Esto da KeyError, tengo que acceder al diccionario coon las keys
# for x in range(0, len(alumno)):
#    print(alumno[x])


for x in alumno:
    # print("El diccioanrio en", x, "es:", alumno.get(x))
    print(x, alumno.get(x))

# Puedo modificar los valores del diccionario:
nuevad_edad = input("Ingrese la nueva edad: ")

alumno["edad"] = nuevad_edad
print("La nueva edad ingresada es: ", alumno["edad"])
print(alumno)