datos = {
    "usuarios":
    [


    ]
}

def ingresar_usuario():
    while True:
        nombre = input("Ingresa el nombre del usuario: ")
        if len(nombre) == 0:
            print("El texto no puede estar vacio")
            continue
        for i in datos["usuarios"]:
            if i["nombre"] == nombre:
                print("El nombre está en uso.")
            break

        genero = input("Ingresa tu sexo (F o M): ").lower()
        if genero == "m":
            print("El género ingresado es masculino.")
        elif genero == "f":
            print("El género ingresado es femenino.")
        else:
            ("Error, carácter incorrecto. (Formato: F o M)")

        contraseña = input("Ingresa tu contraseña: ")

        if len(contraseña) < 8:
            print("La contraseña debe tener mínimo 8 carácteres")
            continue
        elif len(contraseña) == 0:
            print("La contraseña no puede estar vacía.")
            continue

        usuario_agregar = {

            "nombre": nombre,
            "genero": genero,
            "contraseña": contraseña
        }
        datos["usuarios"].append(usuario_agregar)
        print("Usuario ingresado satisfactoriamente.")
        break

while True:
    print("1 - Ingresar un usuario.")
    print("2 - Buscar un usuario.")
    print("3 - Eliminar usuario.")
    print("4 - Salir.")
    opc = int(input("Por favor, ingresa una opción: "))
    if opc <= 0 or (opc > 4):
        print("Opción inválida.")
        continue

    if opc == 1:
        ingresar_usuario()
    
    elif opc == 2:
        nombre_buscar = input("Ingresa el nombre del usuario para mostrar sus datos: ")
        for i in datos["usuarios"]:
            if nombre_buscar == i["nombre"]:
                print(f"Nombre: {i["nombre"]}")
                print(f"Género: {i["genero"]}")
                print(f"Contraseña: {i["contraseña"]}")
            else:
                print("El usuario ingresado no existe.")

    elif opc == 3:
        usuario_eliminar = input("Ingresa el nombre del usuario que quiere eliminar: ")
        for i in datos["usuarios"]:
            if i["nombre"] == usuario_eliminar:
                datos["usuarios"].remove(i)
                print("Usuario eliminado.")
            else:
                ("El usuario no existe.")

    elif opc == 4:
        print("Cerrando programa...")
        break
    