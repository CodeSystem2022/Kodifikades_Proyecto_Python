import psycopg2

def initialize_database():
    try:
        connection = psycopg2.connect(
            host='localhost',
            port='5432',
            user='postgres',
            password='postgres',
            database='UTN-FRSR-Kodifikades',
        )
        print('Conexión exitosa!')
        cursor = connection.cursor()
        return cursor
    except Exception as ex:
        print(ex)

initialize_database()