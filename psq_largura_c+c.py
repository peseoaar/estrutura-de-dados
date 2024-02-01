from collections import deque

grafo = {
    "A":["B", "C"],
    "B":["C"],
    "C":["D", "E"],
    "D":["C", "E"],
    "E":["C", "D"]
}

def busca_em_largura(grafo, vertice_inicial, vertice_final):
    fila = deque()
    fila.append(vertice_inicial)
    predecessores = {vertice: None for vertice in grafo}
    visitados = set()

    while fila:
        vertice_atual = fila.popleft()
        visitados.add(vertice_atual)

        if vertice_atual == vertice_final:
            break
        
        for i in grafo[vertice_atual]:
            if i not in visitados:
                fila.append(i)
                visitados.add(i)
                predecessores[i] = vertice_atual


    caminho = []
    while vertice_final is not None:
        caminho.append(vertice_final)
        vertice_final = predecessores[vertice_final]
    caminho.reverse()

    return caminho

caminho_mais_curto = busca_em_largura(grafo, "A", "E")
print("Caminho mais curto:", caminho_mais_curto)