import usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Consultorio:

    def __init__(self, nombre=""):
        self.nombre = nombre

    def guardar(self):
        sql = "INSERT INTO consultorio VALUES(null, %s, NOW())"
        consultorio = [self.nombre]
        cursor.execute(sql, consultorio)
        database.commit()
        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM consultorio"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def buscar(self, id):
        sql = f"SELECT * FROM consultorio WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def eliminar(self):
        sql = f"DELETE FROM consultorio WHERE nombre LIKE '%{self.nombre}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]