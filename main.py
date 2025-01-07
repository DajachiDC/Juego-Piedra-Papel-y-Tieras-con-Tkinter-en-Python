import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

### FUNCIONES ###

# detectar cuando el usuario seleccionar un elemento del combobox
def seleccionar_elemento(event):
    global seleccion_user
    seleccion_user = combobox.get()
    print(f"Has seleccionado: {seleccion_user}")


# detectar cundo el usuario da click al botón
def click_boton():
    eleccion_maquina = random.choice(elementos)

    if not seleccion_user:
        messagebox.showerror("¡ERROR!", "Debes seleccionar una opción.")

    # Empate
    if seleccion_user == eleccion_maquina:
        messagebox.showinfo("¡EMPATE!", f"Tú: {seleccion_user} - Maquina: {eleccion_maquina}")
    
    # Usuario: papel - Maquina: piedra / Usuario gana contra piedra
    elif seleccion_user == "Papel" and eleccion_maquina == "Piedra":
        messagebox.showinfo("¡GANASTE!", f"Tú: {seleccion_user} - Maquina: {eleccion_maquina}   ¡Ganas contra Piedra!")
    
    # Usuario: tijeras - Maquina: papel / Usuario gana contra papel
    elif seleccion_user == "Tijeras" and eleccion_maquina == "Papel":
        messagebox.showinfo("¡GANASTE!", f"Tú: {seleccion_user} - Maquina: {eleccion_maquina}   ¡Ganas contra Papel!")
    
    # Usuario: piedra - Maquina: tijeras / Usuario gana contra tijeras
    elif seleccion_user == "Piedra" and eleccion_maquina == "Tijeras":
        messagebox.showinfo("¡GANASTE!", f"Tú: {seleccion_user} - Maquina: {eleccion_maquina}   ¡Ganas contra Tijeras!")
    
    # Pierde el usuario
    else:
        messagebox.showinfo("¡PERDISTE!", f"Tú: {seleccion_user} - Maquina: {eleccion_maquina}  ¡Perdiste contra {eleccion_maquina}!")


# Creaación de la ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel y Tijeras - By: Dajachi")
ventana.geometry("400x250")


# Labels y Widgets

label1 = tk.Label(ventana, text="Selecciona: ", font=("Arial", 25, "bold")).pack()

combobox = ttk.Combobox(ventana, width=25, font=("Arial", 15, "bold"))
combobox.pack(pady=20)

elementos = ["Piedra", "Papel", "Tijeras"]
combobox["values"] = elementos


label2 = tk.Label(ventana, text="Generar elección de la maquina:", font=("Arial", 15, "bold")).pack()
boton_generar = tk.Button(ventana, text="GENERAR", font=("Arial", 20, "bold"), fg="green", command=click_boton).pack()


combobox.bind("<<ComboboxSelected>>", seleccionar_elemento)



# Bucle de la ventana
ventana.mainloop()