import psycopg2
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label
from PIL import ImageTk, Image
import tkinter as tk

# Configuración de la conexión a la base de datos
def connection():
    conn = psycopg2.connect(
        host="localhost",
        database="prueba",
        user="postgres",
        password="admin"
    )
    return conn


raiz = Tk()
raiz.title("KODIFIKADES - UTN FRSR")
raiz.geometry("1850x800")
#my_tree = ttk.Treeview(raiz)

#-------------------------TÍTULO------------------------------

label = Label(raiz, text="Panel administración de empleados ", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, padx=50)



#-------------------------CAMPOS------------------------------


#----COLUMNA 0 Y 1 (Datos principales - NOT NULL ) ----

# Nombre/s
nombreLabel = Label(raiz, text="Nombre/s", font=('Arial', 15),justify="right")
nombreLabel.grid(row=3, column=0,  padx=50, pady=5, sticky="w")
nombreEntry = Entry(raiz, bd=2, font=('Arial', 15))
nombreEntry.grid(row=3, column=1,  padx=5, pady=0)

# Apellido/s
apellidoLabel = Label(raiz, text="Apellido/s", font=('Arial', 15))
apellidoLabel.grid(row=4, column=0, padx=50, pady=5, sticky="w")
apellidoEntry = Entry(raiz, bd=2, font=('Arial', 15))
apellidoEntry.grid(row=4, column=1,  padx=5, pady=0)

# DNI
dniLabel = Label(raiz, text="DNI", font=('Arial', 15))
dniLabel.grid(row=5, column=0,  padx=50, pady=5, sticky="w")
dniEntry = Entry(raiz, bd=2, font=('Arial', 15))
dniEntry.grid(row=5, column=1,  padx=5, pady=0)

# Dirección
direccionLabel = Label(raiz, text="Dirección", font=('Arial', 15))
direccionLabel.grid(row=6, column=0,  padx=50, pady=5, sticky="w")
direccionEntry = Entry(raiz, bd=2, font=('Arial', 15))
direccionEntry.grid(row=6, column=1,  padx=5, pady=0)


#----COLUMNA 2 Y 3 (Datos secundarios)----

# Nivel Educativo
nivelEduLabel = Label(raiz, text="Nivel Educativo", font=('Arial', 15))
nivelEduLabel.grid(row=3, column=2,  padx=50, pady=5, sticky="w")
nivelEduCombobox = ttk.Combobox(values=["Primaria", "Secundaria", "Terciario", "Universitario"], width=35)
nivelEduCombobox.grid(row=3, column=3)

# Estado Civil
estCivilLabel = Label(raiz, text="Estado Civil", font=('Arial', 15))
estCivilLabel.grid(row=4, column=2, padx=50, pady=5, sticky="w")
estCivilCombobox = ttk.Combobox(values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"], width=35)
estCivilCombobox.grid(row=4, column=3)

# Email
emailLabel = Label(raiz, text="Email", font=('Arial', 15))
emailLabel.grid(row=5, column=2, padx=50, pady=5, sticky="w")
emailEntry = Entry(raiz,  bd=2, font=('Arial', 15))
emailEntry.grid(row=5, column=3, padx=5, pady=0)

# Teléfono
telefonoLabel = Label(raiz, text="Teléfono", font=('Arial', 15))
telefonoLabel.grid(row=6, column=2,  padx=50, pady=5, sticky="w")
telefonoEntry = Entry(raiz, bd=2, font=('Arial', 15))
telefonoEntry.grid(row=6, column=3,  padx=5, pady=0)


#----COLUMNA 4 Y 5 (Datos empresa - NOT NULL)----

# Id Empleado
idEmpLabel = Label(raiz, text="Id Empleado", font=('Arial', 15))
idEmpLabel.grid(row=3, column=4,  padx=50, pady=5, sticky="w")
idEmpEntry = Entry(raiz, bd=2, font=('Arial', 15))
idEmpEntry.grid(row=3, column=5,  padx=35, pady=0)

# Fecha incorporación
fechaIncLabel = Label(raiz, text="Fecha Incorporación", font=('Arial', 15))
fechaIncLabel.grid(row=4, column=4, padx=50, pady=5, sticky="w")
fechaIncEntry = Entry(raiz, bd=2, font=('Arial', 15))
fechaIncEntry.grid(row=4, column=5,  padx=5, pady=0)

# Departamento
deptoLabel = Label(raiz, text="Departamento", font=('Arial', 15))
deptoLabel.grid(row=5, column=4, padx=50, pady=5, sticky="w")
deptoCombobox = ttk.Combobox(values=["Sistemas", "Finanzas", "Marketing", "RRHH", "Ventas", "Atención al Cliente"], width=35)
deptoCombobox.grid(row=5, column=5)

# Salario
salarioLabel = Label(raiz, text="Salario", font=('Arial', 15))
salarioLabel.grid(row=6, column=4,  padx=50, pady=5, sticky="w")
salarioEntry = Entry(raiz, bd=2, font=('Arial', 15))
salarioEntry.grid(row=6, column=5,  padx=5, pady=0)


#----COLUMNA 6 (BOTONES)----
agregarBtn = Button(raiz, text="Agregar", bd=2, font=('Arial', 20), bg="#84F894", width=15)
agregarBtn.grid(row=3, column=6)

actualizarBtn = Button(raiz, text="Actualizar", bd=2, font=('Arial', 20), bg="#84E8F8", width=15)
actualizarBtn.grid(row=4, column=6)

eliminarBtn = Button( raiz, text="Eliminar", bd=2, font=('Arial', 20), bg="#FF9999", width=15)
eliminarBtn.grid(row=5, column=6)

seleccionarBtn = Button( raiz, text="Seleccionar",  bd=2, font=('Arial', 20), bg="#EEEEEE", width=15)
seleccionarBtn.grid(row=6, column=6)




label = Label(raiz, text="Colocar aquí filtro ", font=('Arial Bold', 30))
label.grid(row=7, column=0, columnspan=8, padx=50, pady=30)



#----VISUALIZADOR DE DATOS----
def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8,column=0,columnspan=7,  padx=(20, 0))


my_tree = ttk.Treeview(raiz)
style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Nombre","Apellido","DNI","Direccion","Nivel Educativo","Estado Civil","Email","Telefono","Id Empleado","Fecha Incorporacion","Departamento","Salario")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Nombre", anchor=W, width=145)
my_tree.column("Apellido", anchor=W, width=145)
my_tree.column("DNI", anchor=W, width=145)
my_tree.column("Direccion", anchor=W, width=145)
my_tree.column("Nivel Educativo", anchor=W, width=145)
my_tree.column("Estado Civil", anchor=W, width=145)
my_tree.column("Email", anchor=W, width=145)
my_tree.column("Telefono", anchor=W, width=145)
my_tree.column("Id Empleado", anchor=W, width=145)
my_tree.column("Fecha Incorporacion", anchor=W, width=145)
my_tree.column("Departamento", anchor=W, width=145)
my_tree.column("Salario", anchor=W, width=145)

my_tree.heading("#0", text="", anchor=W)
#my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Nombre", text="Nombre", anchor=W)
my_tree.heading("Apellido", text="Apellido", anchor=W)
my_tree.heading("DNI", text="DNI", anchor=W)
my_tree.heading("Direccion", text="Dirección", anchor=W)
my_tree.heading("Nivel Educativo", text="Educación", anchor=W)
my_tree.heading("Estado Civil", text="Estado Civil", anchor=W)
my_tree.heading("Email", text="Email", anchor=W)
my_tree.heading("Telefono", text="Teléfono", anchor=W)
my_tree.heading("Id Empleado", text="Id", anchor=W)
my_tree.heading("Fecha Incorporacion", text="Fecha", anchor=W)
my_tree.heading("Departamento", text="Depto", anchor=W)
my_tree.heading("Salario", text="Salario", anchor=W)



scrollbar = ttk.Scrollbar(raiz, orient="vertical", command=my_tree.yview)
scrollbar.grid(row=8, column=8, sticky="ns")

my_tree.configure(yscrollcommand=scrollbar.set)

#-------------------------LOGOS------------------------------

imagen = Image.open("utn.png")
imagen = imagen.resize((215,100), Image.ANTIALIAS)
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = Label(raiz, image=imagen_tk)
label_imagen.grid(row=9, column=0, pady=30, padx=30)

imagen3 = Image.open("kodifikades.png")
imagen3 = imagen3.resize((250,100), Image.ANTIALIAS)
imagen_tk3 = ImageTk.PhotoImage(imagen3)
label_imagen3 = Label(raiz, image=imagen_tk3)
label_imagen3.grid(row=9, column=6, pady=50, columnspan=3)


refreshTable()
raiz.mainloop()
