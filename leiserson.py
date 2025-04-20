# Seteo de variables
grupoM : int = 0
grupoG :  int = 0
grupoC :  int = 0
Errores : list = [0, 0]
aciertos : list = [0, 0]
N : int = 5
CANTIDADDEDISPAROS :  int = 10
CANTIDADDEBARCOS :  int = 2

tableros = [[["~" for _ in range(N)] for _ in range(N)] for _ in range(2)]
barcos_ids = [[[None] * N for _ in range(N)] for _ in range(2)]

# Función para ingresar los barcos
def PosicionesBarcos(jugador: int, TamañoBarco: int, numero_barco: int, primer_pedazo: bool, ultima_fila: int = None, ultima_columna: int = None) -> tuple[int, int]:
    global direccion, grupoM, grupoG, grupoC
    while True:
        try:
            if primer_pedazo:
                fila = int(input(f"[Jugador {jugador+1}] Ingresar la FILA del barco número {numero_barco} (0 a {N-1}): "))
                columna = int(input(f"[Jugador {jugador+1}] Ingresar la COLUMNA del barco número {numero_barco} (0 a {N-1}): "))
            else:
                posiciones_validas : list = []
                adyacentes : list = [
                    (ultima_fila - 1, ultima_columna),
                    (ultima_fila + 1, ultima_columna),
                    (ultima_fila, ultima_columna - 1),
                    (ultima_fila, ultima_columna + 1)
                ]
                #Se modifica adjacentes en funcion de la direccion del barco
                if direccion == "Horizontal":
                    adyacentes = [(f, c) for f, c in adyacentes if f == ultima_fila]
                elif direccion == "Vertical":
                    adyacentes = [(f, c) for f, c in adyacentes if c == ultima_columna]

                #Se agregan a posiciones_validas las posiciones adjacentes dentro del tablero
                for f, c in adyacentes:
                    if 0 <= f < N and 0 <= c < N and tableros[jugador][f][c] == "~":
                        posiciones_validas.append((f, c))

                if not posiciones_validas:
                    print("No hay posiciones válidas adyacentes libres. Intenta de nuevo.")
                    return PosicionesBarcos(jugador, TamañoBarco, numero_barco, True)

                #Se le pide al jugador elegir entre las opciones validas
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
            #Si la casilla no esta dentro de los limites se vuelve a pedir que ingrese posiciones
            if fila < 0 or fila >= N or columna < 0 or columna >= N:
                print("Fuera de rango")
                continue
            #Si la casilla no es ~ significa que esta ocupada y se vuelve a pedir que ingrese posiciones
            if tableros[jugador][fila][columna] != "~":
                print("Casilla ocupada")
                continue

            match TamañoBarco:
                case 1:
                    tableros[jugador][fila][columna] = "🚤"
                    barcos_ids[jugador][fila][columna] = "C" + str(grupoC)
                case 2:
                    tableros[jugador][fila][columna] = "🛳"
                    barcos_ids[jugador][fila][columna] = "M" + str(grupoM)
                case 3:
                    tableros[jugador][fila][columna] = "🚢"
                    barcos_ids[jugador][fila][columna] = "G" + str(grupoG)

            for fila_tablero in tableros[jugador]:
                print(fila_tablero)
            #Devuelve la fila y columna ingresados
            return fila, columna

        except ValueError:
            print("Ingresar posición válida")


# Colocar barcos para cada jugador en funcion de CANTIDADDEBARCOS
for jugador in range(CANTIDADDEBARCOS):
    print(f"Jugador {jugador+1}: Posicionamiento de barcos")
    for i in range(CANTIDADDEBARCOS):
        while True:
            try:
                #Se pregunta tamaño del barcos
                direccion : str = ""
                TamañoBarco = input(f"[Jugador {jugador+1}] ingresar C para barco corto, M para medio, G para grande: ").upper()
                if TamañoBarco == "C":
                    grupoC += 1
                    PosicionesBarcos(jugador, 1, i + 1, True)
                    break
                elif TamañoBarco == "M":
                    grupoM += 1
                    fila, columna = PosicionesBarcos(jugador, 2, i + 1, True)
                    fila, columna = PosicionesBarcos(jugador, 2, i + 1, False, fila, columna)
                    break
                elif TamañoBarco == "G":
                    grupoG += 1
                    fila, columna = PosicionesBarcos(jugador, 3, i + 1, True)
                    for _ in range(2):
                        fila, columna = PosicionesBarcos(jugador, 3, i + 1, False, fila, columna)
                    break
                else:
                    print("Letra inválida")
            except ValueError:
                print("Ingresar letras válidas")



# Parte de batalla

CANTIDADDEDISPAROS_JUGADOR = [CANTIDADDEDISPAROS, CANTIDADDEDISPAROS]
CANTIDADDEBARCOS_JUGADOR = [CANTIDADDEBARCOS, CANTIDADDEBARCOS]
BARCOTOCADO : False = bool 
turno = 0
while CANTIDADDEDISPAROS_JUGADOR[0] > 0 or CANTIDADDEDISPAROS_JUGADOR[1] > 0:
    
    rival = 1 - turno
    
    if CANTIDADDEDISPAROS_JUGADOR[turno] == 0:
        turno = rival
        continue
        #Se pregunta donde disparar
    print(f"\nTurno del Jugador {turno+1}")
    DisparoEjeX = int(input("Ingresar coordenadas de disparo eje X (0 a " + str(N-1) + "): "))
    DisparoEjeY = int(input("Ingresar coordenadas de disparo eje Y (0 a " + str(N-1) + "): "))

    celda = tableros[rival][DisparoEjeX][DisparoEjeY]
    #Dependiendo del valor de celda, se cambia el valor de la posicion del dosparo
    if celda == "~":
        print("AGUA💧")
        Errores[turno] += 1
        tableros[rival][DisparoEjeX][DisparoEjeY] = "💧"

    elif celda in ("🚤", "🛳", "🚢"):
        IDBARCO = barcos_ids[rival][DisparoEjeX][DisparoEjeY]
        barcos_ids[rival][DisparoEjeX][DisparoEjeY] = None
        aciertos[turno] += 1

        # se fija si quedan partes del mismo barco
        QuedanPartesDelMismoBarco = any(IDBARCO == barcos_ids[rival][i][j] for i in range(N) for j in range(N))
        
        if QuedanPartesDelMismoBarco:
            print("Tocado 💥")
            
        else:
            print("Hundido 💥, barco de " +  tableros[rival][DisparoEjeX][DisparoEjeY])
            CANTIDADDEBARCOS_JUGADOR[rival] -= 1

        BARCOTOCADO = True
    else:
        print("Ya disparaste ahi pancho")

    CANTIDADDEDISPAROS_JUGADOR[turno] -= 1

    tableros[rival][DisparoEjeX][DisparoEjeY] = "💥"

    #Si no le quedan barcos al rival gana el jugadore del turno actual
    if CANTIDADDEBARCOS_JUGADOR[rival] == 0:
        print(f"\nJugador {turno+1} gano, no quedan mas barcos del rival en pie")
        for fila in tableros[rival]:
            print(fila)
        break
        #Si se golpeo o hundio un barco sigue el mismo jugador 
    if BARCOTOCADO == False:
        turno = 1 - turno

#Si no le quedan tiros ni al rival ni al jugador queda en empate

if CANTIDADDEDISPAROS_JUGADOR[turno] & CANTIDADDEDISPAROS_JUGADOR[rival] == 0:
    print("Empate, no le quedan disparos a nadie")
    for i in range(2):
        print(f"\nJugador {i+1}:\n  Aciertos: {aciertos[i]}\n  Errores: {Errores[i]}")

#Usado Chatgpt y claude para debugeo de errores y formas de realizar acciones