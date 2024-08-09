import csv

# Nombre del archivo CSV de entrada
input_file = 'input.csv'
# Nombre del archivo de salida
output_file = 'output.txt'


# Función para modificar el primer campo
def modify_first_field(value):
    if value:
        return value + '01'  # Modifica según la necesidad
    return value


# Abrir el archivo CSV para leer
with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    # Abrir el archivo de salida para escribir
    with open(output_file, mode='w', encoding='utf-8') as txtfile:
        for row in reader:
            # Modificar el primer campo
            row[0] = modify_first_field(row[0])
            row[3] = row[3].replace('8923002261', '892300226')

            # Ajustar el valor de algunos campos específicos (ejemplo)
            row[4] = row[4].replace('-', '')
            row[8] = row[8].replace('EPS043', 'EPS042')  # Cambio ejemplo
            row[10] = row[10].replace('EPS042', '02')  # Cambio ejemplo

            # row[11] = row[11] if row[11] else '02'  # Valor por defecto para el campo 12 si está vacío

            # Formatear la fila según el formato requerido
            formatted_row = ','.join(row) + '\n'

            # Escribir la fila formateada en el archivo de salida
            txtfile.write(formatted_row)

print("Conversión completada.")



###########################################################


import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os

# Función para modificar el primer campo
def modify_first_field(value):
    if value:
        return value + '01'
    return value

# Función para procesar el archivo CSV
def process_file(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            with open(output_file, mode='w', encoding='utf-8') as txtfile:
                for row in reader:
                    row[0] = modify_first_field(row[0])
                    row[3] = row[3].replace('8923002261', '892300226')
                    row[4] = row[4].replace('-', '')
                    row[8] = row[8].replace('EPS043', 'EPS042')
                    row[10] = row[10].replace('EPS042', '02')

                    formatted_row = ','.join(row) + '\n'
                    txtfile.write(formatted_row)

        messagebox.showinfo("Éxito", f"Archivo procesado y guardado como {output_file}")

    except FileNotFoundError:
        messagebox.showerror("Error", "No se pudo encontrar el archivo especificado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Función para seleccionar el archivo CSV de entrada y salida
def select_files():
    input_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if input_file:
        output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if output_file:
            process_file(input_file, output_file)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Procesador de Archivos CSV")

# Diseño de la interfaz
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

title = tk.Label(frame, text="Procesador de Archivos CSV", font=("Arial", 16))
title.pack(pady=10)

select_button = tk.Button(frame, text="Seleccionar y Procesar Archivo CSV", command=select_files, width=30, height=2)
select_button.pack(pady=20)

exit_button = tk.Button(frame, text="Salir", command=root.quit, width=10, height=2)
exit_button.pack(pady=10)

# Iniciar el bucle de eventos
root.mainloop()


##########################################################################################################################


import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os


# Función para modificar el primer campo (general)
def modify_first_field(value):
    if value:
        return value + '01'
    return value


# Función para procesar archivos CSV (general)
def process_csv(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            with open(output_file, mode='w', encoding='utf-8') as txtfile:
                for row in reader:
                    # Modificaciones para el archivo CSV general
                    row[0] = modify_first_field(row[0])
                    row[3] = row[3].replace('8923002261', '892300226')
                    row[4] = row[4].replace('-', '')
                    row[8] = row[8].replace('EPS043', 'EPS042')
                    row[10] = row[10].replace('EPS042', '02')

                    formatted_row = ','.join(row) + '\n'
                    txtfile.write(formatted_row)

        messagebox.showinfo("Éxito", f"Archivo procesado y guardado como {output_file}")

    except FileNotFoundError:
        messagebox.showerror("Error", "No se pudo encontrar el archivo especificado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# Función para procesar archivos AP
def process_ap_file(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            with open(output_file, mode='w', encoding='utf-8') as txtfile:
                for row in reader:
                    # Correcciones específicas para el archivo AP
                    row[0] = row[0].replace('-', '')
                    row[1] = row[1].replace('2000100366', '200010036601')
                    row[9] = row[9].replace('', '2')
                    row[10] = row[10].replace('', 'Z504')
                    row[13] = row[13].replace('', '3')
                    formatted_row = ','.join(row) + '\n'
                    txtfile.write(formatted_row)

        messagebox.showinfo("Éxito", f"Archivo AP procesado y guardado como {output_file}")

    except FileNotFoundError:
        messagebox.showerror("Error", "No se pudo encontrar el archivo especificado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# Función para seleccionar archivos CSV y AP
def select_file(file_type):
    if file_type == 'csv':
        input_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if input_file:
            output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if output_file:
                process_csv(input_file, output_file)
    elif file_type == 'ap':
        input_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if input_file:
            output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if output_file:
                process_ap_file(input_file, output_file)


# Configuración de la ventana principal
root = tk.Tk()
root.title("Procesador de Archivos")

# Diseño de la interfaz
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

title = tk.Label(frame, text="Procesador de Archivos", font=("Arial", 16))
title.pack(pady=10)

csv_button = tk.Button(frame, text="Seleccionar y Procesar Archivo CSV", command=lambda: select_file('csv'), width=30,
                       height=2)
csv_button.pack(pady=10)

ap_button = tk.Button(frame, text="Seleccionar y Procesar Archivo AP", command=lambda: select_file('ap'), width=30,
                      height=2)
ap_button.pack(pady=10)

exit_button = tk.Button(frame, text="Salir", command=root.quit, width=10, height=2)
exit_button.pack(pady=10)

# Iniciar el bucle de eventos
root.mainloop()
