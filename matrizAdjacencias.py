# Representacao computacional de um grafo por meio de matriz de adjacencias:
class MatrizAdjacencias:
    #inicializa o grafo:    
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.numArestas = 0
        # inicializa a matriz de adjacencias com todos elementos iguais a zero:
        self.matriz = [[0]*numVertices for _ in range(numVertices)]
        # inicializa o vetor que armazena o grau dos vertices:
        self.graus = [0] * self.numVertices

    # retorna a ordem do grafo:
    def ordem(self):
        return self.numVertices
    
    # retorna o tamanho do grafo:
    def tamanho(self):
        return self.numArestas

    # adiciona uma aresta (v1, v2) no grafo:
    # peso eh um parametro opcional
    def addAresta(self, v1, v2, peso = 1):
        if self.matriz[v1][v2] == 0: # se a aresta nao existe no grafo
            self.numArestas += 1 # incrementa o numero de arestas do grafo
            self.graus[v1] += 1 # incrementa o grau do vertice
        self.matriz[v1][v2] = peso # adiciona a aresta
    
    # retorna True se existe uma aresta (v1,v2) no grafo:
    def possuiAresta(self, v1, v2):
        return (self.matriz[v1][v2] != 0)

    # retorna uma lista com os vizinhos de v:
    def vizinhos(self, v):
        return [i for i in range(self.numVertices) if self.matriz[v][i] != 0]
    
    # retorna o grau de um vertice:
    def grau(self, v):
        return self.graus[v]

    # printa o grafo no formato de matriz de adjacencias:
    def printGrafo(self):
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                print("{} ".format(self.matriz[i][j]), end='')
            print()