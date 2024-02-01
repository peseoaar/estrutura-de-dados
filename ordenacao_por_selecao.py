# ordenacao por selecao 
import numpy as np

array= [4, 10, 14, 24, 1, 12, 2, 6, 3]
i=0


def menorValor(array):
    menor=array[0]
    indiceMenor=0
    for i in range(len(array)):
        if menor > array[i]:
            menor = array[i]
            indiceMenor = i
    return indiceMenor

def ordenacao(array):
    arrayOrd=[]

    for i in range(len(array)):
        menor = menorValor(array)
        arrayOrd.append(array.pop(menor))
    print(arrayOrd)

print(array)
ordenacao(array)
print(array)
