"""
Ejercicio Integrador
 
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su ID, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
 

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el ID del cliente y eliminar sus datos de la base de datos.
Preguntar por el ID del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su ID y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su ID y nombre.
Terminar el programa.
"""
"""
print("Bienvenido al programa. Qué desea hacer? Por favor ingrese el número de la opción deseada")
print("")
print("1- Añadir cliente")
print("2- Elminar cliente")
print("3- Mostrar cliente")
print("4- Listar todos los clientes")
print("5- Listar clientes preferentes")
print("6- Salir del programa")
print("")

answer = int(input("Opción elegida: "))
"""
clients = {}
answer = ""

while answer != 6:
    if answer == 1:
        id = input("Por favor ingresá el ID del cliente: ")
        name = input("Ingresá el nombre completo del cliente: ")
        address = input("Ingresá la dirección del cliente: ")
        phone = input("Ingresá el teléfono del cliente: ")
        mail = input("Ingresá el mail del cliente: ")
        pref = input("¿Es un cliente preferente? ").lower()
        client = {"Nombre Completo": name.capitalize(), "Dirección": address.capitalize(), "Teléfono": phone, "Mail": mail, "Preferente": pref == "si"}
        clients[id] = client
    if answer == 2:
        id = input("Introduce id del cliente: ")
        if id in clients:
            del clients[id]
            print("El cliente ha sido eliminado con éxito")
        else:
            print("El cliente con el ID solicitado no existe")
    if answer == 3:
        id = input("Por favor ingresá el ID del cliente: ")
        if id in clients:
            print("")
            print("Datos del cliente de ID", id)
            for k, v in clients[id].items():
                print(k + ":", v)
        else:
            print("El cliente con el ID solicitado no existe")
    if answer == 4:
        print("Clientes: ")
        for k, v in clients.items():
            print(k, v["Nombre Completo"])
    if answer == 5:
        print("Clientes preferentes: ")
        for k, v in clients.items():
            if v["Preferente"]:
                print(k, v["Nombre Completo"])
    print("Bienvenido al programa. Qué desea hacer? Por favor ingrese el número de la opción deseada")
    print("")
    print("1- Añadir cliente")
    print("2- Elminar cliente")
    print("3- Mostrar cliente")
    print("4- Listar todos los clientes")
    print("5- Listar clientes preferentes")
    print("6- Salir del programa")
    print("")
    answer = int(input("Opción elegida: "))

print("El programa ha finalizado")