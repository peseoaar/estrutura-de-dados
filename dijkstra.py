# grafo de conexoes no grafo
grafo = {}

grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

# custos do grafo
infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# tabela de predecessores
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

#codigo 

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    noh_custo_mais_baixo = None
    for noh in custos:
        custo = custos[noh]
        if custo < custo_mais_baixo and noh not in processados:
            custo_mais_baixo = custo
            noh_custo_mais_baixo = noh
    return noh_custo_mais_baixo 

noh = ache_no_custo_mais_baixo(custos)

while noh is not None:
    custo = custos[noh]
    vizinhos = grafo[noh]

    for n in vizinhos:
        novo_custo = custo + vizinhos[n]
        if novo_custo < custos[n]:
           custos[n] = novo_custo
           pais[n] = noh

    processados.append(noh)
    noh = ache_no_custo_mais_baixo(custos)  

print(custos)
