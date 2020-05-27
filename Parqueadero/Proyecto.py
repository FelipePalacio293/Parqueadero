import json

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

def cargaDeArchivos(tipoDeArchivo):
    if tipoDeArchivo == 1:
        with open("usuarios.json", "r", encoding="utf-8") as file:
            usuarios = json.load(file)
            return usuarios
    elif tipoDeArchivo == 2:
        with open("tiposParqueaderos.json", "r") as file:
            tipoDeParqueaderos = json.load(file)
            return tipoDeParqueaderos

def registrarVehiculo(usuarios):
    nombre = input("Ingrese el nombre de la persona: \n")
    apellido = input("Ingrese el apellido de la persona: \n")
    identificacion = eval(input("Ingrese la identificación del usuario: \n"))
    tipoDeUsuario = input("Ingrese el tipo de usuario: \n")
    placa = input("Ingrese la placa del vehículo: \n")
    tipoDeVehiculo =  input("Ingrese el tipo de vehículo: \n")
    planDePago = input("Ingrese el plan de pago: \n")
    
    size = len(usuarios["usuarios"])
    for x in range(size):
        subSize = len(usuarios["usuarios"][x])
        for y in range(subSize):
            if usuarios["usuarios"][x][y] == identificacion:
                print("Ya hay un vehículo registrado para este usuario")
                return usuarios
    
    usuarios["usuarios"].append([nombre + apellido, identificacion, tipoDeUsuario, placa, tipoDeVehiculo, planDePago]) 

    return usuarios

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

def registrarVehiculoDiario(placa, usuariosNoRegistrados):
    tipoDeVehiculo = input("Ingrese el tipo de vehiculo: \n")
    usuariosNoRegistrados["usuarios"].append([placa, tipoDeVehiculo, "Diario", "Visitante"])
    return usuariosNoRegistrados

def ubicarVehiculo(usuarios, posicion, posicionTipoUsuario, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz, placa, asociarVehiculoConPiso):
    size = len(usuarios["usuarios"])
    buscarDos = 0
    buscar = 1
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

    cantidadDePosiciones = posicionesDesocupadas(buscar, buscarDos, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz)
    
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

def cambiarEstadoAOcupado(infoPiso, placa, buscar, buscarDos, piso, asociarVehiculoConPiso, numPiso, tipoDeVehiculo, tipoDeUsuario):
    print("Las Posiciones disponibles se representan con un 0")
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
        if (infoPiso[fila][columna] == buscar or infoPiso[fila][columna] == buscarDos) and piso[fila][columna] == "0":
            piso[fila][columna] = "X"
            asociarVehiculoConPiso[placa] = [numPiso, fila, columna, tipoDeUsuario, tipoDeVehiculo]
            print("Se ha registrado su vehículo.")
            return piso, asociarVehiculoConPiso
        else:
            print("Posición ocupada o no compatible con el vehículo")

def posicionesDesocupadas(buscar, buscarDos, tipoDeParqueaderos, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz):
    cantidadDePosiciones = [0, 0, 0, 0, 0, 0]
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

def retirarVehiculo(usuarios, usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz):
    placa = input("Ingrese la placa del vehículo que se va a retirar: \n")
    if not revisarRegistro(placa, asociarVehiculoConPiso.keys()):
        print("El vehículo no se encuentra dentro del parqueadero.")
        return usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz
    horas = eval(input("Ingrese el numero de horas que permaneció el vehículo en el parqueadero: \n")) 

    if type(horas) != int:
        horas = int(horas) + 1
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

    if not registrada:
        return usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz
    
    posiciones = asociarVehiculoConPiso[placa]
    [pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz] = quitarVehiculo(posiciones, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz)

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
    asociarVehiculoConPiso.pop(placa)
    return usuariosNoRegistrados, asociarVehiculoConPiso, pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz

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

def revisarPlaca(usuarios, placa):
    size = len(usuarios["usuarios"])
    for y in range(size):
        if placa in usuarios["usuarios"][y] :
            return True, y
    return False, 0

def revisarRegistro(placa, llaves):
    if placa in llaves:
        return True
    return False

def estadisticasPorPiso(pisoUnoMatriz, pisoDosMatriz, pisoTresMatriz, pisoCuatroMatriz, pisoCincoMatriz, pisoSeisMatriz):
    cantidadDePosiciones = [0, 0, 0, 0, 0, 0]
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
    for a in range(5):
        porcentaje.append((cantidadDePosiciones[a] * 100) / 100)
    
    porcentaje.append((cantidadDePosiciones[5] * 100) / 50)
    porcentaje.append((sum(cantidadDePosiciones) * 100) / 550)

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

def estadisticasPorTipoDeUsuario(asociarVehiculoConPiso):
    keys = asociarVehiculoConPiso.keys()
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

def estadisticasPorTipoDeVehiculo(asociarVehiculoConPiso):
    keys = asociarVehiculoConPiso.keys()
    cantidadDeVehiculos = [0, 0, 0, 0]
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