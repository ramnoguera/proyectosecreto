import sys
from datetime import date

#----------------GRUPO 7-------------------------
#Desarrolladores:
#Ramiro Noguera Brenes
#Orlando Orfila Alfaro
#Marianella Ruiz Orozco
#Daniel Sun Mora
#-----------------------------------------

#LISTA CLIENTES
clientes = ["Cecilia Rodrigues", "Carlo Magno Guzman", "Hector Sanchez", "Hanzel Henriquez", "Roberto Castro"]
clientes_id = ["1509789", "40907654", "81112345", "239000977", "56789123"]
contacto = ["687334", "22376590", "67991123", "34778890", "6093455"]
email = ["cecirodrigues@gmail.com", "magno2021@gmail.com", "facturas@outlook.com", "hanzel123@gmail.com", "castro_roberto@yahoo.com"]

#LISTA REPUESTOS
nom_repuestos = ["Discos de freno", "Correa de accesorios", "Filtro de aceite", "Capot", "Portón trasero", "Pastillas de freno"]
repuestos_id = ["D01","C00", "FR2", "Ct15", "Pt150", "Past25"]
marca = ["W Amarok", "Ford", "Toyota", "Nissan", "Mazda", "Audi"]
precio = ["18000", "5550", "54890", "22350", "35670", "43430"]
tipo = ["usado", "usado", "nuevo", "nuevo", "usado", "nuevo"]
stock = ["no", "si", "si", "si", "no", "no"]

#LISTA FACTURACION PARA CIERRE DE CAJA
datosProductos =[]
datosMarca =[]
datosPrecio =[]
datosCantidad =[]
datosCalculo =[]
datosTotal =[]
datosNombre =[]
datosCedula = []
datosEmail=[]
datosContacto =[]

#LISTA TEMPORAL FACTURACION
temporal_datosProductos =[]
temporal_datosMarca =[]
temporal_datosPrecio =[]
temporal_datosCantidad =[]
temporal_datosCalculo =[]
temporal_total=[]
temporal_datosNombre =[]
temporal_datosCedula = []
temporal_datosEmail=[]
temporal_datosContacto =[]

#CONTADOR
contador=[]


#MENU PRINCIPAL

def menu_principal():
    print("")
    print("*************************************************")
    print("Sistema de Mantenimiento y Repuestos EcoCar")
    print("*************************************************")
    print("----------------------------------")
    print(">>>MENÚ PRINCIPAL<<<")
    print("1: Matenimiento de Clientes")
    print("2: Matenimiento de Repuestos")
    print("3: Facturación")
    print("4: Cierre de Caja")
    print("5: Salir")
    print("----------------------------------")
    opcion = int(input("Digita una de las opciones del menú:"))
    print("")
 
    if (opcion == 1): 
        menu_clientes()
    elif (opcion == 2):
         menu_repuestos()
    elif (opcion == 3):
        facturas()
    elif (opcion == 4):
        cierre_caja()
    elif (opcion == 5):
        salir()
    else:
        print("Digite una  opciona valida")
            

#OPCION MANTENIMIENTO DE CLIENTES
def menu_clientes():
    opcion_cliente = 0
    print("----------------------------------")
    print(">>>Menú Mantenimiento de Clientes<<<")
    print("1: Ingresar un nuevo cliente")
    print("2: Buscar clientes")
    print("3: Eliminar datos del cliente")
    print("4: Regresar al Menú Principal")
    print("----------------------------------")
    opcion_cliente = int(input("Digita la opción que deseas realizar:"))
    if (opcion_cliente == 1):
        nuevo_cliente()
    elif (opcion_cliente == 2):
        modificar_cliente()
    elif (opcion_cliente == 3):
        eliminar_cliente()
    elif (opcion_cliente == 4):
        menu_principal()
    else:
        print("Digita una de las opciones del menú")
    
def nuevo_cliente():
    print("")
    identificacion = input("Ingresa la identificación del cliente:")
    if identificacion in clientes_id:
        print("")
        print("Cliente ya se encuentra registrado")
        print("Debes ingresar un ID diferente")
        nuevo_cliente()
    else:
        clientes_id.append(identificacion)
        nombre = input("Ingresa el nombre y apellido del cliente:")
        clientes.append(nombre)
        telefono = input("Ingresa el contacto del cliente:")
        contacto.append(telefono)
        correo = input("Ingresa el e-mail del cliente:")
        email.append(correo)
    print("")
    print("Cliente ingresado correctamente.")
    print("")
    print("Nombre:",nombre)
    print("Identificación:",identificacion)
    print("Contacto:",telefono)
    print("E-mail:",correo)
    print("")
    menu_clientes()
    
def modificar_cliente():
    opcion_modificar=0
    print("")
    buscar_cliente = input("Digita la identificación del cliente:")
    if buscar_cliente in clientes_id:
        indice = clientes_id.index(buscar_cliente)
        cedula = clientes_id[indice]
        nombre = clientes[indice]
        numero = contacto[indice]
        correo = email[indice]        
        print("*************************")
        print("Resultado:")
        print("Cliente:",nombre)
        print("Cédula:",cedula)
        print("Teléfono:",numero)
        print("E-mail:",correo)        
        print("*************************")       
        opcion_modificar = int(input("Para actualizar los datos digita 1, para volver al menú digita 2: "))
        if (opcion_modificar ==1):
            print("")
            print("*****Nota*****")
            print("Los únicos datos permitidos para cambiar son: teléfono y correo electrónico.")
            print("Si el cliente desea cambiar su ID, deberás crear un usuario nuevo.")
            print("**************")
            print("")
            nuevo_telefono = input("Digita el nuevo teléfono:")
            contacto[indice]=nuevo_telefono
            nuevo_correo = input("Digita el nuevo e-mail:")
            email[indice]=nuevo_correo
            print("")
            print("Datos del cliente actualizados correctamente")
            print("*************************")
            print("Cliente:",nombre)
            print("Cédula:",cedula)
            print("Teléfono:",nuevo_telefono)
            print("E-mail:",nuevo_correo)        
            print("*************************")
            menu_clientes()
        if (opcion_modificar ==2):
            menu_clientes()
    else:
        print("")
        print("**************")
        print("Cliente no encontrado.")
        print("**************")
        menu_clientes()

def eliminar_cliente():
    print("")
    buscar_cliente = input("Digita la identificación del cliente:")
    if buscar_cliente in clientes_id:
        indice = clientes_id.index(buscar_cliente)
        cedula = clientes_id[indice]
        nombre = clientes[indice]
        numero = contacto[indice]
        correo = email[indice]        
        print("*************************")
        print("Resultado:")
        print("Cliente:",nombre)
        print("Cédula:",cedula)
        print("Teléfono:",numero)
        print("E-mail:",correo)        
        print("*************************")
        eliminar = str(input("¿Deseas eliminar este cliente del sistema?(S/N):"))
        if eliminar =="S" or eliminar =="s":
            print("")
            print("El cliente ha sido eliminado correctamente.")
            print("")
            clientes_id.pop(indice)
            clientes.pop(indice)
            contacto.pop(indice)
            email.pop(indice)
            print("*********************")
            print("Volviendo al Menú Clientes")
            menu_clientes()
        elif eliminar =="N" or eliminar == "n":
            print("")
            print("*********************")
            print("Volviendo al Menú Clientes")
            menu_clientes()
   
    

#OPCION MANTENIMIENTO DE REPUESTOS
def menu_repuestos():
    print("----------------------------------")
    print(">>>Menú Mantenimiento de repuestos<<<")
    print("1: Buscar repuesto")
    print("2: Agregar repuesto")
    print("3: Modificar repuesto")
    print("4: Eliminar repuesto")
    print("5: Volver al menu principal")
    print("----------------------------------")
    opcion = int(input("Digita cuál función deseas realizar:"))
    if opcion ==1:
            buscar_repuestosid()
    if opcion == 2:
            agregar_repuestosid()
    if opcion ==3:
            modificar_repuestosid()
    if opcion ==4:
            eliminar_repuestosid()
    if opcion ==5:
            menu_principal()


def buscar_repuestosid():
    print("*********************")
    print(">>>Buscar repuestos<<<")
    print("*********************")
    buscar_id=str(input("Ingrese el Id del repuesto:"))
    if buscar_id in repuestos_id:
        i= repuestos_id.index(buscar_id)
        print("Se ha encontrado el repuesto:")
        print("*********************")
        print("Repuesto Id:",repuestos_id[i])
        print("Nombre:",nom_repuestos[i])
        print("Marca:",marca[i])
        print("Precio:",precio[i])
        print("Tipo:",tipo[i])
        print("En Stock:",stock[i])
        print("*********************")
        print("Volviendo a mantenimiento de repuestos")
        menu_repuestos()
    elif buscar_id not in repuestos_id:
        print("*********************")
        print("Id no encontrado")
        print("*********************")
        respuesta_reg= str(input("Desea registrar el repuesto?(S/N):"))
        if respuesta_reg == "S" or respuesta_reg=="s":
            agregar_repuestosid()
        elif respuesta_reg =="N" or respuesta_reg =="n":
            print("*********************")
            print("Volviendo a mantenimiento de repuestos")
            menu_repuestos()

def agregar_repuestosid():
    print("*********************")
    print(">>>Agregar repuestos<<<")
    print("*********************")
    repuestos_id.append(input("Digite el ID del repuesto:"))
    nom_repuestos.append(input("Ingrese el nombre del repuesto:"))
    marca.append(input("Ingrese la marca del repuesto:"))
    precio.append(input("Ingrese el precio del repuesto:"))
    tipo.append(input("Ingrese el tipo de repuesto (nuevo/usado):"))
    stock.append(input("Se encuentra en stock (si/no):"))
    respuesta_agr1 = str(input("Desea agregar otro repuesto?(S/N):"))
    if respuesta_agr1 =="S" or respuesta_agr1 =="s":
        agregar_repuestosid()
    elif respuesta_agr1 =="N" or respuesta_agr1 =="n":
        print("*********************")
        print("Volviendo a mantenimiento de repuestos")
        menu_repuestos()

def modificar_repuestosid():
    print("*********************")
    print(">>>Modificar repuestos<<<")
    print("*********************")
    modificar_id1 = str(input("Ingrese el Id del repuesto por modificar:"))
    if modificar_id1 in repuestos_id:
        i = repuestos_id.index(modificar_id1)
        print("Se ha encontrado el repuesto:")
        print("*********************")
        print("Repuesto Id:", repuestos_id[i])
        print("Nombre:", nom_repuestos[i])
        print("Marca:", marca[i])
        print("Precio:", precio[i])
        print("Cantidad:", tipo[i])
        print("Stock:", stock[i])
        print("*********************")
        modificar_id2 = str(input("Modificar el repuesto?(S/N):"))
        if modificar_id2 =="S" or modificar_id2 =="s":
            print("Ingresa los nuevos valores según se solicita")
            repuestos_id[i] = input("Repuesto Id:")
            nom_repuestos[i] = input("Nombre:")
            marca[i] = input("Marca:")
            precio[i]= input("Precio:")
            tipo[i]= input("Cantidad:")
            stock[i]= input("Stock:")
            print("")
            print("Datos actualizados exitosamente")
            print("*********************")
            print("Repuesto Id:", repuestos_id[i])
            print("Nombre:", nom_repuestos[i])
            print("Marca:", marca[i])
            print("Precio:", precio[i])
            print("Cantidad:", tipo[i])
            print("Stock:", stock[i])
            print("*********************")
            modificar_id3 = str(input("Modificar otro repuesto?(S/N):"))
            if modificar_id3 =="S" or modificar_id3 =="s":
                modificar_repuestosid()
            elif modificar_id3 =="N" or modificar_id3 == "n":
                print("*********************")
                print("Volviendo a mantenimiento de repuestos")
                menu_repuestos()
        elif modificar_id2 =="N" or modificar_id2 == "n":
            print("*********************")
            print("Volviendo a mantenimiento de repuestos")
            menu_repuestos()
    else:
        print("*********************")
        print("Id no encontrado")
        print("*********************")
        print("Volviendo a mantenimiento de repuestos")
        menu_repuestos()


def eliminar_repuestosid():
    print("*********************")
    print(">>>Eliminar repuestos<<<")
    print("*********************")
    eliminar_id1 = str(input("Ingrese el Id del repuesto por eliminar:"))
    if eliminar_id1 in repuestos_id:
        i = repuestos_id.index(eliminar_id1)
        print("Se ha encontrado el repuesto:")
        print("*********************")
        print("Repuesto Id:", repuestos_id[i])
        print("Nombre:", nom_repuestos[i])
        print("Marca:", marca[i])
        print("Precio:", precio[i])
        print("Cantidad:", tipo[i])
        print("Stock:", stock[i])
        print("*********************")
        eliminar_id2 = str(input("Eliminar el repuesto?(S/N):"))
        if eliminar_id2 =="S" or eliminar_id2 =="s":
            print("El repuesto Id", repuestos_id[i], "ha sido eliminado.")
            repuestos_id.pop(i)
            nom_repuestos.pop(i)
            marca.pop(i)
            precio.pop(i)
            tipo.pop(i)
            stock.pop(i)
            print("*********************")
            print("Volviendo a mantenimiento de repuestos")
            menu_repuestos()
        elif eliminar_id2 =="N" or eliminar_id2 == "n":
            print("*********************")
            print("Volviendo a mantenimiento de repuestos")
            menu_repuestos()
    else:
        print("*********************")
        print("Id no encontrado")
        print("*********************")
        print("Volviendo a mantenimiento de repuestos")
        menu_repuestos()
        
                  
#OPCION FACTURAS
def facturas():
    print("")
    print("Iniciando el proceso de Facturación...")
    print("")
    buscar_cliente = input("Digita la identificación del cliente:")
    if buscar_cliente in clientes_id:
        indice = clientes_id.index(buscar_cliente)
        cedula = clientes_id[indice]
        datosCedula.append(cedula)
        temporal_datosCedula.append(cedula)
        nombre = clientes[indice]
        datosNombre.append(nombre)
        temporal_datosNombre.append(nombre)
        numero = contacto[indice]
        datosContacto.append(numero)
        temporal_datosContacto.append(numero)
        correo = email[indice]
        datosEmail.append(correo)
        temporal_datosEmail.append(correo)
        detalle_facturas()            
    else:
        print("Cliente no encontrado, verifica el ID del cliente")
        facturas()

def detalle_facturas():
    opcion = False
    while (opcion==False):
        
        datos_compra= input("Digita el ID del producto:")
        if datos_compra in repuestos_id:
            indice_producto = repuestos_id.index(datos_compra)
            
            nombre_producto = nom_repuestos[indice_producto]
            datosProductos.append(nombre_producto)
            
            temporal_datosProductos.append(nombre_producto)
            
            nom_marca = marca[indice_producto]
            datosMarca.append(nom_marca)

            temporal_datosMarca.append(nom_marca)
                     
            unidad_precio = int(precio[indice_producto])
            datosPrecio.append(unidad_precio)

            temporal_datosPrecio.append(unidad_precio)
            
            cantidad= int(input("Unidades compradas:"))
            datosCantidad.append(cantidad)

            temporal_datosCantidad.append(cantidad)
            
            calculo = (cantidad*unidad_precio)
            datosCalculo.append(calculo)

            temporal_datosCalculo.append(calculo)
                  
        else:
            print("Producto no encontrado, verifica el ID del item")
            facturas()
        
        seguir_comprando= input("Deseas incluir otro producto en la factura?:(S/N)")
        if seguir_comprando == "S" or seguir_comprando =="s":
            detalle_facturas()
  
        else:
            seguir_comprando =="N" or seguir_comprando =="n"
            opcion = True
            imprimir_facturas()
        
def imprimir_facturas():
        print("")
        print("**********************************")
        print("FACTURA DE COMPRA")
        print("----------------------------------")
        print("DATOS DEL CLIENTE")
        print("Nombre:",temporal_datosNombre[-1])
        print("Identificación:",temporal_datosCedula[-1])
        print("Contacto:", temporal_datosContacto[-1])
        print("E-mail:",temporal_datosEmail[-1])
        print("----------------------------------")
        print("DETALLE:")
        for x in range(len(temporal_datosProductos )):
            print("Productos:",temporal_datosProductos[x])
            print("Marca:",temporal_datosMarca[x])
            print("Cantidad:",temporal_datosCantidad[x])
            print("Precio unitario:",temporal_datosPrecio[x],"colones")
            print("")
            calculo= temporal_datosCantidad[x]*temporal_datosPrecio[x]
            temporal_total.append(calculo)
            sumafactura= sum(temporal_total)
            datosTotal.append(sumafactura)
            print("Total:",calculo)
        print("----------------------------------")
        print("Total a pagar:" ,sumafactura,"colones,IVA incluido")
        print("----------------------------------")
        input("Presione ENTER para imprimir")
        print("Factura generada con éxito")
        contadorVentas=0
        contadorVentas=contadorVentas+1
        contador.append(contadorVentas)
        limpiar_temporales()
        menu_principal()        

#---------------------------------------------    
def limpiar_temporales():
    temporal_datosProductos.clear()
    temporal_datosMarca.clear()
    temporal_datosPrecio.clear()
    temporal_datosCantidad.clear()
    temporal_datosCalculo.clear()
    temporal_datosNombre.clear()
    temporal_datosCedula.clear()
    temporal_datosEmail.clear()
    temporal_datosContacto.clear()
    menu_principal()
#---------------------------------------------   
            

#CIERRE DE CAJA

def cierre_caja():
    print("**********************************")
    print(">>CIERRE DE CAJA<<")
    print("**********************************")
    fecha = date.today()
    print("Fecha:", fecha)
    print("Cantidad de ventas realizadas:",len(contador))#aqui va contador
    print("Monto total de ventas:",sum(datosTotal))#aqui va el acumulador
    print("")
    print("Imprimiendo copia de facturas del día...")
    print("----------------------------------")
    print("DATOS DEL CLIENTE")
    for a,b,c,d in zip(datosNombre,datosCedula,datosContacto,datosEmail):
        print("Nombre:",a,"Cédula:",b,"Contacto:",c,"E-mail:",d)
    print("----------------------------------")
    print("FACTURA:")
    for e,f,g,h,i in zip(datosProductos,datosMarca,datosPrecio,datosCantidad,datosCalculo):
        print("Producto:",e,"Marco:",f,"Precio:",g,"Cantidad:",h,"Total a pagar:",i,"colones,IVA incluido")
        print("----------------------------------")
    input("Presione ENTER para regresar al menú principal")
    menu_principal()


#OPCION SALIR

def salir():
    print("")
    print("¡Hasta la próxima visita!")
    print("")
    sys.exit() 
          

#PROGRAMA PRINCIPAL
menu_principal()
