import tkinter as tk
from tkinter import messagebox
import math

def calcular_premio(event=None): # event=None para que funcione también con Enter
    try:
        
        entrada=float(entrada_apueta.get())

        # caso especial
        if entrada ==2500:
            premio_redondeado=4700
        else:
            premio = (2 * entrada - 0.1 * entrada) 
            premio_redondeado= round(premio/100)*100


    

        personas=personas_entrada.get()

        titulo= f"{personas}vs{personas} TRUCO"

        label_resultado.config(text=f"""🤼‍♂️🃏 *{titulo}* 🃏🤼‍♀️
        ♠️ *Entrada ${entrada} * ♠️
        🏆 *Premio  ${premio_redondeado} * 🏆
        ♣️1️⃣  
        ♣️2️⃣ 
        📣 *QUIEN SE UNE???* 📣""" )
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def copiar_texto():
    texto = label_resultado["text"]
    if texto.strip():
        ventana.clipboard_clear()
        ventana.clipboard_append(texto)
        ventana.update()  
        messagebox.showinfo("Copiado", "El texto ha sido copiado")
    else:
        messagebox.showwarning("Advertencia", "No hay texto para copiar")


def limpiar():
    entrada_apueta.delete(0, tk.END)
    personas_entrada.delete(0, tk.END)
    label_resultado.config(text="")

def validar_float(texto):
    if texto == "" or texto == ".":
        return True
    try:
        float(texto)
        return True
    except ValueError:
        return False
    
def validar_int(texto):
    if texto == "":
        return True
    return texto

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Premio de Truco")
ventana.geometry("500x525+400+100")
ventana.configure(bg='yellow green')


# registrar validadores
validar_float_cmd = ventana.register(validar_float)
validar_int_cmd = ventana.register(validar_int)

# Etiqueta y campo de entrada para la apuesta
label_apuesta = tk.Label(ventana, text="Ingrese la apuesta:", bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
label_apuesta.pack(pady=5)

# Campo de entrada
entrada_apueta = tk.Entry(ventana, validate="key", validatecommand=(validar_float_cmd, '%P'))
entrada_apueta.pack(pady=5)

personas_apuesta = tk.Label(ventana, text="Ingrese la cantidad de personas:", bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
personas_apuesta.pack(pady=5)
personas_entrada = tk.Entry(ventana, validate="key", validatecommand=(validar_int_cmd, '%P'))
personas_entrada.pack(pady=5)


# Botón para calcular el premio
boton_calcular = tk.Button(ventana, text="Calcular Premio", command=calcular_premio, bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
boton_calcular.pack(pady=5)

# boton para q entre funcione con calcular premio
ventana.bind('<Return>', calcular_premio)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="", justify=tk.LEFT ,width=40,                    # ancho en caracteres
    height=10, bg="SkyBlue1")
label_resultado.pack(pady=5)


# Botón para copiar el texto
boton_copiar = tk.Button(ventana, text="Copiar Texto", command=copiar_texto, bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
boton_copiar.pack(pady=5)


# boton para limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, bg='SkyBlue1',fg="black", relief="raised", padx=5, pady=5,border=5)
boton_limpiar.pack(pady=5)


button_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg="SkyBlue1", fg="black", relief="raised", padx=5, pady=5,border=5)
button_salir.pack(pady=5)


ventana.mainloop()






