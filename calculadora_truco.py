import tkinter as tk
from tkinter import messagebox,ttk
import math


#acumuladores globales
total_fondo = 0
last_60 = 0
last_40 = 0


def calcular_premio(event=None): # event=None para que funcione también con Enter
    

        entrada=entrada_apueta.get()
        
        personas=personas_entrada.get()
        
        if entrada == "" or personas=="":
            messagebox.showerror("Error", "Por favor, ingresa todos los valores.")
            return

        try:
            entrada = float(entrada)
            personas = int(personas)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
            return

        # leer comisión del combobox y convertir a decimal (p.ej "14" -> 0.14, "14%" -> 0.14)
        try:
            com_text = comision_var.get().strip()
            com_text = com_text.replace('%', '').replace(',', '.')  # soporta "14" y "14%"
            comision = float(com_text) / 100.0
        except Exception:
            comision = 0.10  # fallback 10%
        

        # calcular comisión
        if entrada == 2500:
            diez_por_ciento_redondeado = 300
        else:
            comision_valor = entrada * comision
            diez_por_ciento_redondeado = round(comision_valor / 100) * 100
        
        # caso especial
        if entrada ==2500:
            premio_redondeado=4700
        else:
            premio = (2 * entrada - comision * entrada) 
            premio_redondeado= round(premio/100)*100


        
        # caso especial para 1vs1
        if personas == 1:
            titulo = "Mano a Mano TRUCO"
        else:
            titulo = f"{personas}vs{personas} TRUCO"
        

        frase_seleccionada = frase_var.get()

        label_resultado.config(text=f"""🇦🇷⚔️🛡️‼ *{titulo}* 🇦🇷⚔️🛡️‼
        💵 *ENTRADA ${entrada:.0f}*
        🏆 *PREMIO ${premio_redondeado:.0f}*

        *{frase_seleccionada}*

        👤  
        👤  

        🇦🇷 *QUIERO RETRUCO ARGENTINO* 🇦🇷""")

    
        

        # #calcular el 10% y guardar el valor
        if entrada == 2500:
            diez_por_ciento_redondeado = 300
        else:
            diez_por_ciento = entrada * comision
        # redondeo normal a la centena más cercana
            diez_por_ciento_redondeado = round(diez_por_ciento / 100) * 100

# registrar en la pestaña 2
        registrar_fondo(diez_por_ciento_redondeado)
    
    
def registrar_fondo(diez_por_ciento):
    global total_fondo, last_60,last_40
    total_fondo += diez_por_ciento
    #linea con la entrada y su 10%
    text_fondo.insert(tk.END,f"{diez_por_ciento}\n")
    #actualiza el total
    label_fondo.config(text=f"Total acumulado: ${total_fondo:0.f}")
    #calcular el 60 del total
    last_60=0.6 * total_fondo
    last_40=0.4* total_fondo
    label_60.config(text=f"60% del fondo: ${last_60:0.f}")
    label_40.config(text=f"40% del fondo: ${last_40:0.f}")

def sumar_fondo():
    # lee todas las líneas del Text
    contenido = text_fondo.get("1.0", tk.END).strip().splitlines()
    total = 0
    for line in contenido:
        try:
            total += float(line)
        except:
            continue

    # actualiza etiquetas
    label_fondo.config(text=f"Total acumulado: ${total:.0f}")
    label_60.config(text=f"60% del fondo: ${total*0.6:.0f}")
    label_40.config(text=f"40% del fondo: ${total*0.4:.0f}")

def copiar_texto():
    texto = label_resultado["text"]
    if texto.strip():
        ventana.clipboard_clear()
        ventana.clipboard_append(texto)
        ventana.update()  
        messagebox.showinfo("Copiado", "El texto ha sido copiado")
    else:
        messagebox.showwarning("Advertencia", "No hay texto para copiar")



def calcular_total():
    global total_fondo
    messagebox.showinfo("Total Acumulado", f"El total acumulado es: ${total_fondo:0.f}")    


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
    try:
        int(texto)
        return True
    except ValueError:
        return False

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Premio de Truco")
#ventana.update_idletasks()
ventana.geometry("400x750")
ventana.configure(bg='#E8F5E9')

#pestañas
notebook = tk.ttk.Notebook(ventana)
notebook.pack(expand=True, fill='both')

#pestaña 1
tab1 = tk.Frame(notebook, bg='#E8F5E9')
notebook.add(tab1, text='Calculadora de Truco')


# registrar validadores
validar_float_cmd = ventana.register(validar_float)
validar_int_cmd = ventana.register(validar_int)

# Etiqueta y campo de entrada para la apuesta
label_apuesta = tk.Label(tab1, text="Ingrese la apuesta:", bg='#E8F5E9',fg="black", relief="flat", padx=5, pady=5)
label_apuesta.pack(pady=5)

# Campo de entrada
entrada_apueta = tk.Entry(tab1, validate="key", validatecommand=(validar_float_cmd, '%P'))
entrada_apueta.pack(pady=5)

personas_apuesta = tk.Label(tab1, text="Ingrese la cantidad de personas:", bg='#E8F5E9',fg="black", relief="flat", padx=5, pady=5)
personas_apuesta.pack(pady=5)
personas_entrada = tk.Entry(tab1, validate="key", validatecommand=(validar_int_cmd, '%P'))
personas_entrada.pack(pady=5)

#seccion de la comision
label_comision = tk.Label(tab1, text="Seleccione comisión (%):", bg='#E8F5E9', fg="black")
label_comision.pack(pady=5)


# combobox con opciones
comision_var = tk.StringVar()
combo_comision = ttk.Combobox(tab1, textvariable=comision_var, state="readonly")
combo_comision['values'] = ("10","11","12","13","14","15")
# valor inicial = "10"
combo_comision.current(0)  
combo_comision.pack(pady=5)

#combobox de partidas 
label_frase= tk.Label(tab1, text="Seleccione modalidad:", bg='#E8F5E9', fg="black")
label_frase.pack(pady=5)

frase_var = tk.StringVar()
combo_frase = ttk.Combobox(tab1, textvariable=frase_var, state="readonly")
combo_frase['values'] = ("A 30 PUNTOS", "A 15 PUNTOS", "MD3 15", "MD3 30", "A LA FALTA")
combo_frase.current(0)  # valor inicial
combo_frase.pack(pady=5)

# Botón para calcular el premio
boton_calcular = tk.Button(tab1, text="Calcular Premio", command=calcular_premio, bg='#A5D6A7',fg="black", relief="flat", padx=5, pady=5)
boton_calcular.pack(pady=5)

# boton para q entre funcione con calcular premio
ventana.bind('<Return>', calcular_premio)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(tab1, text="", justify=tk.LEFT ,width=30,                    # ancho en caracteres
    height=10, bg="#A5D6A7")
label_resultado.pack(pady=5)


# Botón para copiar el texto
boton_copiar = tk.Button(tab1, text="Copiar Texto", command=copiar_texto, bg='#A5D6A7',fg="black", relief="flat", padx=5, pady=5)
boton_copiar.pack(pady=5)


# boton para limpiar
boton_limpiar = tk.Button(tab1, text="Limpiar", command=limpiar, bg='#A5D6A7',fg="black", relief="flat", padx=5, pady=5)
boton_limpiar.pack(pady=5)


button_salir = tk.Button(tab1, text="Salir", command=ventana.destroy, bg="#A5D6A7", fg="black", relief="flat", padx=5, pady=5)
button_salir.pack(pady=5)

# pestaña 2
tab2 = tk.Frame(notebook, bg='#F1F8E9')
notebook.add(tab2, text='Fondo 10%')

label_fondo_titulo = tk.Label(tab2, text="Registro del 10% de las apuestas", bg='#F1F8E9',fg="black", relief="flat", padx=5, pady=5)
label_fondo_titulo.pack(pady=5)


text_fondo = tk.Text(tab2, height=15, width=40, bg="#C8E6C9")
text_fondo.pack(pady=5)

total_fondo = 0
label_fondo = tk.Label(tab2, text="Total acumulado: $0", bg='#F1F8E9',fg="black", relief="flat", padx=5, pady=5)
label_fondo.pack(pady=5)

label_60 = tk.Label(tab2, text="60% del fondo: $0", bg='#F1F8E9',fg="black", relief="flat", padx=5, pady=5)
label_60.pack(pady=5)

#boton para copiar le 60%


label_40 = tk.Label(tab2, text="40% del fondo: $0", bg='#F1F8E9',fg="black", relief="flat", padx=5, pady=5)
label_40.pack(pady=5)

btn_sumar = tk.Button(tab2, text="Sumar Valores", command=sumar_fondo, bg='#A5D6A7')
btn_sumar.pack(pady=5)


#para salir en pestaña 2
button_salir2 = tk.Button(tab2, text="Salir", command=ventana.destroy, bg="#A5D6A7", fg="black", relief="flat", padx=5, pady=5)
button_salir2.pack(pady=5)



ventana.mainloop()
