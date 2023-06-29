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
        
        # Barra navegación
        self.scrollbar = ttk.Scrollbar(self.raiz, orient="vertical", command=self.tabla_datos.yview)
        self.scrollbar.grid(row=9, column=8, sticky="ns")
        self.tabla_datos.configure(yscrollcommand=self.scrollbar.set)


        #---------------------------
        #-----------LOGOS-----------
        # --------------------------

        # Imagen UTN
        self.imagen = Image.open("utn.png")
        self.imagen = self.imagen.resize((215,100), Image.ANTIALIAS)
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = Label(self.raiz, image=self.imagen_tk)
        self.label_imagen.grid(row=10, column=0, pady=30, padx=30)

        # Label Datos Obligatorios
        self.label = Label(self.raiz, text="* Datos Obligatorios", font=('Arial Bold', 13),fg="red")
        self.label.grid(row=10, column=3, pady=(80,0))

        # Imagen Kodikikades
        self.imagen3 = Image.open("kodifikades.png")
        self.imagen3 = self.imagen3.resize((250,100), Image.ANTIALIAS)
        self.imagen_tk3 = ImageTk.PhotoImage(self.imagen3)
        self.label_imagen3 = Label(self.raiz, image=self.imagen_tk3)
        self.label_imagen3.grid(row=10, column=6, pady=50, columnspan=3)
        

    #---------------------------
    #----------MÉTODOS----------
    # --------------------------

    def leer(self):
        with Conexion.obtenerConexion() as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM empleados")
            resultados = cursor.fetchall()
            con.commit()
        return resultados    


    #----------Actualizar tabla----------
    def actualizar_tabla(self):
            for data in self.tabla_datos.get_children():
                self.tabla_datos.delete(data)
            data_array = self.leer()
            data_array.sort(reverse=False)  # Invertir el orden de los datos
            for array in data_array:
                self.tabla_datos.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
            self.tabla_datos.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
            

    #----------Limpiar----------
    def limpiar(self):
        for i in range(11):
            self.ph_set("",i)


    #----------SET DE LOS PLACEHOLDERS----------
    def ph_set(self,word,num):
        if word == "None":
            word = ""
        if num ==1:
            self._ph1.set(word)
        if num ==2:
            self._ph2.set(word)
        if num ==3:
            self._ph3.set(word)
        if num ==4:
            self._ph4.set(word)
        if num ==5:
            self._ph5.set(word)
        if num ==6:
            self._ph6.set(word)
        if num ==7:
            self._ph7.set(word)
        if num ==8:
            self._ph8.set(word)
        if num ==9:
            self._ph9.set(word)
        if num ==10:
            self._ph10.set(word)
    
    # ----------AGREGAR-----------
    def agregar(self):
        nombre = str(self.nombreEntry.get())
        apellido = str(self.apellidoEntry.get())
        dni = str(self.dniEntry.get())
        email = str(self.emailEntry.get())
        telefono = str(self.telefonoEntry.get())
        edad = str(self.edadEntry.get())
        estado = str(self.estadoEntry.get())
        fecha = str(self.fechaEntry.get())
        depto = str(self.deptoEntry.get())
        salario = str(self.salarioEntry.get())
        variables = [nombre, apellido, dni, email, telefono, edad, estado, fecha, depto, salario]
        for i in range(len(variables)):
            if not variables[i]:
                variables[i] = None
        if (nombre == "" or nombre == " ") or (apellido == "" or apellido == " ") or (dni == "" or dni == " "):
            messagebox.showinfo("Error", "Complete los datos obligatorios")
            return
        else:
            try:
                with Conexion.obtenerConexion() as con:
                    cursor = con.cursor()
                    cursor.execute("INSERT INTO empleados (nombre, apellido, dni, email, telefono, edad, estado, fecha, depto, salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                                (variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9]))
                    con.commit()
            except:
                messagebox.showinfo("Error", "Ocurrió un error")
                return
        self.actualizar_tabla()
        self.limpiar()

    # ----------SELECCIONAR----------
    def seleccionar(self):
        try:
            item_seleccionado = self.tabla_datos.selection()[0]
            nombre = str(self.tabla_datos.item(item_seleccionado)['values'][1])
            apellido = str(self.tabla_datos.item(item_seleccionado)['values'][2])
            dni = str(self.tabla_datos.item(item_seleccionado)['values'][3])
            email = str(self.tabla_datos.item(item_seleccionado)['values'][4])
            telefono = str(self.tabla_datos.item(item_seleccionado)['values'][5])
            edad = str(self.tabla_datos.item(item_seleccionado)['values'][6])
            estado = str(self.tabla_datos.item(item_seleccionado)['values'][7])
            fecha = str(self.tabla_datos.item(item_seleccionado)['values'][8])
            depto = str(self.tabla_datos.item(item_seleccionado)['values'][9])
            salario = str(self.tabla_datos.item(item_seleccionado)['values'][10])
            self.ph_set(nombre,1)
            self.ph_set(apellido,2)
            self.ph_set(dni,3)
            self.ph_set(email,4)
            self.ph_set(telefono,5)
            self.ph_set(edad,6)
            self.ph_set(estado,7)
            self.ph_set(fecha,8)
            self.ph_set(depto,9)
            self.ph_set(salario,10)
        except:
            messagebox.showinfo("Error", "Debe seleccionar una fila")
