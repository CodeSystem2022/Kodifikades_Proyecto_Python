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