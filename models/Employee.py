import sys
import os
# Obtener la ruta del directorio raíz actual
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar la ruta raíz a sys.path
sys.path.append(root_path)

# Importar el módulo 'initialize_database' desde 'DB.index'
from DB.index import initialize_database

cursor = initialize_database()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (id_employee SERIAL PRIMARY KEY,
                name VARCHAR,
                email VARCHAR,
                surname VARCHAR,
                dni INT,
                address VARCHAR,
                education_level VARCHAR,
                civil_status VARCHAR,
                phone_number INT,
                incorporation VARCHAR,
                department VARCHAR,
                salary INT)''')
cursor.connection.commit()


class Employee:
    def __init__(self, id_employee, name, email, surname, dni, address, education_level, civil_status, phone_number, incorporation, department, salary):
        self.id = id_employee
        self.name = name
        self.surname = surname
        self.dni = dni
        self.address = address
        self.education_level = education_level
        self.civil_status = civil_status
        self.phone_number = phone_number
        self.email = email
        self.incorporation = incorporation
        self.department = department
        self.salary = salary 

    def save(self):
        cursor.execute("INSERT INTO employees (id_employee, name, email, surname, dni, address, education_level, civil_status, phone_number, incorporation, department, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.id_employee, self.name, self.email, self.surname, self.dni, self.address, self.education_level, self.civil_status, self.phone_number, self.incorporation, self.department, self.salary))
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def get_all():
        with cursor:
            cursor.execute("SELECT * FROM employees")
            return [Employee(row[0], row[1], row[2]) for row in cursor.fetchall()]
    
    def update(self):
        cursor.execute('''UPDATE employees SET name = %s, email = %s, surname = %s, dni = %s, address = %s,
                        education_level = %s, civil_status = %s, phone_number = %s, incorporation = %s,
                        department = %s, salary = %s WHERE id_employee = %s''',
                    (self.name, self.email, self.surname, self.dni, self.address, self.education_level,
                        self.civil_status, self.phone_number, self.incorporation, self.department, self.salary,
                        self.id_employee))
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def delete_by_id(employee_id):
        cursor.execute("DELETE FROM employees WHERE id_employee = %s", (employee_id,))
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def get_by_id(employee_id):
        cursor.execute("SELECT * FROM employees WHERE id_employee = %s", (employee_id,))
        result = cursor.fetchone()
        if result:
            return Employee(*result)
        return None

