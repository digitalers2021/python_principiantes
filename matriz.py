# Clase 3 matrice
lista = [
    [0, 1, 2, 3],
    [4, 5, 6, 7]
    ]

print(lista[1])
print(type(lista[1]))
# ahora quiero acceder a la posicion:
# 1, 2 de mi matriz:
print(lista[1][2])


for filas in lista:
    for col in filas:
        print(col)

# Ranking de musica:
# Posicion, Nombre del Artista
# 1, Maluma
# 2, Blackpink
# 3, Calamaro
# 4, Radiohead

ranking  = [[1, "Maluma"], [2, "Blackpink"], [3, "Calamaro"], [4, "Radiohead"]]

for r in ranking:
    print("En la posicion: ", r[0], "El artista: ", r[1])

# Dos ejercicios:
# 1) Invertir el ranking, es decir
# quiero ver desde el ultimo al primero:

# 2) Tengo la siguiente lista
# [4, 5, 2, 7, 6, 101, 5, 5, 3]
# 
# Quiero saber cual es el numero mas alto?
# Y cual el mas bajo? 
# A todo esto quiero el indice o posicion del 
# numero mas alto o mas bajo

numeros = [4, 5, 2, 7, 6, 101, 5, 5, 3]
maximo = numeros[0]
indice_max = 0
for x in range(0, len(numeros)):
    if numeros[x] > maximo:
        maximo = numeros[x]
        indice_max = x

print("Mi maximo es: ", maximo)
print("Y esta en la posicion: ", indice_max)

# Resolucion ejercicio 1:
# 1) Invertir el ranking, es decir
# quiero ver desde el ultimo al primero:

ranking  = [[1, "Maluma"], [2, "Blackpink"], [3, "Calamaro"], [4, "Radiohead"]]
for x in ranking:
    print(x)

for x in range(0, len(ranking)):
    print(ranking[x])

#invertido = []
#for x in ranking:
#    invertido.append(x)

invertido = []
x = len(ranking) -1
while x >= 0:
    invertido.append(ranking[x])
    print(x)
    x -= 1 


print("Mi lista final es: ", invertido)
