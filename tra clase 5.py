nombres=[]
edades=[]
for x in range (5):
    nom=input("ingrese nombre de las personas: ")
    nombres.append(nom)
    ed=int(input("ingrese la edad  de la persona: "))
    edades.append(ed)

print("Nombre de las personas mayor de edad: ")
for x in range (5):
    if  edaded[x]>=18:
        print(nombres[x])
