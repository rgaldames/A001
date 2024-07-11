import random
import csv

def Menu():
    print("================================")
    print("***** Todos Ganamos S.A.  *****")
    print("===============================")
    print("[1] <-> Agregar y/o Modificar Bono")
    print("[2] <-> Listar bonos")
    print("[3] <-> Bono más bajo ")
    print("[4] <-> Detalle")
    print("[5] <-> Salir ")
    op=input(">>>> Elija Opción: ")
    return(op)

def AgregarBono():
    """-	Al seleccionar opción 1, agregará al archivo aguinaldo.CSV 
    el Rut y valor Bono (el valor bono debe ser aleatorio en el 
    rango 30000 a 500000) de un trabajador (si el trabajador ya existe,
    modificará el valor Bono), mostrar mensaje adecuado. 
    (la solicitud y muestra de datos se debe realizar en el 
    programa principal y el proceso se debe realizar en una función)"""
    rut=input("ingrese Rut Trabajador: ")
    monto=random.randint(30000,500000)
    with open("aguinaldo.CSV","a",newline="") as AguinaldoCSV:
        manejador = csv.writer(AguinaldoCSV)
        manejador.writerow([rut,monto])
    print(f"Bono ${monto} Actualizado para {rut}")

def ListasBonos():
    rango1=[]   #Rango menores a 100000      
    rango2=[]   #Entre 100000 y 200000    
    rango3=[]   #Superior a 200000    

    with open("aguinaldo.CSV","r",newline="") as aguinaldos:
        lecto = csv.reader(aguinaldos)
        for row in lecto:
            rut, monto = row
            monto=int(monto)
            if monto<100000:
                rango1.append((rut,monto))
            elif monto>100000 and monto<200000:
                rango2.append((rut,monto))
            elif monto>200000:
                rango3.append((rut,monto))
    aguinaldos.close
    
    print("Listado de Bonos")
    print(f"Bonos menores a $100000    Total: {len(rango1)}")
    print("Rut Trabajador    Valor  Bono")
    for rut, monto in rango1:
        print(f"{rut}     {monto}")

    print(f"Bonos entre 100000 and 200000    Total: {len(rango2)}")
    for rut, monto in rango2:
        print(f"{rut}     {monto}")

    print(f"Bonos menores a $100000    Total: {len(rango3)}")
    for rut, monto in rango3:
        print(f"{rut}     {monto}")


