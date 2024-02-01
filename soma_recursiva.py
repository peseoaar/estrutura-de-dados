array = [2, 4, 6]


def soma(array):
    if array==[]:
        return 0
    else:
        return array[0] + soma(array[1:])

resultado = soma(array)
print(resultado)