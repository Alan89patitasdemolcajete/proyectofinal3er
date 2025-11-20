#Proyecto Final
#Submodulo
#Autores:Alan Vargas, Emiliano Carreon Lopez

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - Ropa")
ventana.geometry("500x600")
ventana.resizable(False, False)

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR,"ventas2025.png"))
    imagen = imagen.resize((250, 250))
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo)
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14))
    lbl_sin_logo.pack(pady=40)

# -------------------------
# BOTONES NEGROS (tk.Button)
# -------------------------
ANCHO_BOTON = 25   # tamaño uniforme

def crear_boton(texto, comando):
    return tk.Button(
        ventana,
        text=texto,
        command=comando,
        font=("Arial", 12),
        bg="black",
        fg="white",
        activebackground="#303030",
        activeforeground="white",
        width=ANCHO_BOTON,
        height=2
    )

btn_reg_prod = crear_boton("Registro de Productos", abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = crear_boton("Registro de Ventas", abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = crear_boton("Reportes", abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = crear_boton("Acerca de", abrir_acerca_de)
btn_acerca.pack(pady=10)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()
