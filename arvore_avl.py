class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.altura = 1
        self.esquerda = None
        self.direita = None

class ArvoreAVL:
    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        # Realiza a rotação
        x.direita = y
        y.esquerda = T2

        # Atualiza alturas
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        # Realiza a rotação
        y.esquerda = x
        x.direita = T2

        # Atualiza alturas
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    def inserir(self, raiz, chave):
        if raiz is None:
            return NoAVL(chave)
        
        if chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.inserir(raiz.direita, chave)
        else:
            return raiz  # Chaves iguais não são permitidas

        # Atualiza a altura do nó atual
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        # Obtém o fator de balanceamento para verificar se é necessário reequilibrar
        balanceamento = self.fator_balanceamento(raiz)

        # Caso de rotação à esquerda
        if balanceamento > 1 and chave < raiz.esquerda.chave:
            return self.rotacao_direita(raiz)

        # Caso de rotação à direita
        if balanceamento < -1 and chave > raiz.direita.chave:
            return self.rotacao_esquerda(raiz)

        # Caso de rotação à esquerda-direita
        if balanceamento > 1 and chave > raiz.esquerda.chave:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Caso de rotação à direita-esquerda
        if balanceamento < -1 and chave < raiz.direita.chave:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def inserir_chave(self, chave):
        self.raiz = self.inserir(self.raiz, chave)

    def imprimir_em_ordem(self, raiz):
        if raiz:
            self.imprimir_em_ordem(raiz.esquerda)
            print(raiz.chave, end=" ")
            self.imprimir_em_ordem(raiz.direita)

# Exemplo de uso
arvore_avl = ArvoreAVL()

# Inserindo chaves
chaves = [10, 20, 30, 40, 50, 25]
for chave in chaves:
    arvore_avl.inserir_chave(chave)

# Imprimindo a árvore em ordem
print("Árvore AVL em ordem:")
arvore_avl.imprimir_em_ordem(arvore_avl.raiz)
