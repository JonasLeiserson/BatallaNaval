import random

Errores = 0
aciertos = 0
N = 5
CantidadDeDisparos = 10
CantidadDeBarcos = 5 

PosicionEnemigoFila =  random.randint(0, N-1)
PosicionEnemigoColumna = random.randint(0, N-1)


print(PosicionEnemigoFila ,PosicionEnemigoColumna)

tablero = [["~" for _ in range(N)] for _ in range(N)]
tablero[PosicionEnemigoFila][PosicionEnemigoColumna] = "🚢"
for fila in  tablero:
    print(fila)

DisparoEjeX = int(input("Ingersar cordenadas de disparo eje x "))
DisparoEjeY = int(input("Ingersar cordenadas de disparo eje y "))

if tablero[DisparoEjeX][DisparoEjeY] == "~":
    print("AGUA")
    Errores =+ 1
    CantidadDeDisparos =- 1
    print(" Te quedan " + str(CantidadDeDisparos) + "  disparos")
else: 
    print("Hundido 💥")
    aciertos =+ 1