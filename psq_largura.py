## Pesquisa em Largura

from collections import deque 

grafo = {}
grafo["acordar"] = ["praticar_exercicio", "escovar_dentes", "embrulhar_lanche"]
grafo["embrulhar_lanche"] = []
grafo["escovar_dentes"] = ["tomar_cafe"]
grafo["tomar_cafe"] = []
grafo["praticar_exercicio"] = ["tomar_banho", "trocar_roupa"]
grafo["tomar_banho"] = []
grafo["trocar_roupa"] = []
fila_pesquisa = deque()
fila_pesquisa+=grafo["acordar"]
count=0

while fila_pesquisa:
    acao = fila_pesquisa.popleft()
    if acao == "trocar_roupa":
        print("Fim")
        print(count,"passos")
    else:
        if grafo[acao]:
            fila_pesquisa += grafo[acao]
        
        count+=1
