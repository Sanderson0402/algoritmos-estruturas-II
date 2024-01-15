class NoArvore:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if no is None:
            return NoArvore(chave)
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._inserir(no.direita, chave)
        return no

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        if no is None:
            return no
        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            no.chave = self._menor_valor(no.direita)
            no.direita = self._remover(no.direita, no.chave)
        return no

    def _menor_valor(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no.chave

    def buscar_maior(self):
        no_atual = self.raiz
        while no_atual.direita is not None:
            no_atual = no_atual.direita
        return no_atual.chave

    def distancia_do_maior(self):
        maior = self.buscar_maior()
        return self._distancia_do_maior(self.raiz, maior)

    def _distancia_do_maior(self, no, chave_maior, distancia=0):
        if no is None:
            return -1
        if no.chave == chave_maior:
            return distancia
        elif chave_maior < no.chave:
            return self._distancia_do_maior(no.esquerda, chave_maior, distancia + 1)
        else:
            return self._distancia_do_maior(no.direita, chave_maior, distancia + 1)

# Exemplo de uso
arvore = ArvoreBinaria()

# Inserção de 10 elementos
elementos = [50, 30, 70, 20, 40, 60, 80, 10, 25, 45]
for elemento in elementos:
    arvore.inserir(elemento)

# Remoção de um elemento
arvore.remover(40)

# Busca do maior elemento e distância
maior_elemento = arvore.buscar_maior()
distancia = arvore.distancia_do_maior()

print(f'Maior elemento na árvore: {maior_elemento}')
print(f'Distância da raiz da árvore até o maior elemento: {distancia}')
