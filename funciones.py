import random,os,csv
 
sueldo_aleatorio = random.randint(300000,2500000)
desc_salud = sueldo_aleatorio*0.07
desc_afp = sueldo_aleatorio*0.12
sueldo_liquido = sueldo_aleatorio-(desc_afp+desc_salud)
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def menu():
    while True:
        print("MENU EMPLEADOS")
        print("1. ASIGNAR SUELDO ALEATORIO")
        print("2. CLASIFICAR SUELDOS")
        print("3. VER ESTADISTICAS")
        print("4. REPORTE DE SUELDOS")
        print("5. SALIR DEL PROGRAMA")
        opc = int(input("Escoge una opcion: "))
        if opc == 1:
            asignar_sueldo()
        elif opc == 2:
            clasificar_sueldos()
        elif opc == 3:
            estadisticas()
        elif opc == 4:
            reporte_sueldos()
        else:
            salir()
            break

def asignar_sueldo():
    print("ASIGNAR SUELDO ALEATORIO")
    for x in range(10):
        sueldo_aleatorio = random.randint(300000,2500000)
        trabajador = (trabajadores[x])
        aleatorio = (sueldo_aleatorio)
        trabajadores.append(trabajador)
        trabajadores.append(sueldo_aleatorio)
        print(trabajador,aleatorio)

            

def clasificar_sueldos():
    print("CLASIFICAR SUELDOS")
    for x in range(10):
        print("Los sueldos menores a $800.000 son:",trabajadores[x],sueldo_aleatorio<800000)
        print("Los sueldos enter $800.000 y $2.000.000 son:",trabajadores[x],sueldo_aleatorio>=800000,sueldo_aleatorio<=2000000)
        print("Los sueldos superiores a $2.000.000 son:",trabajadores[x],sueldo_aleatorio)
         
          
def estadisticas():
    print("ESTADISTICAS")



def reporte_sueldos():
    print("REPORTE DE SUELDOS")
    if not sueldo_aleatorio:
        print("NO HAY SUELDOS")
    else:
        trabajadores.append(trabajadores)
        trabajadores.append(sueldo_aleatorio)
        trabajadores.append(desc_salud)
        trabajadores.append(desc_afp)
        trabajadores.append(sueldo_liquido)
        nombre_archivo = input("Ingresa un nombre de archivo: ")+".csv"
        try:
            with open(nombre_archivo,"x",newline="") as archivo:
                escritor = csv.DictWriter(archivo(trabajadores,sueldo_aleatorio,desc_salud,desc_afp,sueldo_liquido))
                escritor.writerow(archivo)
                escritor.writerows(nombre_archivo)
        except:
            print("EL ARCHIVO YA EXISTE")
def salir():
    os.system('cls')
    print("FINALIZANDO PROGRAMA....")
    print(" Desarrollado por Diego Silva")
    print(" 22142901-K ")