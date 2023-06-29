# Aquí se podrá dar inicio al programa (interfaz gráfica)
from interface import Interface
from conexion import Conexion

class Main:

    if __name__ == "__main__":
        Conexion.crear_tabla_empleados()
        ventana = Interface()
        ventana.raiz.mainloop()