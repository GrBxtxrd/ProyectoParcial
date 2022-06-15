import hashlib
from sqlite3 import connect
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    

    def registrar(self):
        passw = hashlib.sha256()
        passw.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO usuario VALUES(null, %s, %s, %s, %s, NOW())"
        usuario = (self.nombre, self.apellidos, self.email, passw.hexdigest())

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result


    def identificar(self):

        try:
            passwd = hashlib.sha256()
            passwd.update(self.password.encode('utf8'))

            cursor.execute("SELECT * FROM usuario WHERE email = %s AND password = %s", [self.email, passwd.hexdigest()])
            passw = cursor.fetchone()
            
            result = [cursor.rowcount, passw]
            
        except:
            result = [0, cursor]

        return result
   