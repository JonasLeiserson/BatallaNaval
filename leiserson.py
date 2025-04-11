import random

grupoM = 0
grupoG = 0
Errores = 0
aciertos = 0
N = 5
CantidadDeDisparos = 10
CantidadDeBarcos = 2
tablero = [["~" for _ in range(N)] for _ in range(N)]
barcos_ids = [[None] * N for _ in range(N)]

def PosicionesBarcos(TamañoBarco, numero_barco, primer_pedazo, ultima_fila=None, ultima_columna=None):
    while True: 
        try:
            global direccion
            if primer_pedazo:
                fila = int(input(f"Ingresar la FILA del barco número {numero_barco} (entre 0 y {N - 1}): "))
                columna = int(input(f"Ingresar la COLUMNA del barco número {numero_barco} (entre 0 y {N - 1}): "))
            else:
                posiciones_validas = []
                adyacentes = [
                    (ultima_fila - 1, ultima_columna),
                    (ultima_fila + 1, ultima_columna),
                    (ultima_fila, ultima_columna - 1),
                    (ultima_fila, ultima_columna + 1)
                ]

                if direccion == "Horizontal":
                    adyacentes = [
                        (f, c) for f, c in adyacentes 
                        if f == ultima_fila 
                    ]
                elif direccion == "Vertical":
                   
                    adyacentes = [
                        (f, c) for f, c in adyacentes 
                        if c == ultima_columna  
                    ]
                else:
                    pass
                for f, c in adyacentes:
                    if 0 <= f < N and 0 <= c < N and tablero[f][c] == "~":
                        posiciones_validas.append((f, c))

                if not posiciones_validas:
                    print("No hay posiciones válidas adyacentes libres. Intenta de nuevo.")
                    return PosicionesBarcos(TamañoBarco, numero_barco, True)

                print("Elegí una de las siguientes posiciones válidas:")
                for i, (f, c) in enumerate(posiciones_validas):
                    print(f"{i}: Fila {f}, Columna {c}")

                eleccion = int(input("Elegí el número de la opción: "))
                fila, columna = posiciones_validas[eleccion]

                if not primer_pedazo:
                    if fila == ultima_fila:
                        direccion = "Horizontal"
                    elif columna == ultima_columna:
                        direccion = "Vertical"

            if fila < 0 or fila >= N or columna < 0 or columna >= N:
                print("Fuera de rango")
                continue

            if tablero[fila][columna] != "~": 
                print("Casilla ocupada")
                continue

            match TamañoBarco:
                case 1:
                    tablero[fila][columna] = "🚤"
                case 2:
                    tablero[fila][columna] = "🛳"
                    barcos_ids[fila][columna] = "M" + str(grupoM)
                    print(barcos_ids)
                case 3:
                    tablero[fila][columna] = "🚢"
                    barcos_ids[fila][columna] = "G" + str(grupoG)
                    print(barcos_ids)

            for fila_tablero in tablero:
                print(fila_tablero)

            break

        except ValueError:
            print("Ingresar posicion valida")

    return fila, columna


for i in range(CantidadDeBarcos):
    while True: 
        try:    
            direccion = ""
            TamañoBarco = input("Ingrese C para barco corto (1 casilla), M para medio (2 casillas), G para grande (3 casillas): ").upper()

            if TamañoBarco == "C":
                PosicionesBarcos(1, i + 1, True)
                break
            elif TamañoBarco == "M":
                grupoM += 1
                fila, columna = PosicionesBarcos(2, i + 1, True)
                for j in range(1):
                    fila, columna = PosicionesBarcos(2, i + 1, False, fila, columna)
                break
            elif TamañoBarco == "G":
                grupoG += 1
                fila, columna = PosicionesBarcos(3, i + 1, True)
                for j in range(2):
                    fila, columna = PosicionesBarcos(3, i + 1, False, fila, columna)
                break
            else:
                print("Letra inválida")
        except ValueError:
            print("Ingresar Letras validas")


while CantidadDeDisparos > 0: 
    DisparoEjeX = int(input("Ingersar cordenadas de disparo eje x entre 0 y " + str(N-1)))
    DisparoEjeY = int(input("Ingersar cordenadas de disparo eje y entre 0 y " + str(N-1)))

    if tablero[DisparoEjeX][DisparoEjeY] == "~":
        print("AGUA")
        Errores += 1
        CantidadDeDisparos -= 1
        tablero[DisparoEjeX][DisparoEjeY] = "💧"
        print(" Te quedan " + str(CantidadDeDisparos) + "  disparos")

        for fila in tablero:
            print(fila)

    elif tablero[DisparoEjeX][DisparoEjeY] == "🚤": 
        print("Hundido 💥")
        aciertos += 1
        CantidadDeBarcos -= 1
        tablero[DisparoEjeX][DisparoEjeY] = "💥"

    elif tablero[DisparoEjeX][DisparoEjeY] == "🛳":
        
        IDBARCO = barcos_ids[DisparoEjeX][DisparoEjeY]
        
        barcos_ids[DisparoEjeX][DisparoEjeY] = None
        
        for i in range(N):
            for j in range(N):
                if barcos_ids[i][j] == IDBARCO:
                    QUEDANBARCOSDEESTEGRUPO = True

                if  QUEDANBARCOSDEESTEGRUPO == True:
                    print("Tocado 💥")
                    
                else:
                    print("Hundido 💥")
                    CantidadDeBarcos -= 1
                    
                QUEDANBARCOSDEESTEGRUPO = False
                    
        aciertos += 1
        CantidadDeDisparos -= 1
        tablero[DisparoEjeX][DisparoEjeY] = "💥"

        for fila in tablero:
            print(fila)
    else: 
        IDBARCO = barcos_ids[DisparoEjeX][DisparoEjeY]
        
        barcos_ids[DisparoEjeX][DisparoEjeY] = None
        
        for i in range(N):
            for j in range(N):
                if barcos_ids[i][j] == IDBARCO:
                    QUEDANBARCOSDEESTEGRUPO = True

                    if  QUEDANBARCOSDEESTEGRUPO == True:
                        print("Tocado 💥")
                    
                    else:
                        print("Hundido 💥")
                        CantidadDeBarcos -= 1
                    
                    QUEDANBARCOSDEESTEGRUPO = False
                    
        aciertos += 1
        CantidadDeDisparos -= 1
        tablero[DisparoEjeX][DisparoEjeY] = "💥"

        for fila in tablero:
            print(fila)
    
    if CantidadDeBarcos == 0: 
        print("No quedan más barcos, ganaste. \n" +
              "Tuviste " + str(aciertos) + " aciertos \n" +
              "Tuviste " + str(Errores) + " Errores")
        break

print("No te quedan más disparos, perdiste. \n" +
    "Tuviste " + str(aciertos) + " aciertos \n" +
    "Tuviste " + str(Errores) + " Errores")
for fila in tablero:
    print(fila)