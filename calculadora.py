## Hacer una calculadora
## que permita sumar, restar, multiplicar y dividir
# y que verifique que no se diva por zero

numero_a = input("Ingrese el valor de a: ")
numero_b = input("Ingrese el valor de b: ")

print(numero_a + numero_b) # esto va a tomar los strings:
print(type(numero_a))

# hago un "casteo"
int_a = int(numero_a)
int_b = int(numero_b)
print("Vuelvo a hacer la suma pero como INT")
print(int_a + int_b)

# otro ejemplo seria;
numero_z = int(input("Ingreso el numero z: "))
print(type(numero_z))