# Para resolver o problema da mochila, a função principal inicializa uma matriz dp para armazenar os resultados intermediários e chama a função solve_n_queens_util(board, col, n) para preencher essa matriz. 
# Depois de preencher a matriz, ela recupera os itens incluídos na mochila e retorna o valor máximo que pode ser carregado na mochila e os itens incluídos.

def mochila_max_valor(pesos, valores, capacidade):
    n = len(pesos)
    
    # Inicializa uma matriz para armazenar os resultados intermediários
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenche a matriz usando a abordagem de programação dinâmica
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Recupera os itens incluídos na mochila
    itens_incluidos = []
    i, w = n, capacidade
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            itens_incluidos.append(i - 1)
            w -= pesos[i - 1]
        i -= 1

    return dp[n][capacidade], itens_incluidos[::-1]

# Exemplo de uso
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5

max_valor, itens_incluidos = mochila_max_valor(pesos, valores, capacidade)

print("Valor máximo que pode ser carregado na mochila:", max_valor)
print("Itens incluídos na mochila:", itens_incluidos)
