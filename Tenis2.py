import csv
reservas=[]
canchas = ["Club de Tenis Mantagua", "Club de Tenis Las Salinas","Club de Tenis La Ligua", "Club de Tenis Quilpué", "Club de Tenis La Calera"]
disponibilidad ={
    'nombre': ["Club de Tenis Mantagua", "Club de Tenis Las Salinas","Club de Tenis La Ligua", "Club de Tenis Quilpué", "Club de Tenis La Calera"],
    'valor': [10000, 12000, 14000, 16000, 18000],
    'horario':["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]   
}

#cancha, fecha, hora, nombre, contacto, valor = '','','','','',0
#función para leer el archivo csv y almacenar las reservas en la lista de reservas
def carga_inicial():
    with open('reservas_inicial.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            cancha= fila[0]
            fecha= fila[1]
            hora= fila[2]
            nombre= fila[3]
            contacto= fila[4]
            valor= fila[5]
            reserva ={
                'cancha': cancha,
                'fecha': fecha,
                'hora': hora,
                'nombre': nombre,
                'contacto': contacto,
                'valor': valor
            }
            reservas.append(reserva)
    print("Archivo procesado exitosamente")

def crear_reserva():
    while True:
        while True:
            #seleccionar cancha
            while True:
                i=0
                for cancha in disponibilidad['nombre']:
                    i=i+1
                    print(f"{i} - {cancha}")
                print("Seleccione una cancha: ")
                op = validar_int()
                if op >0 and op <6:
                    cancha = (disponibilidad['nombre'])[op-1]
                    valor= (disponibilidad['valor'])[op-1]
                    print(f"ha seleccionado la cancha {cancha}")
                    break
                else:
                    print("opción incorrecta")
            #Seleccionar fecha
            print("Ingrese una fecha: ")
            fecha = validar_string()
            print("Ha seleccionado la fecha ", fecha)

            #seleccionar hora
            while True:
                i=0
                for hora in disponibilidad['horario']:
                    i=i+1
                    print(f"{i} - {hora}")
                print("Seleccione una hora: ")
                op = validar_int()
                if op >0 and op <10:
                    hora = (disponibilidad['horario'])[op-1]
                    print(f"ha seleccionado la hora {hora}")
                    break
                else:
                    print("opción incorrecta")
            flag=False
            for reserva in reservas:
                if cancha == reserva['cancha'] and  fecha == reserva['fecha'] and hora ==reserva['hora']:
                    flag=True
            if flag==True:
                print("reservado, no disponible")
                ver_disponibilidad(cancha, fecha)
                print("VUELVA A SELECCIONAR LA CANCHA, FECHA Y HORA")
            else:
                print("disponible.......")
                break
            
        #nombre
        print("Ingrese su nombre: ")
        nombre = validar_string()
        print("nombre ingresado correctamente", nombre)   
        #contacto
        print("Ingrese su contacto: ")
        contacto = validar_string()
        print(f"{contacto}, registrado exitosamente")

        #crear el diccionario
        reserva = {
            'cancha': cancha,
            'fecha': fecha,
            'hora': hora,
            'nombre': nombre,
            'contacto': contacto,
            'valor': valor
        }   
        #se agrega la reserva a la lista de reservas
        reservas.append(reserva)
        print("DETALLE DE LA RESERVA")
        print(f"Cancha: {reserva['cancha']}\nFecha: {reserva['fecha']}\nHora: {reserva['hora']}\nValor: {reserva['valor']}\n")
        print("Desea realizar otra reserva:\n S- nuevo pedido\nN- volver al menú\nSalir")
        op = validar_string()
        if op.upper == 'S':
            continue
        elif op.upper()=='N':
            break
        elif op.upper()== 'SALIR':
            exit()

def ver_disponibilidad(cancha =None, fecha=None):
    if cancha == None and fecha ==None:
        #seleccionar cancha 
        while True:
            i=0
            for cancha in disponibilidad['nombre']:
                i=i+1
                print(f"{i} - {cancha}")
            print("Seleccione una cancha: ")
            op = validar_int()
            if op >0 and op <6:
                cancha = (disponibilidad['nombre'])[op-1]
                print(f"ha seleccionado la cancha {cancha}")
                break
            else:
                print("opción incorrecta")
        #Seleccionar fecha
        print("Ingrese una fecha: ")
        fecha = validar_string()
        print("Ha seleccionado la fecha ", fecha)

    #validar si la cancha y la fecha estan en la lista de reservas
    flag =False
    horas_reservadas =[]
    for reserva in reservas:
        if reserva['cancha']== cancha and reserva['fecha']== fecha:
            flag=True
            hora = reserva['hora']
            horas_reservadas.append(hora)
            
    for hora in disponibilidad['horario']:
        if hora in horas_reservadas:
            estado ='reservado'
        else:
            estado='disponible'
        print(f"{hora} - {estado}")
    
def ver_nombre():
    print("Ingrese su nombre para ver las reservas: ")
    nombre = validar_string()
    flag=False
    for reserva in reservas:
        if reserva['nombre'].upper() == nombre.upper():
            flag=True
            print(f"Cancha: {reserva['cancha']}\nFecha: {reserva['fecha']}\nHora: {reserva['hora']}\nValor: {reserva['valor']}\n")
    if flag==False:
        print("No existen reservas para ",nombre)

def crear_archivo():
    with open("reservas.txt", 'w') as archivo:
        archivo.write("------------RESERVAS------------\n")
        for reserva in reservas:
            archivo.write(f"Cancha: {reserva['cancha']}\nFecha: {reserva['fecha']}\nHora: {reserva['hora']}\nValor: {reserva['valor']}\nNombre: {reserva['nombre']}\nContacto: {reserva['contacto']}\n")
            archivo.write("------------------------------------------\n")
def validar_string():
    while True:
        cadena = input()
        if cadena.strip(): #strip() devuelve el string sin espacios, para validar que contenga algun caracter
            return cadena
        else:
            print("El campo no debe estar vacío")

def validar_int():
    while True:
        try:
            num= int(input())
        except ValueError:
            print("Ingrese solo números")
        else: 
            break
    return num
def salir():
    print("CHAO PESCADO")
    exit()

def menu():
    while True:
        print("""
SISTEMA DE RESERVAS
1- Reservar una cancha
2- Consultar disponibilidad
3- Ver por nombre
4- Cargar reservas
5- Guardar reservas
6- salir
              """)
        
        op = validar_string()
        if op =='1':
            crear_reserva()
        elif op == '2':
            ver_disponibilidad()
        elif op == '3':
            ver_nombre()
        elif op == '4':
            carga_inicial()
        elif op == '5':
            crear_archivo()
        elif op == '6':
            salir()
        else:
            print("Opción Incorrecta")

menu()