#  6- Una juguetería tiene mucho éxito en dos de sus productos: Piñatas
# y muñecas. Suele hacer venta por correo y la empresa de logística les cobra
# por el peso de cada paquete, así que deben calcular cuanto pesan los
# piñatas y las muñecas que saldrán en cada paquete vendido. Cada piñata pesa
# 112 g y cada muñeca 75 g. Escribir un programa que lea el número de piñatas
# y muñecas vendidos en el último pedido y calcule el peso total del paquete
# que será enviado.



pesopiñata = 112
#  peso de  la piñata
pesomuñeca = 75
#  peso de  la muñeca

piñatas = int(input('Ponga el número de piñatas para enviar: '))
muñecas = int(input('Ponga el número de muñecas para enviar: '))
pesototal = pesopiñata * piñatas + pesomuñeca * muñecas
print('El peso total es: ' + str(pesototal))

