import Funciones as fn
Pedidos=[]


while True:
    print("*********************************")
    print("Bienvenido al menu de Gasxplosive")
    print("")

    print("1. Registrar pedido\n 2. Listar todos los pedidos\n 3. Imprimir hoja de ruta\n 4. Salir del programa")
    while True:
        try:
            opcion = int(input("Ingrese su seleccion de opcion :"))
            break
        except:
            print("Ingrese solo valores numericos")


    if opcion == 1:
        fn.registrar_pedido(Pedidos)
    elif opcion == 2:
        fn.listar_pedidos(Pedidos)
    elif opcion == 3:
        fn.imprimir_hoja(Pedidos)
    elif opcion == 4:
        print("Gracias por ocupar nuestro programa")
    else:
        print("Debe ingresar valores numericos solo entre 1 y 4")
    


