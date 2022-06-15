import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctor:

    def __init__(self, nombre="", apellidos="", email="", direccion="", telefono="", consultorio_id=""):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.consultorio_id = consultorio_id

    def guardar(self):
        sql = "INSERT INTO doctor VALUES(null, %s, %s, %s, %s, %s, NOW(), %s)"
        doctor = (self.nombre, self.apellidos, self.email, self.direccion, self.telefono, self.consultorio_id)

        cursor.execute(sql, doctor)
        database.commit()

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM doctor"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def buscar(self, id):
        sql = f"SELECT * FROM doctor WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def eliminar(self):
        sql = f"DELETE FROM doctor WHERE nombre LIKE '%{self.nombre}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]