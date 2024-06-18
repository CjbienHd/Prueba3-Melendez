

SECTORES = ["CENTRO", "COLINA", "INDUSTRIAS"]


def registrar_pedido(arg1):
    nombre = input("Ingrese nombre y apelido del cliente del cliente :").upper()
    sector = input("Ingrese Sector(Centro/Colina/Industrias) :").upper()
    while sector not in SECTORES:
        print("El 'sector' ingresado no esta dentro de las 3 opciones antes mencionadas\n Intentelo nuevamente")
        sector = input("Ingrese Sector(Centro/Colina/Industrias) :").upper()
  

    direccion = input("Ingrese direccion :").upper()
    while True:
        try:
            cil_5 = int(input("Ingrese cantidad de Cilindros de 5 kilos a llevar :"))
            cil_15 = int(input("Ingrese cantidad de Cilindros de 15 kilos a llevar :"))
            cil_45 = int(input("Ingrese cantidad de Cilindros de 45 kilos a llevar :"))
            break
        except:
            print("Debe ingresar solo valores numericos al describir la cantidad de cilindros a desear")
    arg1.append({"nombre":nombre,
                 "Sector":sector,
                 "direccion":direccion,
                 "Cil. 5kg":cil_5,
                 "Cil. 15kg":cil_15,
                 "Cil. 45kg":cil_45})
    return

def listar_pedidos(arg1):
    for datos in arg1:
        print(datos)

def imprimir_hoja(arg1):
    unico_sector = input("Ingrese sector(Centro/Colina/Industrias) :").upper()
    pedido_sector = []
    if unico_sector in SECTORES:
        for datos in arg1:
            if datos["Sector"] == unico_sector:
                pedido_sector.append(datos)
    nombreArchivo = f"Hoja ruta {unico_sector}.txt"

    with open(nombreArchivo, "w") as archivo:
        for datos in pedido_sector:
            archivo.write(f"El nombre es :{datos["nombre"]}\n")
            archivo.write(f"El sector es :{datos["Sector"]}\n")
            archivo.write(f"La direccion es :{datos["direccion"]}\n")
            archivo. write(f"Cilindros de 5kg :{datos["Cil. 5kg"]}\n")
            archivo.write(f"Cilndros de 15kg :{datos["Cil. 15kg"]}\n")
            archivo.write(f"Cilindros de 45kg :{datos["Cil. 45kg"]}\n")
            archivo.write("\n")





  

    

    
                







    
