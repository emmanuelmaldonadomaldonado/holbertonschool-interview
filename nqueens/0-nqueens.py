#!/usr/bin/python3
"""
0. N queens
"""
import sys


def backtracking(board, row=0, column=0):
    """
    method that uses the backtracking algorithm to obtain
    all possible solutions
    """
    # si llegamos a la ultima fila se imprime el resultado
    if row == len(board):
        print_result(board)
        # luego continua buscando mas soluciones
        return

    if row == 0:
        # si es la primera fila, no hay necesidad de comprobar
        for column in range(len(board)):
            board[row][column] = 1
            backtracking(board, row + 1, 0)
            board[row][column] = 0

    else:
        for column in range(len(board)):
            # a partir de la segunda fila se comprueba si se puede colocar
            if comprobation(board, row, column):
                board[row][column] = 1
                backtracking(board, row + 1, 0)
                board[row][column] = 0


def comprobation(board, row, column):
    """
    method that checks if the queen is being attacked,
    vertically or diagonally on both sides
    """
    # comprobacion de arriba hacia abajo verticalmente
    for row_2 in range(len(board)):
        if board[row_2][column] == 1:
            return False

    row_2 = row
    column_2 = column
    # comprobacion por si la posicion es el extremo izquierda
    if row != len(board) - 1 or column != 0:
        # ubicando el extremo inicial de la diagonal mediante su ubicacion
        while row_2 > 0 and column_2 > 0:
            row_2 -= 1
            column_2 -= 1

        # comprobacion de diagonal de izquierda a derecha
        while row_2 < len(board) and column_2 < len(board):
            if board[row_2][column_2] == 1:
                return False
            row_2 += 1
            column_2 += 1

    row_2 = row
    column_2 = column
    # comprobacion por si la posicion es el extremo derecha
    if row != len(board) - 1 or column != len(board) - 1:
        # ubicando el extremo inicial de la diagonal mediante su ubicacion
        while row_2 > 0 and column_2 < len(board) - 1:
            row_2 -= 1
            column_2 += 1

        # comprobacion de diagonal de derecha a izquierda
        while row_2 < len(board) and column_2 >= 0:
            if board[row_2][column_2] == 1:
                return False
            row_2 += 1
            column_2 -= 1

    # si pasa todas las pruebas entonces retornamos True
    return True


def print_result(board):
    """
    Method that prints the location of the queen
    through its row and column
    """
    result = []
    for row in board:
        result.append([board.index(row), row.index(1)])

    print(result)


def validate_integer(number):
    """

    """
    try:
        # Intentamos convertir el argumento a entero
        number = int(number)
        # Si la conversión fue exitosa, retornamos el número
        return number
    except ValueError:
        # Si la conversión falló, significa que el argumento no es un entero
        # Entonces retornamos 1
        return 1
    except TypeError:
        # Si ocurre un TypeError, significa que el argumento es None
        # Entonces también retornamos 1
        return 1


# Obtenemos el número de argumentos y los argumentos
argc = len(sys.argv)
argv = sys.argv

# Verificamos si se han proporcionado dos argumentos
if argc != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Verificamos si el argumento N es un entero
n = validate_integer(argv[1])

if n == 1:
    print("N must be a number")
    sys.exit(1)

# Verificamos si N es mayor o igual a 4
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Si llegamos aquí, significa que los argumentos son válidos
# Podemos continuar con el programa...

board = []
row = []

for i in range(n):
    for j in range(n):
        row.append(0)
    board.append(row)
    row = []

backtracking(board)
