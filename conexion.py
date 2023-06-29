import psycopg2

class Conexion:

    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'

    @classmethod
    def obtenerConexion(cls):
        cls._conexion = psycopg2.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
        return cls._conexion
    
    @staticmethod
    def crear_tabla_empleados():
        with Conexion.obtenerConexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                                (id_empleado SERIAL PRIMARY KEY NOT NULL,
                                nombre VARCHAR(255) NOT NULL,
                                apellido VARCHAR(255) NOT NULL,
                                dni INT NOT NULL UNIQUE,
                                email VARCHAR(255),
                                telefono BIGINT,
                                edad SMALLINT,
                                estado VARCHAR(255),
                                fecha DATE,
                                depto VARCHAR(255),
                                salario NUMERIC)''')
                conn.commit()
