import doctores.doctor as modelo
import consultorios.consultorio as consultorio

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1][1]}!! Vamos a registrar a un doctor")

        consul = consultorio.Consultorio(usuario[0])
        consultorios = consul.listar()

        print("\nEstos son los consultorios registrados:\n")
        for cons in consultorios:
            print(f"Id: {cons[0]} --- Nombre: {cons[1]}")
        print("\n")

        nombre = input("Introduce el nombre del doctor(a): ")
        apellido = input("Introduce el apellido del doctor(a): ")
        email = input("Introduce el email del doctor(a): ")
        direccion = input("Introduce la direccion del doctor(a): ")
        telefono = input("Introduce el telefono del doctor(a): ")

        while(True):
            consultorio_id = input("Introduce el id de un consultorio existente: ")
            cons_id = consul.buscar(consultorio_id)
            if len(cons_id)> 0:
                break
        
        doctor = modelo.Doctor(nombre, apellido, email, direccion, telefono, consultorio_id)
        guardar = doctor.guardar()
        
        if guardar[0] >= 1:
            print(f"\nPerfecto! Has dado de alta al doctor(a): {doctor.nombre}")
        else:
            print(f"\nNo se ha guardado correctamente, intentelo más tarde: {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\n{usuario[1][1]} Estos son los doctores dados de alta:\n")
        doctor =  modelo.Doctor(usuario)
        doctores = doctor.listar()

        for doct in doctores:
            print(f"Nombre: {doct[1]} {doct[2]} -> Registrado: {doct[6]}")
    
    def eliminar(self, usuario):
        print(f"\n{usuario[1][1]}! Eliminar doctor(a): ")

        nombre = input("Introduce el nombre del doctor(a) a eliminar: ")

        doctor = modelo.Doctor(nombre)
        eliminar = doctor.eliminar()

        if eliminar[0] >= 1:
            print(f"\nSe elimino al doctor(a): {doctor.nombre}!!")
        else:
            print("Ha ocurrido un error, intentalo mas tarde")