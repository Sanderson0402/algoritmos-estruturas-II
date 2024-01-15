class Grafo:
    def __init__(self):
        self.vertices = {}

    def inserir_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def inserir_aresta(self, vertice_origem, vertice_destino):
        if vertice_origem in self.vertices and vertice_destino in self.vertices:
            self.vertices[vertice_origem].append(vertice_destino)
            self.vertices[vertice_destino].append(vertice_origem)

    def remover_aresta(self, vertice_origem, vertice_destino):
        if vertice_origem in self.vertices and vertice_destino in self.vertices:
            self.vertices[vertice_origem].remove(vertice_destino)
            self.vertices[vertice_destino].remove(vertice_origem)

    def buscar_vertice(self, vertice):
        return vertice in self.vertices

    def buscar_aresta(self, vertice_origem, vertice_destino):
        return vertice_destino in self.vertices[vertice_origem]

    def obter_vizinhos(self, vertice):
        return self.vertices[vertice] if vertice in self.vertices else []

grafo = Grafo()


grafo.inserir_vertice('A')
grafo.inserir_vertice('B')
grafo.inserir_vertice('C')

grafo.inserir_aresta('A', 'B')
grafo.inserir_aresta('B', 'C')

print(grafo.buscar_vertice('A'))  # True
print(grafo.buscar_vertice('D'))  # False

print(grafo.buscar_aresta('A', 'B'))  # True
print(grafo.buscar_aresta('A', 'C'))  # False

grafo.remover_aresta('A', 'B')

print(grafo.obter_vizinhos('A'))  # ['C']
