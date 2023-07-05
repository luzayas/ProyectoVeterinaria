import altaCliente
import os
import pickle
fichero_cliente = "clientes.pkl"
lista_clientes = []
datos_modificados = False
 
if os.path.exists(fichero_cliente):
    with open(fichero_cliente,'rb') as file: 
        lista_clientes= picke.load(file)

def obtener_cliente (dni):
    for cliente in lista_clientes: 
        if cliente.dni == dni:
            return cliente
        return None


 
#Menu Principal#

def mostrar_Menu():
    print ("\n")
    print ("1 - Alta")
    print ("2- Baja")
    print ("3 - Modificar")
    print ("4 - Mostrar cliente")
    print ("5 - Mostrar clientes")
    print ("6 - Guardar")
    print ("7 - Salir")


#Presentación del sistema. Se hará desde la muestra del menú de opciones. 
    #Menu Principal2# 
while True:
    opcion = mostrar_Menu()
    if opcion == 1: alta_cliente()
    elif opcion == 2: baja_cliente()
    elif  opcion == 3: modificacion_cliente ()
    elif opcion == 4: informacion_cliente()
    elif opcion == 5: informacion_clientes ()
    elif opcion == 6: guardar()
    elif opcion == 7: ladrar ()
    elif opcion == 8: quit
    else: 
            break

#Menu Alta#

def alta_cliente ():
    global datos_modificados
    print ("Por favor, introduzca los siguientes datos: ")
    dni = input ("DNI:")
    if obtener_cliente == None:
        nombre_cliente = input ("Introduzca el nombre del cliente:")
        nombre_perro = input ("Nombre de la mascota:")
        raza = input ("Tipo de raza:")
        perro = altaCliente.Perro (nombre_perro, raza)
        cliente = altaCliente.Cliente(nombre_cliente,dni,perro)
        lista_clientes.append(cliente)
        print("Cliente dado de alta!!")
        datos_modificados=True
    else: 
        print("El cliente ya existe!!!")

#Para dar de alta al cliente, se necesita un nombre y el DNI . Para que no se repitan los datos, el programa ya dará el aviso. 
#Si el cliente no existe, entonces se guardará el dato con la condicional if, la cual pide todos los datos y usará los valores alfanuméricos. 


#Consulta del cliente# 
def informacion_cliente() :
    dni = input("Introduce el DNI del cliente a consultar: ")
    cliente = obtener_cliente(dni)
    if cliente ==None:
        print("----El cliente con DNI " + dni + ", no existe----")
    else:
        print("-----CLIENTE:-----" + "\nNombre: " + cliente.nombre + "\nDNI: " + cliente.dni + "\nNombre de perro: " + cliente.perro.nombre + "\nRaza: " + cliente.perro.raza)
def informacion_clientes():
    tabla = []
    for cliente in lista_clientes:
        print("-----CLIENTE:-----" + "\nNombre: " + cliente.nombre + "\nDNI: " + cliente.dni + "\nNombre de perro: " + cliente.perro.nombre + "\nRaza: " + cliente.perro.raza + "\n")
    pausa = input("Pulsa una letra para continuar")

    #para la consulta general como las de los clientes, se crearán dos funciones que llama al cliente por el DNI y nos muestra todos los datos. Segundo, la función general de clientes, crea una lista y carga a todos los clientes para después buscarla. 
    
def guardar():
    global datos_modificados
    with open(fichero_clientes, 'wb') as filestream:
        pickle.dump(lista_clientes, filestream)
    print("Información del cliente guardada!")
    datos_modificados = False

#Al definir Guardar, se alamacenará la lsita en el fichero de clientes. Es por eso que se utiliza la función open() como escritura binaria. Para lograrlo, se utiliza la estructura condicional with, con el alias filestream. La función dump() del módulo pickle funciona para ello. Finalmente, se asigna la variable datos_modificados a False para que no haga un doble trabajo. 


#Modificación cliente#

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
            altaCliente.nombre = nombre_cliente
            nombre_perro = input("Nombre del Perro: ")
        if nombre_perro != "":
           altaCliente.perro.nombre = nombre_perro
        raza = input("Tipo de raza: ")
        if raza != "":
            altaCliente.perro.raza = raza
        print("Cliente modificado correctament!")
        datos_modificados = True
        
        #Con esta función, se modificarán los datos del cliente dado de alta. Primero se declara la variable global de datos_modificados y luego, se preguntará por el DNI del usuario, para saber si existe este cliente o no. De ser afirmativo, se procederá a su modificación, de la misma manera que se entraron los datos para darlo de alta. Es por eso que se utilizan las condicionales con lógica negada. Una vez finalizado y dado por válido, se utilizará la variable global True. 

#Baja Cliente#
def baja_cliente():
    global datos_modificados
    dni = input("DNI del cliente a dar de baja: ")
    cliente = obtener_cliente(dni)
    if cliente == None:
        print("----El cliente con DNI " + dni + ", no existe----")
    else:
        lista_clientes.remove(cliente)
        print("Cliente borrado exitosamente")
        datos_modificados = True

#Para dar de baja al cliente, se declarará la condición else, ya que remove() lo eliminará del archivo. 
 
 