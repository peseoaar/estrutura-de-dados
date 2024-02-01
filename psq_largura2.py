from collections import deque

grafo = {}
grafo["Eu"] = ["Bob", "Claire", "Alice"]
grafo["Claire"] = ["Eu", "Thom", "Jonny"]
grafo["Alice"] = ["Eu", "Peggy"]
grafo["Bob"] = ["Anuj", "Eu", "Peggy"]
grafo["Anuj"] = ["Bob"]
grafo["Peggy"] = ["Alice", "Bob"]
grafo["Thom"] = ["Claire"]
grafo["Jonny"] = ["Claire"]



def pesquisa(nome):
    fila_pesquisa = deque() #fila
    fila_pesquisa += grafo[nome]

    pesquisada = []

    while fila_pesquisa:
        pessoa = fila_pesquisa.popleft()
        
        if pessoa not in pesquisada:
            if pessoa[-1] == "y":    # peggy e a vendedora, por isso buscar y como ultima letra
                print (pessoa, "e um(a) vendedor(a)")
                return True
            else:
                fila_pesquisa += grafo[pessoa]
                pesquisada.append(pessoa)

pesquisa("Eu")
