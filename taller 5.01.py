# 2- Crear y cargar dos listas con los nombres de 5 productos en una y
# sus respectivos precios en otra. Definir dos listas paralelas. Mostrar
# cuantos productos tienen un precio mayor al primer producto
# ingresado.


# se ingresa la cantidad articulos y precios.
numero = int(input("Ingrese cuantos articulos quiere en su lista y precios: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista de articulos es:", lista)

    buscar = input("Dígame el articulo a buscar: ")
    contador = 0
    for i in lista:
        if i == buscar:
            contador += 1;
    if contador == 0:
        print("El articulo '" + buscar + "' no aparece en la lista.")
    elif contador == 1:
        print("El articulo '" + buscar + "' aparece una vez en la lista.")
    else:
        print("El articulo '" + buscar + "' aparece", contador, "veces en la lista.")
