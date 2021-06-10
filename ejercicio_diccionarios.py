# Tarea:
# Pensar una manera mas eficiente de obtener alumnos en base a la matricula
# La matricula se debe poder ingresar por un input del programa pista: input()

# Lista de diccionarios
alumnos = [
    {"nombre": "Pepe", "apellido": "Perez", "matricula": 435},
    {"nombre": "Julieta", "apellido": "Rodriguez", "matricula": 233},
    {"nombre": "Maria", "apellido": "Rodriguez", "matricula": 123}
]

def listar_alumnos(lista_alumnos):
    for a in lista_alumnos:
        print(a["nombre"])

def obtener_alumno(matricula, lista_alumnos):
    for a in lista_alumnos:
        if a['matricula'] == matricula:
            return a


listar_alumnos(alumnos)
print(alumnos)
mi_alumno = obtener_alumno(435, alumnos)
print(mi_alumno)