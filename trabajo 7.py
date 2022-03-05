#  Escribir un programa que pregunte al usuario si quiere una pizza
#  vegetariana o no vegetariana y en función de su respuesta le muestre un
#  menú con los ingredientes disponibles para que elija.
#  Solo se puede elegir un ingrediente además del queso mozzarella y el
#  tomate que están en todas la pizzas.
#  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana
#  o no y todos los ingredientes que lleva.



print('Pizzeria')
print ('Tipos de pizza 1-Vegetariana 2-No vegetariana')
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")

if tipo == "1":
    print('Ingredientes de pizzas vegetarianas')
    print('1-Aceitunas, cebolla  2-chile dulce')
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con   ", end="")
    if ingrediente == "1":
        print("Aceitunas, cebolla")
    else: 
        print("chile dulce")
else:
    print('Ingredientes de pizzas no vegetariana')
    print('1-peperoni  2-Jamon  3-Carne de res')
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con  ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamon")
    else:
        print("Carne de res")
