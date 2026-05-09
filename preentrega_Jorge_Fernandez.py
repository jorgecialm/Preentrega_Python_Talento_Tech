productos = []
while True:
    print("*" * 50)
    print("Bienvenido a la app de gestion de productos ")
    print("*" * 50)
    print("\n1.Agregar productos")
    print("2.Mostrar productos")
    print("3.Buscar productos")
    print("4.Eliminar productos")
    print("5.Salir\n")
    opcion = input("\nIngrese una opcion entre 1-5 : ")
    if opcion == "" or not opcion.isdigit():
        print("Debe ingresar una opcion valida entre 1-5 ")
    else:
        opcion = int(opcion)
        if opcion == 1:
            # opcion para agregar productos
            nombre = input("Ingrese el nombre del producto :")
            categoria = input("Ingrese la categoria del producto : ")
            precio = input("Ingrese el precio  del producto : ")
            while not nombre:
                print("Debe ingresar el nombre del producto")
                nombre = input("Ingrese el nombre del producto :")
            while not categoria:
                print("Debe ingresar el categoria del producto")
                categoria = input("Ingrese el categoria del producto :")
            while not precio or not precio.isdigit():
                print("Debe ingresar un precio valido")
                precio = input("Ingrese el precio  del producto : ")

            productos.append([nombre, categoria, int(precio)])
            print("Producto agregado con exito ")

        elif opcion == 2:
            # muestra los productos
            if not productos:
                print("No hay productos en la lista")
            else:
                for i, producto in enumerate(productos, start=1):
                    print(
                        f"{i}. Nombre : {producto[0]} - Categoria : {producto[1]} - Precio : ${producto[2]}"
                    )
        elif opcion == 3:  # opcion de buscar productos
            encontrados = []
            if len(productos) == 0:
                print("No hay productos para buscar")
            else:
                busqueda = input("Ingrese el nombre del producto que quiere buscar : ")
                while not busqueda:
                    print("Debe ingresar un nombre de producto a buscar  ")
                    busqueda = input(
                        "Ingrese el nombre del producto que quiere buscar : "
                    )
                for producto in productos:
                    if busqueda.lower() in producto[0].lower():
                        encontrados.append(producto)
                if encontrados:
                    print("Articulo encontrado ")
                    for i, p in enumerate(encontrados, start=1):
                        print(f"{i}. {p[0]} - {p[1]} - ${p[2]}")
                else:
                    print("No se encontró ningún producto con ese nombre")

        elif opcion == 4:
            # muestra la lista de productos
            if len(productos) == 0:
                print("No hay productos para eliminar")
            else:
                for i, producto in enumerate(productos, start=1):
                    print(
                        f"{i}. Nombre : {producto[0]} - Categoria : {producto[1]} - Precio : ${producto[2]}"
                    )
                # pedir al usuario que elija el indice de la lista
                indice = input("Ingrese el indice del articulo que desea eliminar : ")
                while not indice or not indice.isdigit():
                    print("Ingrese uno de los indices de la lista ")
                    indice = input(
                        "Ingrese el indice del articulo que desea eliminar : "
                    )
                # con un indice de tipo numerico validado buscar

                if int(indice) < 1 or int(indice) > len(productos):
                    print("Ese número no existe en la lista")
                else:
                    productos.pop(int(indice) - 1)
                    print("Producto eliminado con éxito")

        elif opcion == 5:
            print("\nSaliste de la aplicacion\n ")
            break
        else:
            print("Opcion no valida ingresa entre una entre 1-5")
