# Ejercicio 1.
# Dados 2 números enteros, imprimir por pantalla el producto.
# Si el producto de ambos números es mayor a 100, mostrar además la suma de los números.
# Se puede utilizar el siguiente código para mostrar por pantalla

# x = int(input("Ingrese el primer número: "))
# y = int(input("Ingrese el segundo número: "))
#
# producto = x * y
#
# print("El producto entre {} y {} es: {}".format(x, y, producto))
#
# if (producto > 100):
#     suma = x + y
#     print("La suma entre {} y {} es: {}".format(x, y, suma))

# Ejercicio 2.
# Dada una lista de números, se pide iterar los elementos de la lista y almacenar en
# otra lista el resultado de sumar ese elemento con el anterior.
# Por ejemplo, dada la lista: [1, 2, 3, 4], se espera que la salida sea una lista con los
# elementos [3, 5, 7]
# Resolver el problema de dos maneras diferentes: con un FOR y con una lista por
# comprensión.

lista = [1, 2, 3, 4]

list = []

for l in lista:
    print(lista[l])
    print(lista[l - 1])
    list = lista[l] + lista[l - 1]
    print(list)
    print("\n")

