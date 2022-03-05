# 5- Escribir una función que reciba una muestra de números en una
# lista y devuelva otra lista con sus cuadrados.


def cuadros(numeros):
    list = []
    for i in numeros:
        list.append(i**2)
    return list

print(cuadros([1, 2, 3, 4]))
print(cuadros([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
