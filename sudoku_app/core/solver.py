def buscar_vacia(tablero):
    """
    Busca la siguiente celda vacía (representada por cadena vacía "").
    Retorna (fila, columna) o None si no hay vacías.
    """
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == "":
                return (fila, col)
    return None

def es_valido(tablero, fila, col, emoji):
    """
    Comprueba si colocar 'emoji' en tablero[fila][col] es válido.
    Revisa fila, columna y subcuadrícula 3x3.
    """
    # Revisar fila
    for c in range(9):
        if tablero[fila][c] == emoji:
            return False

    # Revisar columna
    for r in range(9):
        if tablero[r][col] == emoji:
            return False

    # Revisar subcuadrícula 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for r in range(inicio_fila, inicio_fila + 3):
        for c in range(inicio_col, inicio_col + 3):
            if tablero[r][c] == emoji:
                return False

    return True

def resolver(tablero, emojis):
    """
    Resuelve el Sudoku con backtracking.
    'tablero' es una lista de listas 9x9 con emojis o "".
    'emojis' es la lista de emojis válidos que se pueden usar.
    Devuelve True si se resolvió, False si no.
    """
    vacio = buscar_vacia(tablero)
    if not vacio:
        return True  # No hay vacíos, sudoku resuelto

    fila, col = vacio

    for emoji in emojis:
        if es_valido(tablero, fila, col, emoji):
            tablero[fila][col] = emoji
            if resolver(tablero, emojis):
                return True
            tablero[fila][col] = ""  # Backtrack

    return False

def es_tablero_valido(tablero):
    def sin_repetidos(lista):
        elementos = [x for x in lista if x != ""]
        return len(set(elementos)) == len(elementos)

    # Verifica filas
    for fila in tablero:
        if not sin_repetidos(fila):
            return False

    # Verifica columnas
    for col in range(9):
        columna = [tablero[fila][col] for fila in range(9)]
        if not sin_repetidos(columna):
            return False

    # Verifica subcuadrantes 3x3
    for box_row in range(3):
        for box_col in range(3):
            celdas = []
            for i in range(3):
                for j in range(3):
                    celdas.append(tablero[box_row*3 + i][box_col*3 + j])
            if not sin_repetidos(celdas):
                return False

    return True