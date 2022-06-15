import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cita:

    def __init__(self, titulo="", nota="", paciente="", sintomas="", usuario_id="", doctor_id="", fecha_cita=""):
        self.titulo = titulo
        self.nota = nota
        self.paciente = paciente
        self.sintomas = sintomas
        self.usuario_id = usuario_id
        self.doctor_id = doctor_id
        self.fecha_cita = fecha_cita

    def guardar(self):
        sql = "INSERT INTO citas VALUES(null, %s, %s, %s, %s, %s, %s, NOW(), %s)"
        cita = (self.titulo, self.nota, self.paciente, self.sintomas, self.usuario_id, self.doctor_id, self.fecha_cita)

        cursor.execute(sql, cita)
        database.commit()

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM citas WHERE usuario_id = {self.usuario_id}"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def eliminar(self):
        sql = f"DELETE FROM citas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]