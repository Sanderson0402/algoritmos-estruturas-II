# Essa função fibonacci utiliza programação dinâmica para calcular o n-ésimo número de Fibonacci de maneira eficiente, evitando recalculos desnecessários ao armazenar as soluções dos subproblemas no array memoization. 
# Isso resulta em uma complexidade de tempo linear em relação a n, tornando o algoritmo mais eficiente do que uma implementação recursiva simples.

def fibonacci(n):
    memoization = [None] * (n + 1)

    memoization[0] = 0
    memoization[1] = 1

    for i in range(2, n + 1):
        memoization[i] = memoization[i - 1] + memoization[i - 2]

    return memoization[n]

# Exemplo de uso
n = 6
resultado = fibonacci(n)
print(f'O {n}-ésimo número de Fibonacci é: {resultado}')
