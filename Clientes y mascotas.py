import sqlite3
from tkinter import *

#Base de datos 
conn = sqlite3.connect('veterinaria.db')
c = conn.cursor()

#Tabla de paciente
c.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                sexo TEXT,
                edad_aprox INTEGER,
                especie TEXT,
                rasgos TEXT,
                enfermedad TEXT,
                nombre_dueno TEXT,
                numero_contacto TEXT,
                alta INTEGER
            )''')

# total de pacientes ingresados
def obtener_cantidad_pacientes():
    c.execute("SELECT COUNT(*) FROM pacientes")
    return c.fetchone()[0]

# pacientes dados de alta
def obtener_cantidad_pacientes_dados_de_alta():
    c.execute("SELECT COUNT(*) FROM pacientes WHERE alta = 1")
    return c.fetchone()[0]

# nuevo paciente
def registrar_paciente():
    nombre = entry_nombre.get()
    sexo = entry_sexo.get()
    edad = entry_edad.get()
    especie = entry_especie.get()
    rasgos = entry_rasgos.get()
    enfermedad = entry_enfermedad.get()
    nombre_dueno = entry_nombre_dueno.get()
    numero_contacto = entry_numero_contacto.get()
    alta = 0

    c.execute("INSERT INTO pacientes (nombre, sexo, edad_aprox, especie, rasgos, enfermedad, nombre_dueno, numero_contacto, alta) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (nombre, sexo, edad, especie, rasgos, enfermedad, nombre_dueno, numero_contacto, alta))
    conn.commit()
    label_mensaje.config(text="Paciente registrado con éxito.")

# consulta paciente 
def consultar_registros():
    c.execute("SELECT * FROM pacientes")
    registros = c.fetchall()

    output_text.delete(1.0, END)
    for paciente in registros:
        output_text.insert(END, f"ID: {paciente[0]}\n")
        output_text.insert(END, f"Nombre: {paciente[1]}\n")
        output_text.insert(END, f"Sexo: {paciente[2]}\n")
        output_text.insert(END, f"Edad: {paciente[3]}\n")
        output_text.insert(END, f"Especie: {paciente[4]}\n")
        output_text.insert(END, f"Rasgos: {paciente[5]}\n")
        output_text.insert(END, f"Enfermedad: {paciente[6]}\n")
        output_text.insert(END, f"Dueño: {paciente[7]}\n")
        output_text.insert(END, f"Contacto: {paciente[8]}\n")
        output_text.insert(END, "\n")

# registro paciente
def modificar_registro():
    id_paciente = entry_id.get()

    c.execute("SELECT * FROM pacientes WHERE id=?", (id_paciente,))
    paciente = c.fetchone()

    if paciente:
        nombre = entry_nombre.get()
        sexo = entry_sexo.get()
        edad = entry_edad.get()
        especie = entry_especie.get()
        rasgos = entry_rasgos.get()
        enfermedad = entry_enfermedad.get()
        nombre_dueno = entry_nombre 
def eliminar_paciente():
    id_paciente = entry_id.get()

    c.execute("SELECT * FROM pacientes WHERE id=?", (id_paciente,))
    paciente = c.fetchone()

    if paciente:
        c.execute("DELETE FROM pacientes WHERE id=?", (id_paciente,))
        conn.commit()
        label_mensaje.config(text="Paciente dado de alta correctamente.")
    else:
        label_mensaje.config(text="No se encontró ningún paciente con ese ID.")

#reporte
def generar_reportes():
    total_pacientes = obtener_cantidad_pacientes()
    total_pacientes_alta = obtener_cantidad_pacientes_dados_de_alta()

    output_text.delete(1.0, END)
    output_text.insert(END, f"Total de pacientes ingresados: {total_pacientes}\n")
    output_text.insert(END, f"Total de pacientes dados de alta: {total_pacientes_alta}\n")

# Salir del programa
def salir():
    conn.close()
    ventana.destroy()

# Crear la interfaz gráfica
ventana = Tk()
ventana.title("Sistema de gestión de pacientes en Veterinaria")

label_nombre = Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, sticky=W)
entry_nombre = Entry(ventana)
entry_nombre.grid(row=0, column=1)

label_sexo = Label(ventana, text="Sexo:")
label_sexo.grid(row=1, column=0, sticky=W)
entry_sexo = Entry(ventana)
entry_sexo.grid(row=1, column=1)

label_edad = Label(ventana, text="Edad:")
label_edad.grid(row=2, column=0, sticky=W)
entry_edad = Entry(ventana)
entry_edad.grid(row=2, column=1)

label_especie = Label(ventana, text="Especie:")
label_especie.grid(row=3, column=0, sticky=W)
entry_especie = Entry(ventana)
entry_especie.grid(row=3, column=1)

label_rasgos = Label(ventana, text="Rasgos:")
label_rasgos.grid(row=4, column=0, sticky=W)
entry_rasgos = Entry(ventana)
entry_rasgos.grid(row=4, column=1)

label_enfermedad = Label(ventana, text="Enfermedad:")
label_enfermedad.grid(row=5, column=0, sticky=W)
entry_enfermedad = Entry(ventana)
entry_enfermedad.grid(row=5, column=1)

label_nombre_dueno = Label(ventana, text="Nombre del dueño:")
label_nombre_dueno.grid(row=6, column=0, sticky=W)
entry_nombre_dueno = Entry(ventana)
entry_nombre_dueno.grid(row=6, column=1)

label_numero_contacto = Label(ventana, text="Número de contacto:")
label_numero_contacto.grid(row=7, column=0, sticky=W)
entry_numero_contacto = Entry(ventana)
entry_numero_contacto.grid(row=7, column=1)

label_id = Label(ventana, text="ID del paciente:")
label_id.grid(row=8, column=0, sticky=W)
entry_id = Entry(ventana)
entry_id.grid(row=8, column=1)

button_registrar = Button(ventana, text="Registrar paciente", command=registrar_paciente)
button_registrar.grid(row=9, column=0, pady=10)

button_consultar = Button(ventana, text="Consultar registros", command=consultar_registros)
button_consultar.grid(row=9, column=1, pady=10)

button_modificar = Button(ventana, text="Modificar registro", command=modificar_registro)
button_modificar.grid(row=10, column=0)

button_eliminar = Button(ventana, text="Dar de alta a paciente", command=eliminar_paciente)
button_eliminar.grid(row=10, column=1)

button_reportes = Button(ventana, text="Generar reportes", command=generar_reportes)
button_reportes.grid(row=11, column=0, pady=10)

button_salir = Button(ventana, text="Salir", command=salir)
button_salir.grid(row=11, column=1)

label_mensaje = Label(ventana, text="")
label_mensaje.grid(row=12, columnspan=2)

output_text = Text(ventana, width=50, height=10)
output_text.grid(row=13, columnspan=2, pady=10)

ventana.mainloop()
