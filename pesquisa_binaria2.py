import numpy as np

array = np.array([n for n in range(100)])
i=0
inicio=0
fim=len(array)-1
achou=0
posicao=0

# busca binaria
numero = int(input("Digite um numero: "))

while achou==0 and fim>=inicio:
    meio = int((inicio + fim) / 2)

    if array[meio] == numero:
        posicao = array[meio]
        achou+=1
    elif numero < array[meio]:
        fim = meio - 1
    elif numero > array[meio]:
        inicio = meio + 1

if achou == 1:
    print("O numero digitado esta na posicao", posicao," do array.")
else:
    print("O numero digitado NAO se encontra no array.")


