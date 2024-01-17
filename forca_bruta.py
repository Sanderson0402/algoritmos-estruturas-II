# Um exemplo clássico de força bruta é o problema do "quebra-cabeça das oito peças" (eight-puzzle), um jogo no qual o objetivo é rearranjar peças numeradas de 1 a 8 em uma grade 3x3, deixando um espaço vazio.
# Neste exemplo, a função eight_puzzle_bruteforce utiliza força bruta para encontrar uma solução para o quebra-cabeça das oito peças, gerando todas as permutações possíveis do estado inicial até encontrar o estado meta desejado.

from itertools import permutations

def is_solvable(puzzle):
    inversions = sum(
        (1 for i in range(len(puzzle)) for j in range(i + 1, len(puzzle)) if puzzle[i] > puzzle[j])
    )
    return inversions % 2 == 0

def eight_puzzle_bruteforce(initial_state, target_state):
    if not is_solvable(initial_state) or not is_solvable(target_state):
        return None  # Verifica se a configuração inicial e a meta são solucionáveis

    # Gera todas as permutações possíveis das peças
    all_permutations = permutations(initial_state)

    # Verifica cada permutação até encontrar a meta
    for permutation in all_permutations:
        if permutation == target_state:
            return list(permutation)

    return None  # Retorna None se a solução não for encontrada

# Exemplo de uso
estado_inicial = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 representa o espaço vazio
estado_meta = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solucao = eight_puzzle_bruteforce(estado_inicial, estado_meta)

if solucao:
    print(f"Solução encontrada: {solucao}")
else:
    print("Não foi possível encontrar uma solução.")
