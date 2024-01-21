# O objetivo é posicionar N rainhas em um tabuleiro NxN de tal forma que nenhuma rainha ameace outra. 
# Se em algum ponto se tornar impossível continuar sem violar as restrições (nenhuma rainha pode atacar outra), o algoritmo retrocede (backtrack) para tentar uma abordagem diferente.

def is_safe(board, row, col, n):
    # Verifica se é seguro colocar uma rainha na posição (row, col)
    
    # Verifica a linha horizontal à esquerda
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Verifica a diagonal superior à esquerda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Verifica a diagonal inferior à esquerda
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, n):
    # Função utilitária para resolver o problema das N rainhas usando backtracking
    
    if col == n:
        # Todas as rainhas foram colocadas com sucesso
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            # Se for seguro colocar uma rainha na posição (i, col), faça isso
            board[i][col] = 1

            # Chama recursivamente para a próxima coluna
            if solve_n_queens_util(board, col + 1, n):
                return True

            # Se a posição não levar a uma solução, desfaz a escolha
            board[i][col] = 0

    # Não há posições seguras nesta coluna
    return False

def solve_n_queens(n):
    # Função principal para resolver o problema das N rainhas
    
    # Inicializa o tabuleiro NxN com zeros
    board = [[0] * n for _ in range(n)]
    
    # Chama a função utilitária para resolver o problema
    if not solve_n_queens_util(board, 0, n):
        print("Não existe solução.")
        return
    
    # Imprime o tabuleiro com as rainhas colocadas
    for i in range(n):
        print(board[i])

# Exemplo de uso para o problema das 8 rainhas
solve_n_queens(8)
