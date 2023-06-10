def validar_sudoku(tabuleiro):
    for linha in tabuleiro:
        if not validar_conjunto(linha):
            return False

    for coluna in range(9):
        if not validar_conjunto([linha[coluna] for linha in tabuleiro]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            regiao = [tabuleiro[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not validar_conjunto(regiao):
                return False

    return True


def validar_conjunto(conjunto):
    numeros = [x for x in conjunto if x != "."]
    return len(set(numeros)) == len(numeros)


tabuleiro = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

for i, linha in enumerate(tabuleiro):
    for j, valor in enumerate(linha):
        if not valor.isdigit():
            continue
        tabuleiro[i][j] = int(valor)

if validar_sudoku(tabuleiro):
    print("O tabuleiro de Sudoku é válido.")
else:
    print("O tabuleiro de Sudoku contém valores incorretos.")

