import random

Errores = 0
aciertos = 0
N = 5
CantidadDeDisparos = 10
CantidadDeBarcos = 2

#PosicionEnemigoFila =  random.randint(0, N-1)
#PosicionEnemigoColumna = random.randint(0, N-1)
N = 5  # Por ejemplo, un tablero de 5x5
CantidadDeBarcos = 2  # Cambialo según lo que necesites

tablero = [["~" for _ in range(N)] for _ in range(N)]

def PosicionesBarcos():
    fila = int(input("Ingresar la FILA del barco número " + str(i + 1) + " (entre 0 y " + str(N - 1) + "): "))
    columna = int(input("Ingresar la COLUMNA del barco número " + str(i + 1) + " (entre 0 y " + str(N - 1) + "): "))
    tablero[fila][columna] = "🚢"

for i in range(CantidadDeBarcos):
    TamañoBarco = input("Ingrese CHICO si quiere un barco de una casilla, MEDIANO si quiere de 2 casillas o GRANDE si quiere un barco de 3 casillas: ").upper()

    if TamañoBarco == "CHICO":
        PosicionesBarcos()
    elif TamañoBarco == "MEDIANO":
        PosicionesBarcos()
    else:
        PosicionesBarcos()

print("\nTablero Final:")
for fila in tablero:
    print(" ".join(fila))


while CantidadDeDisparos > 0: 
    DisparoEjeX = int(input("Ingersar cordenadas de disparo eje x entre 0 y " + str(N-1)))
    DisparoEjeY = int(input("Ingersar cordenadas de disparo eje y entre 0 y " + str(N-1)))

    if tablero[DisparoEjeX][DisparoEjeY] == "~":
        print("AGUA")
        Errores =+ 1
        CantidadDeDisparos -= 1
        tablero[DisparoEjeX][DisparoEjeY] = "💧"
        print(" Te quedan " + str(CantidadDeDisparos) + "  disparos")
        
        for fila in  tablero:
            print(fila)
    else: 
        print("Golpeado 💥")
        aciertos =+ 1
        CantidadDeBarcos -= 1
        tablero[DisparoEjeX][DisparoEjeY] = "💥"
        for fila in  tablero:
                print(fila)

        if CantidadDeBarcos == 0: 
            print("No quedan mas barcos, ganaste. \n" + 
                  "Tuviste " + str(aciertos) + " aciertos \n" 
                  +  "Tuviste " + str(Errores) + " Errores"
                 )
            break

print("No te quedan mas disparos, perdiste. \n" + 
    "Tuviste " + str(aciertos) + " aciertos \n" +
    "Tuviste " + str(Errores) + " Errores"
    )