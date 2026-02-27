from typing import List, Union

Matrix = List[List[Union[int, float, complex]]]
Row = List[Union[int, float, complex]]

def check_matrix(matrix: Matrix) -> bool:
    if len(matrix) < 1:
        return False
    if len(matrix[0]) < 1:
        return False
    if not all(len(row) == len(matrix[0]) for row in matrix):
        return False
    return True

def find_pivot(row: Row, start_col: int = 0) -> int | None:
    for i in range(start_col, len(row)):
        # Para números complejos, comparamos con 0 usando absoluto
        if isinstance(row[i], complex):
            if abs(row[i]) > 1e-10:  # Tolerancia para números complejos
                return i
        elif abs(row[i]) > 1e-10:  # Tolerancia para números reales
            return i
    return None

def normalize_pivot_row(matrix: Matrix, row_idx: int, col_idx: int) -> None:
    """Normaliza la fila del pivote para que el pivote sea 1"""
    pivot = matrix[row_idx][col_idx]
    if abs(pivot) < 1e-10:
        return
    
    # Dividir toda la fila por el valor del pivote
    for j in range(len(matrix[row_idx])):
        matrix[row_idx][j] = matrix[row_idx][j] / pivot

def eliminate_column(matrix: Matrix, pivot_row: int, pivot_col: int, eliminate_all: bool = True) -> None:
    """Elimina elementos en la columna del pivote"""
    pivot_value = matrix[pivot_row][pivot_col]
    if abs(pivot_value) < 1e-10:
        return
    
    rows = len(matrix)
    
    for i in range(rows):
        if eliminate_all:
            # Eliminar en todas las filas excepto la del pivote
            if i == pivot_row:
                continue
        else:
            # Solo eliminar debajo del pivote (para escalonada simple)
            if i <= pivot_row:
                continue
        
        factor = matrix[i][pivot_col] / pivot_value
        if abs(factor) < 1e-10:
            continue
            
        # Restar múltiplo de la fila del pivote
        for j in range(pivot_col, len(matrix[i])):
            matrix[i][j] = matrix[i][j] - factor * matrix[pivot_row][j]

def swap_rows(matrix: Matrix, row1: int, row2: int) -> None:
    """Intercambia dos filas"""
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def find_pivot_in_column(matrix: Matrix, col: int, start_row: int) -> int | None:
    """Encuentra el primer elemento no nulo en una columna a partir de una fila dada"""
    rows = len(matrix)
    for i in range(start_row, rows):
        if isinstance(matrix[i][col], complex):
            if abs(matrix[i][col]) > 1e-10:
                return i
        elif abs(matrix[i][col]) > 1e-10:
            return i
    return None

def reduced_row_echelon(matrix: Matrix) -> None:
    """Convierte la matriz a su forma escalonada reducida por filas (RREF)"""
    if not check_matrix(matrix):
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    pivot_row = 0
    pivot_col = 0
    
    # Fase 1: Forma escalonada por filas con pivotes normalizados a 1
    while pivot_row < rows and pivot_col < cols:
        # Encontrar pivote en esta columna
        pivot_idx = find_pivot_in_column(matrix, pivot_col, pivot_row)
        
        if pivot_idx is None:
            # No hay pivote en esta columna, pasar a la siguiente columna
            pivot_col += 1
            continue
        
        # Si el pivote no está en la fila actual, intercambiar
        if pivot_idx != pivot_row:
            swap_rows(matrix, pivot_row, pivot_idx)
        
        # Normalizar la fila del pivote (hacer pivote = 1)
        normalize_pivot_row(matrix, pivot_row, pivot_col)
        
        # Eliminar elementos debajo del pivote
        eliminate_column(matrix, pivot_row, pivot_col, eliminate_all=False)
        
        pivot_row += 1
        pivot_col += 1
    
    # Fase 2: Forma escalonada reducida (hacer ceros arriba de los pivotes)
    
    # Primero, identificar las posiciones de los pivotes
    pivot_positions = []
    pivot_row = 0
    pivot_col = 0
    
    while pivot_row < rows and pivot_col < cols:
        if pivot_row < rows and pivot_col < cols and abs(matrix[pivot_row][pivot_col]) > 1e-10:
            pivot_positions.append((pivot_row, pivot_col))
            pivot_row += 1
        pivot_col += 1
    
    # Ahora, para cada pivote (empezando desde el último), hacer ceros arriba
    for i in range(len(pivot_positions) - 1, -1, -1):
        pivot_row, pivot_col = pivot_positions[i]
        
        # Asegurarse de que el pivote es 1 (por si acaso)
        if abs(matrix[pivot_row][pivot_col]) > 1e-10:
            normalize_pivot_row(matrix, pivot_row, pivot_col)
        
        # Eliminar elementos encima del pivote
        for row_above in range(pivot_row):
            factor = matrix[row_above][pivot_col]
            if abs(factor) > 1e-10:
                for col in range(pivot_col, cols):
                    matrix[row_above][col] = matrix[row_above][col] - factor * matrix[pivot_row][col]
    
    # Asegurar que las filas nulas estén al final
    for i in range(rows):
        if all(abs(x) < 1e-10 for x in matrix[i]):
            for j in range(i + 1, rows):
                if not all(abs(x) < 1e-10 for x in matrix[j]):
                    swap_rows(matrix, i, j)

def row_echelon(matrix: Matrix) -> None:
    """Convierte la matriz a su forma escalonada por filas (no reducida)"""
    if not check_matrix(matrix):
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    pivot_row = 0
    pivot_col = 0
    
    while pivot_row < rows and pivot_col < cols:
        # Encontrar pivote en esta columna
        pivot_idx = find_pivot_in_column(matrix, pivot_col, pivot_row)
        
        if pivot_idx is None:
            # No hay pivote en esta columna, pasar a la siguiente columna
            pivot_col += 1
            continue
        
        # Si el pivote no está en la fila actual, intercambiar
        if pivot_idx != pivot_row:
            swap_rows(matrix, pivot_row, pivot_idx)
        
        # Normalizar la fila del pivote (hacer pivote = 1)
        normalize_pivot_row(matrix, pivot_row, pivot_col)
        
        # Eliminar elementos debajo del pivote
        eliminate_column(matrix, pivot_row, pivot_col, eliminate_all=False)
        
        pivot_row += 1
        pivot_col += 1
    
    # Asegurar que las filas nulas estén al final
    for i in range(rows):
        if all(abs(x) < 1e-10 for x in matrix[i]):
            for j in range(i + 1, rows):
                if not all(abs(x) < 1e-10 for x in matrix[j]):
                    swap_rows(matrix, i, j)

if __name__ == "__main__":
    # Ejemplo 1: Matriz con números complejos
    matrix1 = [
        [complex(0, 1), 1, complex(0, 2)],
        [2, complex(0, -1), 4],
        [complex(0, -1), 1, complex(0, -1)]
    ]
    
    print("Matriz original 1:")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    reduced_row_echelon(matrix1)
    
    print("\nMatriz en forma escalonada REDUCIDA por filas (RREF):")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    print("\n" + "="*50 + "\n")

    matrix1 = [
    [1, -2, 3, 0],
    [2, -1, 2, 0],
    [3,  1, 2, 0]
    ]
    
    print("Matriz original 1:")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    reduced_row_echelon(matrix1)
    
    print("\nMatriz en forma escalonada REDUCIDA por filas (RREF):")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    print("\n" + "="*50 + "\n")

    matrix1 = [
    [1 , 3 ,  2 ,  3 , -7 , 14],
    [2 , 6 ,  1 , -2 ,  5 , -2],
    [1 , 3 , -1 ,  0 ,  2 , -1]
    ]
    
    print("Matriz original 1:")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    reduced_row_echelon(matrix1)
    
    print("\nMatriz en forma escalonada REDUCIDA por filas (RREF):")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    print("\n" + "="*50 + "\n")

    matrix1 = [
        [1, 1,  1, 4],
        [2, 5, -2, 3],
        [1, 7, -7, 5]
    ]
    
    print("Matriz original 1:")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    reduced_row_echelon(matrix1)
    
    print("\nMatriz en forma escalonada REDUCIDA por filas (RREF):")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    print("\n" + "="*50 + "\n")

    matrix1 = [
        [-5, 3, 1, 4, 11],
        [0, -1, 2, 4, -2],
        [4, -1, -3, -7, -6]
    ]
    
    print("Matriz original 1:")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    reduced_row_echelon(matrix1)
    
    print("\nMatriz en forma escalonada REDUCIDA por filas (RREF):")
    for row in matrix1:
        print([f"{x}" if isinstance(x, (float, complex)) else str(x) for x in row])
    
    print("\n" + "="*50 + "\n")
