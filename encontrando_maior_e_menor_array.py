from numpy import *

array = [1, 2, 3, 4]
maior = 0
menor = 0

for i in array:
    if i == 0:
        maior = menor = array[i]
    else:
        if i < menor:
            menor = array[i]
        elif i > maior:
            maior = array[i]
        
print(menor, maior);