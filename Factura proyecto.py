# Factura 
# Incluye: Nombre del cliente, telefono del cliente, cantidad y  precio
# Descuentos en las ordenes



print("Gracias por escoger EcoCar")
print("Ingrese el nombre del cliente:")
e = input ()
print("El cliente es: ", e)
print("Ingrese el telefono del cliente:")
t= input ()
print("Telefono: ", t)
print("Ingrese la descripcion del articulo:")
des= input ()
print("Ingrese la cantidad:")
can= input ()
can = int (can)
print("Ingrese el precio:")
pr= input ()
pr = int (pr)

total = can*pr
print("Subtotal: ", total)
y= total*0.18
y= int (y)
print("ITBIS", y)

x= total+y
print("Total: ", x)

if x<=10000:
    a= x*0.05
    a= int (a)
    print ("Tiene un descuento de: ", a)
    mp=x-a
    mp= int (mp)
    print("Monto a pagar: ", mp)

else: 
    s=x*0.10
    s= int (s)
    print ("Tiene un descuento de: ", s)
    mp=x-S
    mp= int(mp)
    print ("Monto a pagar: ", mp)


