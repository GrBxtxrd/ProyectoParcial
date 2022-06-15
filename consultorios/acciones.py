import consultorios.consultorio as modelo

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1][1]}!! Vamos a dar de alta a un nuevo consultorio...")

        nombre = input("Introduce el nombre del consultorio: ")

        consultorio = modelo.Consultorio(nombre)
        guardar = consultorio.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto! Has guardado el consultorio: {consultorio.nombre}")
        else:
            print(f"\nNo se guardo el consultorio, intentalo más tarde: {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\n{usuario[1][1]} Estos son tus consultorios: ")
        consultorio = modelo.Consultorio(usuario[0])
        consultorios = consultorio.listar()

        for cons in consultorios:
            print("\n********************")
            print(f"Nombre: {cons[1]}")
            print("\n********************")
    
    def eliminar(self, usuario):
        print(f"\n{usuario[1][1]}! Eliminar consultorio: ")

        nombre = input("Introduce el nombre del consultorio a eliminar: ")

        consultorio = modelo.Consultorio(nombre)
        eliminar = consultorio.eliminar()

        if eliminar[0] >= 1:
            print(f"\nSe borro el consultorio: {consultorio.nombre}!!")
        else:
            print("Ha ocurrido un error, intentalo mas tarde")