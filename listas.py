# Clase 4
# Listas

lista_super = ["pan", "leche", "jamon", "jamon","galletitas"]

print(lista_super[0])
print("verifico que el tipo de dato de mi elemento en la lista es string")
print(type(lista_super[0]))
print("Y lista que tipo de dato es?")
print(type(lista_super))

print(lista_super[2])

## READ o leer 
for x in range(0, len(lista_super)):
    print(lista_super[x])

## Crear
lista_super.append("coca cola")
print("Agrego un elemento: ")
for x in range(0, len(lista_super)):
    print(lista_super[x])

# me permite sacar elementos
item = lista_super.pop()
print(item)


# y le podemos pasar pop("pan") ? 
# para que sea mas rapido
for x in range(0, len(lista_super)):
    if lista_super[x] == "jamon":
        print("Me encontraste en el indice: ", x)

te_encontre = False
indice = 0
while (te_encontre is False) and (indice < len(lista_super)):
    if lista_super[indice] == "jamon":
        te_encontre = True

    print("Indice en el while: ", indice)
    indice += 1

print("Se encontro?", te_encontre)
print("Indice: ", indice)

## otra forma de recorrer una lista 
# es con for in
for x in lista_super:
    print(type(x))
    print(x)


print("FIN PROGRAMA")
