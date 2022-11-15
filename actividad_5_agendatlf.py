agenda = {
    "Jose": 3022944,
    "Mario": 829455,
    "Angel": 829405,
    "Luis": 930594,
}

menu = True

while menu:
    print("BIENVENIDO A LA AGENDA DIGITAL")
    print("------------------------------")
    print("Por favor escoje una acción")
    print("------------------------------")
    opcion = input("1 - Consultar un contacto "
                   "\n2 - Añadir un contacto "
                   "\n3 - Modificar un contacto "
                   "\n4 - Borrar un contacto "
                   "\n5 - Consultar Agenda "
                   "\n6 - Salir \n")

    match opcion:
        case "1":
            print("*** CONSULTAR UN CONTACTO ***")
            nomONum = input("1 - Consultar por nombre "
                            "\n2 - Consultar por número de teléfono ")
            valNok = True
            while valNok:
                if nomONum == "1":
                    nombre = input("\nIntroduce el nombre que quieres consultar ").capitalize()

                    if nombre not in agenda:
                        print("\nNo existe el contacto: " + nombre)
                    else:
                        print("\n")
                        print(agenda[nombre])
                        valNok = False

                elif nomONum == "2":

                    tlf = input("Introduce el numero que quieres consultar ")

                    if tlf not in agenda:
                        print("\nNo existe el contacto: " + tlf)
                    else:
                        print(agenda[tlf])
                        valNok = False
                else:
                    print("El valor introducido no es el correcto, vuelvelo a intentar")

        case "2":
            print("*** AÑADIR UN CONTACTO ***")
            nombre = input("Introduce el nombre ").capitalize()

            if agenda.__contains__(nombre.capitalize()):
                print("Este contacto ya existe ")
            else:
                tlf = input("Introduce el número de teléfono ")
                agenda[nombre] = tlf

        case "3":
            print("*** MODIFICAR UN CONTACTO ***")

        case "4":
            print("*** BORRAR UN CONTACTO ***")
            nombreONum = input("1 - Borrar por nombre "
                               "\n2 - Borrar por número de teléfono ")

            if nombreONum == "1":
                nomContacto = input("Introduce el nombre del contacto a eliminar ").capitalize()

                if nomContacto not in agenda:
                    print("El contacto no existe")
                else:
                    agenda.pop(nomContacto)
                    print("------- SE HA ELIMINADO EL CONTACTO CORRECTAMENTE -------")
            else:
                telContacto = input("Introduce el número de telefono del contacto a eliminar ")
                del agenda[telContacto]
                print("------- SE HA ELIMINADO EL CONTACTO CORRECTAMENTE -------")

        case "5":
            print("*** CONSULTAR AGENDA ***")
            for key, value in agenda.items():
                print(key, ' -> ', value)
        case "6":
            print("SALIENDO...")
            menu = False

        case _:
            print("El numero introducido no es válido, vuelvelo a intentar")
