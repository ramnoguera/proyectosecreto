# 3- Escribir un programa que pida al usuario un número entero y
# muestre por pantalla un triángulo rectángulo como este de altura del
# número introducido:

numero=int(input('inserte numero: '))
for i in range(numero):
    print('*'*(i+1))
