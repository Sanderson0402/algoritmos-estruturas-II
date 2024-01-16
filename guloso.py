# Algoritmo para resolver o problema da troca de moedas, onde o objetivo é dar o troco com o menor número de moedas possível. Este é um problema clássico que pode ser resolvido de forma eficiente usando um algoritmo guloso.

def troco_guloso(valor, moedas):
    troco = []
    moedas = sorted(moedas, reverse=True)  # Ordena as moedas em ordem decrescente
    
    for moeda in moedas:
        while valor >= moeda:
            troco.append(moeda)
            valor -= moeda
            
    return troco

# Exemplo de uso
valor_total = 63
moedas_disponiveis = [25, 10, 5, 1]

resultado = troco_guloso(valor_total, moedas_disponiveis)
print(f"Troco para {valor_total} usando moedas {moedas_disponiveis}: {resultado}")
