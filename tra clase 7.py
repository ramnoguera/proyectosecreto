lista=[["Rocio",21,1.80], ["Alberto", 52,1.75],  ["Isabel",14,1.72]]

print("Lista completa")
print("lista")
print("---------")

print("Primer componente")
print(lista[1])
print("---------")

print("Tercer componente de la lista  del primer componente")
print(lista[0][2])
print("---------")

print("Lista contenida en  la primer componente")
for x in range(len(lista[0])):
    print(lista[0][x])
print("---------")

print("Cada  elemento que contiene la lista")
for k in range (len(lista)):
    for x in range(len(lista[k])):
            print(lista[k][x])






