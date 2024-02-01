import numpy as np 

i=0
j=0

carros = [
    ["Modelo", "Fabricante", "Ano", "Valor"],
    ["Civic", "Honda", "1995", 11000],
    ["Palio", "Fiat", "1998", 4200],
    ["Santana", "Chevrolet", "2002", 1750]
]

for i in range(4):
    for j in range(4):
        print(" | ",carros[i][j], end=" ")
        if j == 3:
            print()
         