from tkinter import Tk, Label, messagebox, ttk, Entry, Button, NO, W
from PIL import ImageTk, Image
import tkinter
from conexion import Conexion

class Interface:

    def __init__(self):
        # Creación de la ventana y propiedades de la misma
        self.raiz = Tk()
        self.raiz.title("KODIFIKADES - UTN FRSR")
        self.raiz.geometry("1800x820")

        
        # Placeholders de los Entry
        self._ph1 = tkinter.StringVar()
        self._ph2 = tkinter.StringVar()
        self._ph3 = tkinter.StringVar()
        self._ph4 = tkinter.StringVar()
        self._ph5 = tkinter.StringVar()
        self._ph6 = tkinter.StringVar()
        self._ph7 = tkinter.StringVar()
        self._ph8 = tkinter.StringVar()
        self._ph9 = tkinter.StringVar()
        self._ph10 = tkinter.StringVar()
        self._ph11 = tkinter.StringVar()

        # ----------Título----------
        self.label = Label(self.raiz, text="PANEL ADMINISTRACIÓN EMPLEADOS", font=('Arial', 30))
        self.label.grid(row=0, column=0, columnspan=7, padx=50, pady=(20, 40))

        # --------------------------
        # ----------CAMPOS----------
        # -------------------------
        
        #----------COLUMNA 0 Y 1 (Datos principales - NOT NULL ) ----------
        # Nombre/s
        self.nombreLabel = Label(self.raiz, text="*Nombre:", font=('Arial', 15))
        self.nombreLabel.grid(row=3, column=0,  padx=50, pady=5, sticky="w")
        self.nombreEntry = Entry(self.raiz, bd=2, font=('Arial', 15),textvariable = self._ph1)
        self.nombreEntry.grid(row=3, column=1,  padx=5, pady=0)

        # Apellido/s
        self.apellidoLabel = Label(self.raiz, text="*Apellido:", font=('Arial', 15))
        self.apellidoLabel.grid(row=4, column=0, padx=50, pady=5, sticky="w")
        self.apellidoEntry = Entry(self.raiz, bd=2, font=('Arial', 15),textvariable = self._ph2)
        self.apellidoEntry.grid(row=4, column=1,  padx=5, pady=0)

        # DNI
        self.dniLabel = Label(self.raiz, text="*DNI:", font=('Arial', 15))
        self.dniLabel.grid(row=5, column=0,  padx=50, pady=5, sticky="w")
        self.dniEntry = Entry(self.raiz, bd=2, font=('Arial', 15),textvariable = self._ph3)
        self.dniEntry.grid(row=5, column=1,  padx=5, pady=0)

        # Buscar ID
        self.EmpleadosLabel = Label(self.raiz, text="Buscar ID:", font=('Arial', 15))
        self.EmpleadosLabel.grid(row=7, column=0,  padx=50, pady=(0, 40), sticky="w")
        self.EmpleadosEntry = Entry(self.raiz, bd=2, font=('Arial', 15),textvariable = self._ph11)
        self.EmpleadosEntry.grid(row=7, column=1,  padx=5, pady=(0, 40))

        
        #----------COLUMNA 2 Y 3 (Datos secundarios)----------
        # Email
        self.emailLabel = Label(self.raiz, text="Email:", font=('Arial', 15))
        self.emailLabel.grid(row=3, column=2, padx=50, pady=5, sticky="w")
        self.emailEntry = Entry(self.raiz,  bd=2, font=('Arial', 15),textvariable = self._ph4)
        self.emailEntry.grid(row=3, column=3, padx=5, pady=0)

        # Teléfono
        self.telefonoLabel = Label(self.raiz, text="Teléfono:", font=('Arial', 15))
        self.telefonoLabel.grid(row=4, column=2,  padx=50, pady=5, sticky="w")
        self.telefonoEntry = Entry(self.raiz, bd=2, font=('Arial', 15),textvariable = self._ph5)
        self.telefonoEntry.grid(row=4, column=3,  padx=5, pady=0)

        # Edad
        self.edadLabel = Label(self.raiz, text="Edad:", font=('Arial', 15))
        self.edadLabel.grid(row=5, column=2, padx=50, pady=5, sticky="w")
        self.edadEntry = Entry(self.raiz,  bd=2, font=('Arial', 15),textvariable = self._ph6)
        self.edadEntry.grid(row=5, column=3, padx=5, pady=0)


        #----------COLUMNA 4 Y 5 (Datos empresa)----------
        # Estado
        self.estadoLabel = Label(self.raiz, text="Estado:", font=('Arial', 15))
        self.estadoLabel.grid(row=3, column=4,  padx=50, pady=5, sticky="w")
        self.estadoEntry = ttk.Combobox(values=["","Activo","Licencia","Vacaciones","Despido","Renuncia"], width=35, textvariable = self._ph7)
        self.estadoEntry.grid(row=3, column=5)

        # Fecha incorporación
        self.fechaLabel = Label(self.raiz, text="Fecha Incorporación:", font=('Arial', 15))
        self.fechaLabel.grid(row=4, column=4, padx=50, pady=5, sticky="w")
        self.fechaEntry = Entry(self.raiz, bd=2, font=('Arial', 15),textvariable = self._ph8)
        self.fechaEntry.grid(row=4, column=5,  padx=5, pady=0)

        # Departamento
        self.deptoLabel = Label(self.raiz, text="Departamento:", font=('Arial', 15))
        self.deptoLabel.grid(row=5, column=4, padx=50, pady=5, sticky="w")
        self.deptoEntry = ttk.Combobox(values=["","Sistemas", "Finanzas", "Marketing", "RRHH", "Ventas", "Atención al Cliente"], width=35,textvariable = self._ph9)
        self.deptoEntry.grid(row=5, column=5)

        # Salario
        self.salarioLabel = Label(self.raiz, text="Salario:", font=('Arial', 15))
        self.salarioLabel.grid(row=6, column=4,  padx=50, pady=5, sticky="w")
        self.salarioEntry = Entry(self.raiz, bd=2, font=('Arial', 15),textvariable = self._ph10)
        self.salarioEntry.grid(row=6, column=5,  padx=5, pady=0)
        
        #--------------------------
        #----------BOTONES---------
        # -------------------------

        # Agregar
        self.agregarBtn = Button(self.raiz, text="Agregar", bd=2, font=('Arial', 20), bg="#84F894", width=15, command=self.agregar)
        self.agregarBtn.grid(row=3, column=6, padx=(30, 0))

        # Actualizar        
        self.actualizarBtn = Button(self.raiz, text="Actualizar", bd=2, font=('Arial', 20), bg="#84E8F8", width=15,command=self.actualizar)
        self.actualizarBtn.grid(row=4, column=6, padx=(30, 0))

        # Eliminar
        self.eliminarBtn = Button(self.raiz, text="Eliminar", bd=2, font=('Arial', 20), bg="#FF9999",width=15, command=self.eliminar)
        self.eliminarBtn.grid(row=5, column=6, padx=(30, 0))

        # Seleccionar
        self.seleccionarBtn = Button(self.raiz, text="Seleccionar", bd=2, font=('Arial', 20), bg="#fdcae1",width=15, command=self.seleccionar)
        self.seleccionarBtn.grid(row=6, column=6, padx=(30, 0))

        # Buscar
        self.buscarBtn = Button(self.raiz, text="Buscar", bd=2, font=('Arial', 20), bg="#ff8000",width=15, command=self.buscar)
        self.buscarBtn.grid(row=7, column=6, padx=(30, 0), pady=(0, 40))
        
        #--------------------------
        #-------VISUALIZADOR-------
        # -------------------------

        # Tabla
        self.tabla_datos = ttk.Treeview(self.raiz)
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('Arial Bold', 15))
        self.tabla_datos['columns'] = ("Id","Nombre","Apellido","DNI","Email","Telefono","Edad","Estado","Fecha Incorporacion","Departamento","Salario")
        self.tabla_datos.column("#0", width=0, stretch=NO)
        self.tabla_datos.column("Id", anchor=W, width=150)
        self.tabla_datos.column("Nombre", anchor=W, width=150)
        self.tabla_datos.column("Apellido", anchor=W, width=150)
        self.tabla_datos.column("DNI", anchor=W, width=150)
        self.tabla_datos.column("Email", anchor=W, width=230)
        self.tabla_datos.column("Telefono", anchor=W, width=150)
        self.tabla_datos.column("Edad", anchor=W, width=150)
        self.tabla_datos.column("Estado", anchor=W, width=150)
        self.tabla_datos.column("Fecha Incorporacion", anchor=W, width=150)
        self.tabla_datos.column("Departamento", anchor=W, width=150)
        self.tabla_datos.column("Salario", anchor=W, width=150)
        self.tabla_datos.heading("#0", text="", anchor=W)
        self.tabla_datos.heading("Id", text="ID", anchor=W)
        self.tabla_datos.heading("Nombre", text="Nombre", anchor=W)
        self.tabla_datos.heading("Apellido", text="Apellido", anchor=W)
        self.tabla_datos.heading("DNI", text="DNI", anchor=W)
        self.tabla_datos.heading("Email", text="Email", anchor=W)
        self.tabla_datos.heading("Telefono", text="Teléfono", anchor=W)
        self.tabla_datos.heading("Edad", text="Edad", anchor=W)
        self.tabla_datos.heading("Estado", text="Estado", anchor=W)
        self.tabla_datos.heading("Fecha Incorporacion", text="Fecha", anchor=W)
        self.tabla_datos.heading("Departamento", text="Depto", anchor=W)
        self.tabla_datos.heading("Salario", text="Salario", anchor=W)
        self.tabla_datos.grid(row=9, column=0, columnspan=7, padx=(20, 0))
        self.tabla_datos.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
        self.actualizar_tabla()