import json

""" Función: menu
Objetivo:
    Función que contiene el menú de opciones que el usuario puede ejecutar.
"""

def menu():
    usuariosNoRegistrados = {"usuarios": []}
    usuarios = {"usuarios": []}
    asociarVehiculoConPiso = {}
    [pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz] = crearMatricesPisos()
    x = int(input("Opciones: \n 1. Registrar Vehiculo. \n 2. Cargar Archivos usuarios \n 3. Cargar archivo parqueaderos \n 4. Ingresar vehiculo \n 5. Salida de vehículo.\n 6. Generar estadísticas.\n -1 Para terminar \n"))
    while x != -1:
        if x == 1:
            usuarios = registrarVehiculo(usuarios)
        elif x == 2:
            usuariosTemp = cargaDeArchivos(1)
            usuarios["usuarios"] += usuariosTemp["usuarios"]
        elif x == 3:
            tipoDeParqueaderos = cargaDeArchivos(2)
        elif x == 4:
            [pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, asociarVehiculoConPiso] = ingresarVehiculo(usuarios, usuariosNoRegistrados, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, asociarVehiculoConPiso)
        elif x == 5:
            [usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz] = retirarVehiculo(usuarios, usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz)
        elif x == 6:
            estadisticasPorPiso(pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz)
            estadisticasPorTipoDeUsuario(asociarVehiculoConPiso)
            estadisticasPorTipoDeVehiculo(asociarVehiculoConPiso)
        x = int(input("Opciones: \n 1. Registrar Vehiculo. \n 2. Cargar Archivos usuarios \n 3. Cargar archivo parqueaderos \n 4. Ingresar vehiculo\n 5. Salida de vehículo.\n 6. Generar estadísticas.\n -1 Para terminar \n"))

""" Función: crearMatricesPisos
Objetivo:
    Función que contiene las matrices de todos los pisos.
Salida (6 matrices):
    Devuelve 6 matrices correspondientes a cada piso
"""

def crearMatricesPisos():
    pisoUnoMatriz =     [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

    pisoDosMatriz =     [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

    pisoTresMatriz =    [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

    pisoCuatroMatriz = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

    pisoCincoMatriz =  [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]
    
    pisoSeisMatriz =    [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

    return pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz

""" Función: cargaDeArchivos
Objetivo:
    Función que carga y retorna los archivos json de usuarios y tipos de parqueaderos.
Entrada:
    numero: identificador del tipo de archivo que se quiere cargar.
Salida (diccionario):
    1: devuelve el diccionario con los usuarios registrados dentro del parqueadero
    2: devuelve el diccionario con los tipos de parqueaderos.
"""

def cargaDeArchivos(tipoDeArchivo):
    if tipoDeArchivo == 1:
        with open("usuarios.json", "r", encoding="utf-8") as file:
            usuarios = json.load(file)
            return usuarios
    elif tipoDeArchivo == 2:
        with open("tiposParqueaderos.json", "r") as file:
            tipoDeParqueaderos = json.load(file)
            return tipoDeParqueaderos

""" Función: registrarVehiculo
Objetivo:
    Función que se encarga de registrar un nuevo usuario dentro del diccionario de usuarios.
Entrada:
    diccionario: que contiene todos los usuarios dentro del parqueadero.
Salida (diccionario):
    1: devuelve el diccionario de usuarios (en caso de que no este registrado ya) con el nuevo usuario registrado
"""

def registrarVehiculo(usuarios):
    identificacion = eval(input("Ingrese la identificación del usuario: \n"))
    [registrado, posicion] = revisarPlaca(usuarios, identificacion)
    if registrado:
        print("Este usuario ya se encuentra registrado")
        return usuarios
    nombre = input("Ingrese el nombre de la persona: \n")
    apellido = input("Ingrese el apellido de la persona: \n")

    tipoDeUsuario = int(input("Ingrese el tipo de usuario: \n1. Estudiante\n2. Profesor\n3. Personal Administrativo\n"))
    
    if tipoDeUsuario == 1:
        tipoDeUsuario = "Estudiante"
    elif tipoDeUsuario == 2:
        tipoDeUsuario = "Profesor"
    elif tipoDeUsuario == 3:
        tipoDeUsuario = "Personal Administrativo"

    placa = input("Ingrese la placa del vehículo: \n")

    tipoDeVehiculo =  int(input("Ingrese el tipo de vehículo: \n1. Automóvil\n2. Automóvil Eléctrico\n3. Motocicleta\n4. Discapacitado\n"))
    if tipoDeVehiculo == 1:
        tipoDeVehiculo = "Automóvil"
    elif tipoDeVehiculo == 2:
        tipoDeVehiculo = "Automóvil Eléctrico"
    elif tipoDeVehiculo == 3:
        tipoDeVehiculo = "Motocicleta"
    elif tipoDeVehiculo == 4:
        tipoDeVehiculo = "Discapacitado"

    planDePago = int(input("Ingrese el plan de pago: \n1. Mensualiad\n2. Diario\n"))
    if planDePago == 1:
        planDePago = "Mensualiad"
    elif planDePago == 2:
        planDePago = "Diario"
    

    usuarios["usuarios"].append([nombre + apellido, identificacion, tipoDeUsuario, placa, tipoDeVehiculo, planDePago]) 

    return usuarios

""" Función: ingresarVehiculo
Objetivo:
    Función que se encarga de verificar que el usuario no tenga un vehículo
    dentro del parqueadero, en caso de ser así, continuará llamanda a las funciones
    de registro.
Entrada:
    diccionario: que contiene todos los usuarios dentro del parqueadero.
Salida (diccionario):
    1: 
"""

def ingresarVehiculo(usuarios, usuariosNoRegistrados, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, asociarVehiculoConPiso):
    placa = input("Ingrese la placa del vehiculo \n")
    [registrada, posicion] = revisarPlaca(usuarios, placa)
    dentroDelParqueadero = revisarRegistro(placa, asociarVehiculoConPiso.keys())
    if (registrada) and (not dentroDelParqueadero):  
        [pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, asociarVehiculoConPiso] = ubicarVehiculo(usuarios, 3, 2 ,tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, placa, asociarVehiculoConPiso)
    elif (not dentroDelParqueadero):
        usuariosNoRegistrados = registrarVehiculoDiario(placa, usuariosNoRegistrados)
        [pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, asociarVehiculoConPiso] = ubicarVehiculo(usuariosNoRegistrados, 0, 3, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, placa, asociarVehiculoConPiso)
    else:
        print("Este vehiculo se encuentra dentro del paqueadero")
    return pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, asociarVehiculoConPiso

""" Función: registrarVehiculoDiario
Objetivo:
    Función que registra a los usuarios que no están dentro del diccionario de usuarios principal.
Entrada:
    diccionario: que contiene los usuarios no registrados en el parqueadero.
    string: numero de la placa del vehículo del usuario
Salida (diccionario):
    1: devuelve el diccionario de usuarios no registrados, con el usuario añadido
"""

def registrarVehiculoDiario(placa, usuariosNoRegistrados):
    # usuariosNoRegistrados es un diccionario que contiene todos los usuarios
    # que llegan al parqueadero y no estan registrados en el diccionario usuarios
    tipoDeVehiculo = input("Ingrese el tipo de vehiculo: \n")
    usuariosNoRegistrados["usuarios"].append([placa, tipoDeVehiculo, "Diario", "Visitante"])
    return usuariosNoRegistrados

""" Función: ubicarVehiculo
Objetivo:
    Función que muestra las posiciones disponibles al usuario para su tipo de vehículo.
Entrada:
    diccionario: que contiene los usuarios no registrados o registrados en el parqueadero
    string: numero de la placa del vehículo del usuario
    matrices: 6 matrices correspondientes a los pisos del parqueadero
    diccionario: que almacena la información del usuario con el piso en el que estaciona
Salida (diccionario):
    1: matrices de los pisos
    2: diccionario con los datos del usuario y el piso donde estacionó
"""

def ubicarVehiculo(usuarios, posicion, posicionTipoUsuario, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, placa, asociarVehiculoConPiso):
    size = len(usuarios["usuarios"])
    buscarDos = 0
    buscar = 1
    #Bucle que se encarga de saber que tipo de vehículo tiene el usuario, le asigna estos valores a una o unas variables
    #dependiendo si el vehículo puede estar en dos tipos de posiciones.
    for y in range(size):
        if usuarios["usuarios"][y][posicion] == placa:
            if usuarios["usuarios"][y][posicion + 1] == "Automóvil":
                buscar = 1
                break
            elif usuarios["usuarios"][y][posicion + 1] == "Automóvil Eléctrico":
                buscar = 1
                buscarDos = 2
                break
            elif usuarios["usuarios"][y][posicion + 1] == "Motocicleta":
                buscar = 3
                break
            elif usuarios["usuarios"][y][posicion + 1] == "Discapacitado":
                buscar = 1
                buscarDos = 4
                break

    #Variable que contiene la cantidad de posiciones de cada piso.
    cantidadDePosiciones = posicionesDesocupadas(buscar, buscarDos, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz)
    
    #Se le pide al usuario en que piso desea parquear mostrando el total de posiciones disponibles para su vehículo
    #en ese piso. 
    #Se válida que el piso en esa posición tenga mínimo una posición disponible. En caso de que no, se vuelve a 
    #imprime un error y se vuelve a pedir el piso.
    while True:
        piso = int(input(f"Ingrese el piso donde desea parquear: "
                        f"\n1. Piso 1 (Posiciones desocupadas: {cantidadDePosiciones[0]})" 
                        f"\n2. Piso 2 (Posiciones desocupadas: {cantidadDePosiciones[1]})"
                        f"\n3. Piso 3 (Posiciones desocupadas: {cantidadDePosiciones[2]})" 
                        f"\n4. Piso 4 (Posiciones desocupadas: {cantidadDePosiciones[3]})"
                        f"\n5. Piso 5 (Posiciones desocupadas: {cantidadDePosiciones[4]})" 
                        f"\n6. Piso 6 (Posiciones desocupadas: {cantidadDePosiciones[5]})" 
                        "\n"))
        if cantidadDePosiciones[piso - 1] > 0:
            break
        print("No hay sitios disponibles en este piso, introduzca otro")

    #Dependiendo del piso elegido por el usuario, se llama la función de cambiar el estado del piso.

    if piso == 1:
        [pisoUnoMatriz, asociarVehiculoConPiso] = cambiarEstadoAOcupado(tipoDeParqueaderos["Piso1"], placa, buscar, buscarDos, pisoUnoMatriz, asociarVehiculoConPiso, "Piso1", usuarios["usuarios"][y][posicion + 1], usuarios["usuarios"][y][posicionTipoUsuario])
    elif piso == 2:
        [pisoDosMatriz, asociarVehiculoConPiso] = cambiarEstadoAOcupado(tipoDeParqueaderos["Piso2"], placa, buscar, buscarDos, pisoDosMatriz, asociarVehiculoConPiso, "Piso2", usuarios["usuarios"][y][posicion + 1], usuarios["usuarios"][y][posicionTipoUsuario])
    elif piso == 3:
        [pisoTresMatriz, asociarVehiculoConPiso] = cambiarEstadoAOcupado(tipoDeParqueaderos["Piso3"], placa, buscar, buscarDos, pisoTresMatriz, asociarVehiculoConPiso, "Piso3", usuarios["usuarios"][y][posicion + 1], usuarios["usuarios"][y][posicionTipoUsuario])
    elif piso == 4:
        [pisoCuatroMatriz, asociarVehiculoConPiso] = cambiarEstadoAOcupado(tipoDeParqueaderos["Piso4"], placa, buscar, buscarDos, pisoCuatroMatriz, asociarVehiculoConPiso, "Piso4", usuarios["usuarios"][y][posicion + 1], usuarios["usuarios"][y][posicionTipoUsuario])
    elif piso == 5:
        [pisoCincoMatriz, asociarVehiculoConPiso] = cambiarEstadoAOcupado(tipoDeParqueaderos["Piso5"], placa, buscar, buscarDos, pisoCincoMatriz, asociarVehiculoConPiso, "Piso5", usuarios["usuarios"][y][posicion + 1], usuarios["usuarios"][y][posicionTipoUsuario])
    elif piso == 6:
        [pisoSeisMatriz, asociarVehiculoConPiso] = cambiarEstadoAOcupado(tipoDeParqueaderos["Piso6"], placa, buscar, buscarDos, pisoSeisMatriz, asociarVehiculoConPiso, "Piso6", usuarios["usuarios"][y][posicion + 1], usuarios["usuarios"][y][posicionTipoUsuario])

    return pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, asociarVehiculoConPiso

""" Función: cambiarEstadoAOcupado
Objetivo:
    Función que permite al usuario elegir la posición para parquear. Genera además las posiciones disponibles tanto 
    para el tipo de vehículo como para la disponibilidad del sitio.
Entrada:
    
Salida (diccionario):
    
"""

def cambiarEstadoAOcupado(infoPiso, placa, buscar, buscarDos, piso, asociarVehiculoConPiso, numPiso, tipoDeVehiculo, tipoDeUsuario):
    print("Las Posiciones disponibles se representan con un 0")
    # Se muestra al usuario las posiciones desocupadas para su tipo de vehículo en el piso elegido
    # El usuario elige por fila y columna la posición que desea. 
    while True:
        for y in range(len(piso)):
            for w in range(len(piso[y])):
                if (infoPiso[y][w] == buscar or infoPiso[y][w] == buscarDos)  and piso[y][w] == "0":
                    print("0 ", end="")
                else:
                    print("X ", end="")
            print()

        fila = int(input("Ingrese la fila donde desea ubicar su vehículo: \n"))
        columna = int(input("Ingrese la columna donde desea ubicar su vehículo: \n"))
        
        # Se válida que la posición elegida por el usuario, esté desocupada, y corresponda a su tipo de vehículo.
        # En caso de estar ocupada o no ser compatible, se le vuelve a pedir al usuario la posición donde sea parquear.

        if (infoPiso[fila][columna] == buscar or infoPiso[fila][columna] == buscarDos) and piso[fila][columna] == "0":
            piso[fila][columna] = "X"
            
            # Se crea el diccionario asociarVehiculoConPiso cuyas llaves son las placas de los vehículos. Cada llave contiene una lista
            # con el Piso donde parqueó el usuario, la fila, la columna, el tipo de usuario, y el tipo de vehículo.

            asociarVehiculoConPiso[placa] = [numPiso, fila, columna, tipoDeUsuario, tipoDeVehiculo]
            print("Se ha registrado su vehículo.")
            return piso, asociarVehiculoConPiso
        else:
            print("Posición ocupada o no compatible con el vehículo")

""" Función: posicionesDesocupadas
Objetivo:
    Función que cálcula el total de posiciones desocupadas en cada piso para el tipo de vehículo del usuario.
Entrada:
    buscar: identificador de un tipo de vehículo
    buscarDos: identificador de un tipo de vehículo
    matrices: 6 matrices correspondientes a los pisos
Salida (diccionario):
    1: lista con el total de posiciones disponibles en cada piso
"""

def posicionesDesocupadas(buscar, buscarDos, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz):
    cantidadDePosiciones = [0, 0, 0, 0, 0, 0]

    # Bucle que se encarga de recorrer todos los pisos del parqueadero buscando las posiciones desocupadas para el
    # tipo de vehículo solicitado. El tipo de vehículo solicitado se refleja en las variables buscar y buscar dos, 
    # en caso de que el vehículo solo tenga una posición que pueda ocupar, como en el caso de los automóviles normales.
    # La variable buscarDos por defecto sería 0.

    for x in range(10):
        for y in range(10):
            if (tipoDeParqueaderos["Piso1"][x][y] == buscar or tipoDeParqueaderos["Piso1"][x][y] == buscarDos)  and pisoUnoMatriz[x][y] == "0":
                cantidadDePosiciones[0] += 1
            if (tipoDeParqueaderos["Piso2"][x][y] == buscar or tipoDeParqueaderos["Piso2"][x][y] == buscarDos) and pisoDosMatriz[x][y] == "0":
                cantidadDePosiciones[1] += 1
            if (tipoDeParqueaderos["Piso3"][x][y] == buscar or tipoDeParqueaderos["Piso3"][x][y] == buscarDos) and pisoTresMatriz[x][y] == "0":
                cantidadDePosiciones[2] += 1
            if (tipoDeParqueaderos["Piso4"][x][y] == buscar or tipoDeParqueaderos["Piso4"][x][y] == buscarDos) and pisoCuatroMatriz[x][y] == "0":
                cantidadDePosiciones[3] += 1
            if (tipoDeParqueaderos["Piso5"][x][y] == buscar or tipoDeParqueaderos["Piso5"][x][y] == buscarDos) and pisoCincoMatriz[x][y] == "0":
                cantidadDePosiciones[4] += 1
    for w in range(5):
        for z in range(10):
            if (tipoDeParqueaderos["Piso6"][w][z] == buscar or tipoDeParqueaderos["Piso6"][w][z] == buscarDos) and pisoSeisMatriz[w][z] == "0":
                cantidadDePosiciones[5] += 1

    return cantidadDePosiciones

""" Función: posicionesDesocupadas
Objetivo:
    Función que cálcula el total de posiciones desocupadas en cada piso para el tipo de vehículo del usuario.
Entrada:
    buscar: identificador de un tipo de vehículo
    buscarDos: identificador de un tipo de vehículo
    matrices: 6 matrices correspondientes a los pisos
Salida (diccionario):
    1: lista con el total de posiciones disponibles en cada piso
"""

def retirarVehiculo(usuarios, usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz):
    placa = input("Ingrese la placa del vehículo que se va a retirar: \n")

    # Se válida que el vehículo si esté dentro del parqueadero. En caso de no estar se retorna vacío.

    if not revisarRegistro(placa, asociarVehiculoConPiso.keys()):
        print("El vehículo no se encuentra dentro del parqueadero.")
        return usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz
    horas = eval(input("Ingrese el numero de horas que permaneció el vehículo en el parqueadero: \n")) 

    # Condicional que válida si el tipo de dato ingresado por usuario no es un entero.
    # en caso de no serlo, se procede a convertirlo a entero, y sumarle uno para aproximarlo a 
    # su valor superior.

    if type(horas) != int:
        horas = int(horas) + 1

    # Se válida si la placa del vehículo se encuentra dentro del diccionario usuariosNoRegistrados.
    # En caso de ser así, se borra al vehículo dentro del diccionario de vehículos dentro del parqueadero.
    # Y se borra al usuario del diccionario en el cual estaba registrado temporalmente.

    [registrada, posicion] = revisarPlaca(usuariosNoRegistrados, placa)
    if registrada:
        posiciones = asociarVehiculoConPiso[placa]
        
        [pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz] = quitarVehiculo(posiciones, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz)
        
        asociarVehiculoConPiso.pop(placa)
        usuariosNoRegistrados["usuarios"].pop(posicion)

        valorAPagar = 3000 * horas
        print("El valor a pagar es ", valorAPagar)

        return usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz
    


    [registrada, posicion] = revisarPlaca(usuarios, placa)

    # Se válida si la placa del vehículo se encuentra dentro del diccionario usuarios.
    # En caso de ser así, se borra al vehículo dentro del diccionario de vehículos dentro del parqueadero.

    if not registrada:
        return usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz
    
    # Se llama a la función de quitar vehículo utilizando la lista que contiene el piso donde estacionó el usuario, la fila y la columna.

    posiciones = asociarVehiculoConPiso[placa]
    [pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz] = quitarVehiculo(posiciones, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz)

    # Se busca que tipo de cobro tiene el usuario. En caso de ser mensualidad se retorna. En caso de ser diario
    # se procede a buscar que tipo de usuario es, y de esa manera se le asigna el precio por hora.

    if usuarios["usuarios"][posicion][5] == "Mensualidad":
        asociarVehiculoConPiso.pop(placa)
        print("El usuarios tiene mensualidad. \n No se genera cobro.")
        return usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz
    if usuarios["usuarios"][posicion][2] == "Estudiante":
        precio = 1000
    elif usuarios["usuarios"][posicion][2] == "Profesor":
        precio = 2000
    elif usuarios["usuarios"][posicion][2] == "Personal Administrativo":
        precio = 1500
        
    valorAPagar = precio * horas
    print("El valor a pagar es ", valorAPagar)

    # Se elimina al vehículo del diccionario que contiene todos los vehículos dentro del parqueadero.

    asociarVehiculoConPiso.pop(placa)
    return usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz

""" Función: quitarVehiculo
Objetivo:
    Función que cambia el estado del piso donde parqueó el usuario a desocuopado.
"""
def quitarVehiculo(posiciones, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz):
    if posiciones[0] == "Piso1":
        pisoUnoMatriz[posiciones[1]][posiciones[2]] = "0"
    elif posiciones[0] == "Piso2":
        pisoDosMatriz[posiciones[1]][posiciones[2]] = "0"
    elif posiciones[0] == "Piso3":
        pisoTresMatriz[posiciones[1]][posiciones[2]] = "0"
    elif posiciones[0] == "Piso4":
        pisoCuatroMatriz[posiciones[1]][posiciones[2]] = "0"
    elif posiciones[0] == "Piso5":
        pisoCincoMatriz[posiciones[1]][posiciones[2]] = "0"
    elif posiciones[0] == "Piso6":
        pisoSeisMatriz[posiciones[1]][posiciones[2]] = "0"

    return pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz

""" Función: revisarPlaca
Objetivo:
    Función que se encarga de validar si la placa se encuentra dentro del diccionario dado.
Entrada:
    diccionario: que contiene los usuarios donde se requiera revisar la placa.
    string: con la placa que se quiera buscar.
salida:
    True: si la placa se encuentra.
    False: si la placa no se encuentra
"""

def revisarPlaca(usuarios, placa):
    size = len(usuarios["usuarios"])
    for y in range(size):
        if placa in usuarios["usuarios"][y] :
            return True, y
    return False, 0

""" Función: revisarRegistro
Objetivo:
    Función que se encarga de validar si el vehículo se encuentra dentro del parqueadero.
Entrada:
    Lista: que contiene las placas de los vehículos dentro del parqueadero.
    string: con la placa que se quiera buscar.
salida:
    True: si la placa se encuentra.
    False: si la placa no se encuentra
"""

def revisarRegistro(placa, llaves):
    if placa in llaves:
        return True
    return False

""" Función: estadisticasPorPiso
Objetivo:
    Función que se encarga registrar en un archivo de texto la cantidad de vehículos que hay en cada piso.
Entrada:
    Matrices: que contienen los vehículos que hay en cada piso.
"""

def estadisticasPorPiso(pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz):
    # Variable de tipo lista que contiene la cantidad de pisos del parqueadero.
    cantidadDePosiciones = [0, 0, 0, 0, 0, 0]
    # Bucle que en caso de encontrar una "X" en esa posición suma 1 a la variable cantidadDePosiciones que ejerce el rol 
    # de contador.
    for x in range(10):
        for y in range(10):
            if pisoUnoMatriz[x][y] == "X":
                cantidadDePosiciones[0] += 1
            if pisoDosMatriz[x][y] == "X":
                cantidadDePosiciones[1] += 1
            if pisoTresMatriz[x][y] == "X":
                cantidadDePosiciones[2] += 1
            if pisoCuatroMatriz[x][y] == "X":
                cantidadDePosiciones[3] += 1
            if pisoCincoMatriz[x][y] == "X":
                cantidadDePosiciones[4] += 1
    for w in range(5):
        for z in range(10):
            if pisoSeisMatriz[w][z] == "X":
                cantidadDePosiciones[5] += 1
    porcentaje = []

    # Se hace una regla de tres para saber el porcentaje de ocupación de cada piso.

    for a in range(5):
        porcentaje.append((cantidadDePosiciones[a] * 100) / 100)
    
    porcentaje.append((cantidadDePosiciones[5] * 100) / 50)
    porcentaje.append((sum(cantidadDePosiciones) * 100) / 550)

    # Se abre un archivo de texto en el que se escribirán los porcentajes de ocupación.

    archivoTexto = open("archivoEstadisticasPorPiso.txt", "w")

    archivoTexto.write("Piso 1 " + str(porcentaje[0]) + "%\n")
    archivoTexto.write("Piso 2 " + str(porcentaje[1]) + "%\n")
    archivoTexto.write("Piso 3 " + str(porcentaje[2]) + "%\n")
    archivoTexto.write("Piso 4 " + str(porcentaje[3]) + "%\n")
    archivoTexto.write("Piso 5 " + str(porcentaje[4]) + "%\n")
    archivoTexto.write("Piso 6 " + str(porcentaje[5]) + "%\n")
    archivoTexto.write("Todos los pisos " + str(porcentaje[6]) + "%\n")
    archivoTexto.close()
    return

""" Función: estadisticasPorTipoDeUsuario
Objetivo:
    Función que se encarga registrar en un archivo de texto la cantidad de vehículos que hay por tipo de usuario.
Entrada:
    Diccionario: que contiene el tipo de usuario.
"""

def estadisticasPorTipoDeUsuario(asociarVehiculoConPiso):
    keys = asociarVehiculoConPiso.keys()
    # Variable que ejercerá de contador de la cantidad de usuarios de cada tipo.
    cantidadDeVehiculos = [0, 0, 0, 0]
    for x in keys:
        if asociarVehiculoConPiso[x][3] == "Profesor":
            cantidadDeVehiculos[0] += 1
        elif asociarVehiculoConPiso[x][3] == "Estudiante":
            cantidadDeVehiculos[1] += 1
        elif asociarVehiculoConPiso[x][3] == "Personal Administrativo":
            cantidadDeVehiculos[2] += 1
        elif asociarVehiculoConPiso[x][3] == "Visitante":
            cantidadDeVehiculos[3] += 1

    archivoTexto = open("estadisticasTiposDeUsuarios.txt", "w")
    archivoTexto.write("Profesor " + str(cantidadDeVehiculos[0]) + "\n")
    archivoTexto.write("Estudiante " + str(cantidadDeVehiculos[1]) + "\n")
    archivoTexto.write("Personal administrativo " + str(cantidadDeVehiculos[2])+ "\n")
    archivoTexto.write("Visitante " + str(cantidadDeVehiculos[3]) + "\n")
    archivoTexto.close()
    return

""" Función: estadisticasPorTipoDeVehiculo
Objetivo:
    Función que se encarga registrar en un archivo de texto la cantidad de vehículos que hay por tipo de vehículo.
Entrada:
    Diccionario: que contiene el tipo de vehículo.
"""

def estadisticasPorTipoDeVehiculo(asociarVehiculoConPiso):
    keys = asociarVehiculoConPiso.keys()
    cantidadDeVehiculos = [0, 0, 0, 0]
    # Variable que ejercerá de contador de la cantidad de vehículos de cada tipo.
    for x in keys:
        if asociarVehiculoConPiso[x][4] == "Automóvil":
            cantidadDeVehiculos[0] += 1
        elif asociarVehiculoConPiso[x][4] == "Automóvil Eléctrico":
            cantidadDeVehiculos[1] += 1
        elif asociarVehiculoConPiso[x][4] == "Motocicleta":
            cantidadDeVehiculos[2] += 1
        elif asociarVehiculoConPiso[x][4] == "Discapacitado":
            cantidadDeVehiculos[3] += 1

    archivoTexto = open("estadisticasTiposDeVehiculo.txt", "w", encoding="utf-8")
    archivoTexto.write("Hay un total de " + str(cantidadDeVehiculos[0]) + " Automóviles parqueados\n")
    archivoTexto.write("Hay un total de " + str(cantidadDeVehiculos[1]) + " Automóviles Eléctricos parqueados\n")
    archivoTexto.write("Hay un total de " + str(cantidadDeVehiculos[2]) + " Motocicletas parqueados\n")
    archivoTexto.write("Hay un total de " + str(cantidadDeVehiculos[3]) + " vehículos de personas discapactidas parqueados")
    archivoTexto.close()
    return 

menu()