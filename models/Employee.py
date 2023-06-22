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
    def __init__(self, id, name, email, surname, dni, address, education_level, civil_status, phone_number, incorporation, department, salary):
        self.id = id
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
        cursor.execute("INSERT INTO employees (id, name, email, surname, dni, address, education_level, civil_status, phone_number, incorporation, department, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.id, self.name, self.email, self.surname, self.dni, self.address, self.education_level, self.civil_status, self.phone_number, self.incorporation, self.department, self.salary))
        cursor.connection.commit()

    @staticmethod
    def get_all():
        with cursor:
            cursor.execute("SELECT * FROM employees")
            return [Employee(row[0], row[1], row[2]) for row in cursor.fetchall()]
    
    def update_by_id(id, name=None, email=None, surname=None, dni=None, address=None,education_level=None,civil_status=None, phone_number=None, incorporation=None, department=None,salary=None):
        query = "UPDATE employees SET "
        values = []
        if name:
            query += "name = %s, "
            values.append(name)
        if email:
            query += "email = %s, "
            values.append(email)
        if surname:
            query += "surname = %s, "
            values.append(surname)
        if dni:
            query += "dni = %s, "
            values.append(dni)
        if address:
            query += "address = %s, "
            values.append(address)
        if education_level:
            query += "education_level = %s, "
            values.append(education_level)
        if civil_status:
            query += "civil_status = %s, "
            values.append(civil_status)
        if phone_number:
            query += "phone_number = %s, "
            values.append(phone_number)
        if incorporation:
            query += "incorporation = %s, "
            values.append(incorporation)
        if department:
            query += "department = %s, "
            values.append(department)
        if salary:
            query += "salary = %s, "
            values.append(salary)

        # Remove the trailing comma and space from the query
        query = query[:-2]

        query += " WHERE id = %s"
        values.append(id)

        cursor.execute(query, tuple(values))
        cursor.connection.commit()

    @staticmethod
    def delete_by_id(id):
        cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
        cursor.connection.commit()

    @staticmethod
    def get_by_id(id):
        cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
        result = cursor.fetchone()
        if result:
            return Employee(*result)
        return None
    
    @staticmethod
    def filter_by(id=None, department=None):
        query = "SELECT * FROM employees WHERE"
        conditions = []

        if id is not None:
            conditions.append(f"id = {id}")
        if department is not None:
            conditions.append(f"department = '{department}'")

        if conditions:
            query += " " + " AND ".join(conditions)

        with cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Employee(*row) for row in rows]

    
    def __str__(self):
        return f"Employee ID: {self.id}\nName: {self.name}\nEmail: {self.email}\nSurname: {self.surname}\nDNI: {self.dni}\nAddress: {self.address}\nEducation Level: {self.education_level}\nCivil Status: {self.civil_status}\nPhone Number: {self.phone_number}\nIncorporation: {self.incorporation}\nDepartment: {self.department}\nSalary: {self.salary}"
    
    

# employee1 = Employee(1, 'lucas', 'lucas@gmial', 'ruiz', 123123, 'pepe', 'primaria', 'solterito', 123213, 'ayer', 'sistemas', 9999)
# employee1.save()
# employee2 = Employee(2, 'lucas', 'lucas@gmial', 'ruiz', 123123, 'pepe', 'primaria', 'solterito', 123213, 'ayer', 'sistemas', 9999)
# employee2.save()
# employee3 = Employee(3, 'lucas', 'lucas@gmial', 'ruiz', 123123, 'pepe', 'primaria', 'solterito', 123213, 'ayer', 'sistemas', 9999)
# employee3.save()

#Employee.update_by_id(2, 'ramiro')
# Employee.delete_by_id(3);
#filtered = Employee.filter_by(department='sistemas')
#for employee in filtered:
#    print(employee)

