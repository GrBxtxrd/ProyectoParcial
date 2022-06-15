import citas.cita as modelo
import doctores.doctor as doctor

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1][1]}!! Vamos a agendar una cita")

        titulo = input("Introduce el titulo de la cita: ")
        nota = input("Introduce una nota de la cita: ")
        
        paciente = input("Introduce el nombre del paciente: ")

        sintomas = input("Introduce los sintomas del paciente: ")

        print(f"\n{usuario[1][1]} Estos son tus doctores:\n")
        doctr =  doctor.Doctor(usuario)
        doctores = doctr.listar()

        for doct in doctores:
            print(f"Id: {doct[0]} | Nombre: {doct[1]} {doct[2]} | Registrado el: {doct[6]}")
        
        while(True):
            doctor_id = input("Introduce un id de un doctor existente: ")
            doc_id = doctr.buscar(doctor_id)
            if len(doc_id)> 0:
                break

        fecha_cita = input("Introduce la fecha para la cita(en formato Año-mes-dia): ")
        
        cita = modelo.Cita(titulo, nota, paciente, sintomas, usuario[0], doctor_id, fecha_cita)
        guardar = cita.guardar()
        
        if guardar[0] >= 1:
            print(f"\nPerfecto! Has agendado la cita: {cita.titulo}")
        else:
            print(f"\nNo se guardo correctamente, intentalo más tarde: {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\n{usuario[1][1]} Estas son tus citas:\n")
        cita =  modelo.Cita('', '', '', '', usuario[0])
        citas = cita.listar()

        for cit in citas:
            print(f"Titulo: {cit[1]} | Reservada el: {cit[7]}")
    
    def eliminar(self, usuario):
        print(f"\n{usuario[1][1]}! Eliminar citas: ")

        titulo = input("Introduce el titulo de la cita a eliminar: ")

        cita = modelo.Cita(titulo, '', '', '', usuario[0])
        eliminar = cita.eliminar()

        if eliminar[0] >= 1:
            print(f"\nSe elimino la cita: {cita.titulo}!!")
        else:
            print("Ha ocurrido un error, intentalo mas tarde")