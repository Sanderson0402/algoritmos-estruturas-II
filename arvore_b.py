class NoB:
    def __init__(self, folha=True):
        self.folha = folha
        self.chaves = []
        self.filhos = []

class ArvoreB:
    def __init__(self, grau):
        self.raiz = NoB()
        self.grau = grau

    def busca(self, no, chave):
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1

        if i < len(no.chaves) and chave == no.chaves[i]:
            return True  # Chave encontrada
        elif no.folha:
            return False  # Chave não encontrada
        else:
            return self.busca(no.filhos[i], chave)

    def insere(self, chave):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.grau) - 1:
            novo_no = NoB(folha=False)
            self.raiz = novo_no
            novo_no.filhos.append(raiz)
            self._divide_filho(novo_no, 0)
            self._insere_nao_cheio(novo_no, chave)
        else:
            self._insere_nao_cheio(raiz, chave)

    def _insere_nao_cheio(self, no, chave):
        i = len(no.chaves) - 1
        if no.folha:
            no.chaves.append(None)
            while i >= 0 and chave < no.chaves[i]:
                no.chaves[i + 1] = no.chaves[i]
                i -= 1
            no.chaves[i + 1] = chave
        else:
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            if len(no.filhos[i].chaves) == (2 * self.grau) - 1:
                self._divide_filho(no, i)
                if chave > no.chaves[i]:
                    i += 1
            self._insere_nao_cheio(no.filhos[i], chave)

    def _divide_filho(self, pai, indice_filho):
        grau = self.grau
        filho = pai.filhos[indice_filho]
        novo_filho = NoB(folha=filho.folha)
        pai.chaves.insert(indice_filho, filho.chaves[grau - 1])
        pai.filhos.insert(indice_filho + 1, novo_filho)
        novo_filho.chaves = filho.chaves[grau:]
        filho.chaves = filho.chaves[:grau - 1]

        if not filho.folha:
            novo_filho.filhos = filho.filhos[grau:]
            filho.filhos = filho.filhos[:grau]

# Exemplo de uso
arvore_b = ArvoreB(grau=2)
chaves = [3, 7, 1, 9, 2, 5, 8, 4, 6]

for chave in chaves:
    arvore_b.insere(chave)

print(arvore_b.busca(arvore_b.raiz, 5))  # Deve imprimir True
print(arvore_b.busca(arvore_b.raiz, 10))  # Deve imprimir False
