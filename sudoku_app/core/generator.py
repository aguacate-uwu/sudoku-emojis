import random
from copy import deepcopy
from core import solver

def generar_tablero_completo(emojis):
    """
    Genera un tablero completo válido usando backtracking.
    """
    tablero = [["" for _ in range(9)] for _ in range(9)]
    emojis_shuffled = emojis[:]  # copia para desordenar

    def rellenar():
        vacio = solver.buscar_vacia(tablero)
        if not vacio:
            return True
        fila, col = vacio
        random.shuffle(emojis_shuffled)
        for emoji in emojis_shuffled:
            if solver.es_valido(tablero, fila, col, emoji):
                tablero[fila][col] = emoji
                if rellenar():
                    return True
                tablero[fila][col] = ""
        return False

    rellenar()
    return tablero

def quitar_celdas(tablero_completo, dificultad="media"):
    """
    Elimina emojis del tablero según la dificultad.
    """
    tablero = deepcopy(tablero_completo)

    if dificultad == "facil":
        celdas_a_quitar = 30
    elif dificultad == "media":
        celdas_a_quitar = 45
    elif dificultad == "dificil":
        celdas_a_quitar = 60
    else:
        celdas_a_quitar = 45

    posiciones = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(posiciones)

    quitadas = 0
    for fila, col in posiciones:
        if quitadas >= celdas_a_quitar:
            break
        tablero[fila][col] = ""
        quitadas += 1

    return tablero

def generar_sudoku(emojis, dificultad="media"):
    """
    Genera un tablero válido y parcialmente vacío.
    Devuelve: tablero_incompleto, tablero_solucion
    """
    tablero_completo = generar_tablero_completo(emojis)
    tablero_incompleto = quitar_celdas(tablero_completo, dificultad)
    return tablero_incompleto, tablero_completo