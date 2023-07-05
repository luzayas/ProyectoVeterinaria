import asyncio   
from tkinter import END
import clases
import os
import pickle


fichero_clientes = "clientes.pkl"
datos_modificados = False
lista_clientes = [] 
if os.path.exists(fichero_clientes):
    with open(fichero_clientes, 'rb') as f:
        lista_clientes = pickle.load(f)

### MENU ###
def mostrar_opciones():
    print("\n")
    print("1- ALTA")
    print("2- BAJA")
    print("3- MODIFICACIÓN")
    print("4- CONSULTA_CLIENTE")
    print("5- CONSULTA GLOBAL")
    print("6- GUARDAR")
    print("7- SALIR")
    opcion = int(input("Introduzca una opción: "))
    print("\n")
    return opcion

def obtener_cliente(dni):
    for cliente in lista_clientes:
        if cliente.dni == dni: return cliente

def alta_cliente():
    global datos_modificados
    print("Por favor, introduzca los siguientes datos:")
    dni =input("DNI: ")
    if obtener_cliente(dni)==None:
        nombre_cliente = input("Nombre del cliente: ")    
        nombre_mascota = input("Nombre de la mascota: ")
        especie = input ("Especie de la mascota: ")
        sexo = input("Sexo de la mascota:")
        edad = input ("Edad de la mascota:")
        rasgos = input ("Rasgos de la mascota:")
        motivo = input ("Motivo de consulta: ")
        print("Cliente dado de alta!!")
        datos_modificados=True
    else:
        print("Ya existe un cliente con el DNI " + dni + "-------")
        def alta_liente ():
            archivo = open ("alta_cliente", 'wb')
            pickle.dump(self.cliente, archivo)
            archivo.close()
            del archivo
     

def modificacion_cliente():
    global datos_modificados
    dni = input("DNI del cliente a modificar? ")
    cliente = obtener_cliente(dni)
    if cliente==None:
        print("---El cliente con DNI " + dni + ", no existe-----")
    else:
        print("Por favor, rellena los siguientes datos:")
        nombre_cliente = input("Nombre del cliente: ")
        if nombre_cliente != "":
            cliente.nombre = nombre_cliente
        nombre_mascota = input ("Nombre de la mascota: ")
        if nombre_mascota != "":
            cliente.mascota.nombre = nombre_mascota
            sexo = input("Sexo de la mascota:")
            edad = input ("Edad de la mascota:")
            rasgos = input ("Rasgos de la mascota:")
            motivo = input ("Motivo de consulta:")
        if mascota != "":
            cliente.mascota.motivo = motivo
        print("----CLIENTE MODIFICADO---")
        datos_modificados = True
        def modificacion_cliente ():
            archivo = open ("modificacion_cliente", 'wb')
            pickle.dump(self.cliente, archivo)
            archivo.close()
            del archivo


def baja_cliente():
    global datos_modificados
    dni = input("DNI del cliente a dar de baja: ")   
    cliente = obtener_cliente(dni)
    if cliente == None:
        print("----El cliente con DNI " + dni + ", no existe----")
    else:
        lista_clientes.remove(cliente)
        print("---CLIENTE BORRADO---")
        datos_modificados = True
    def baja_cliente ():
            archivo = open ("baja_cliente", 'wb')
            pickle.dump(self.cliente, archivo)
            archivo.close()
            del archivo

def informacion_cliente():
    dni = input("Introduce el DNI del cliente a consultar: ")
    cliente = obtener_cliente(dni)
    if cliente ==None:
        print("----El cliente con DNI " + dni + ", no existe----")
    else:
        print("-----CLIENTE:-----" + "\nNombre: " +  cliente.mascota.enfermedad  + "\nDNI: " + cliente.dni + "\nNombre de la mascota: " + 
         cliente.mascota.motivo  + "\nEnfermedad: " +  cliente.mascota.motivo)
def informacion_clientes():
    tabla = []
    for cliente in lista_clientes:
        print("-----CLIENTE:-----" + "\nNombre: " + cliente.nombre + "\nDNI: " + cliente.dni + "\nNombre de la mascota: " + 
         cliente.mascota.motivo + "\nMotivo: " + motivo + "\n")
    pausa = input("Pulsa una letra para continuar")

def guardar():
    global datos_modificados
    with open(fichero_clientes, 'wb') as filestream:
        pickle.dump(lista_clientes, filestream)
    print("Información del cliente guardada!")
    datos_modificados = False


    ##CARGAR MENU ##
while True:
    opcion = mostrar_opciones()
    if opcion == 1: alta_cliente()
    elif opcion == 2: baja_cliente()
    elif opcion == 3: modificacion_cliente()
    elif opcion == 4: informacion_cliente()
    elif opcion == 5: informacion_clientes()
    elif opcion == 6: guardar()
    elif opcion == 7: quit()
    if datos_modificados :
        respuesta = input("¿Quiere guardar los datos realizados?(S/N)")
        if respuesta =="s" or respuesta == "S":
            guardar()
        else:
            break