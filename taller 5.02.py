# 3- Crear dos listas paralelas. En la primera ingresar los nombres de
# empleados y en la segunda los sueldos de cada empleado. Ingresar
# or teclado cuando inicia el programa la cantidad de empleados de la
# empresa. Borrar luego todos los empleados que tienen un sueldo
# mayor a 100000 (borrar el sueldo y su nombre).

# tres empleados se ingresan 
 

print("INFORME DE SUELDOS DE EMPLEADOS")
print("ingresar salarios en dolares por ejemplo (1000,500,8000)")
 
nombre1 = input("ESCRIBA UN NOMBRE Y UN APELLIDO: ")
sueldo1 = float(input(f"INGRESE EL SALARIO DE {nombre1}: "))
nombre2 = input("ESCRIBA UN NOMBRE Y UN APELLIDO (otro empleado): ")
sueldo2 = float(input(f"INGRESE EL SALARIO DE {nombre2}: "))
nombre3 = input("ESCRIBA UN NOMBRE Y UN APELLIDO (otro empleado): ")
sueldo3 = float(input(f"INGRESE EL SALARIO DE {nombre3}: "))
 
if sueldo1>1000:
    print(f"{nombre1} TIENE UN INGRESO MAYOR A $1000")
if sueldo2>1000:
    print(f"{nombre2} TIENE UN INGRESO MAYOR A $1000")
if sueldo3>1000:
    print(f"{nombre3} TIENE UN INGRESO MAYOR A $1000")


