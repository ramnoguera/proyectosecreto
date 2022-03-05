# 1- Escribir un programa que pida al usuario su peso (en kg) y estatura
# (en metros); y muestre en pantalla el índice de masa corporal (IMC).


def inicio():
    kilos=float(input('ingrese peso en kilos'))
    altura=float(input('altura en  metros'))
    print('masa corporal de: ', calculo(kilos,altura))

def calculo(kg,m):
    imc=kg/(m*m)
    return(imc)

inicio()
