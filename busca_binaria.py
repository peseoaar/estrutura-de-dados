array = []
encontrado=0
posicao=0


for i in range(101):
    if i != 0:
        array.append(i)

valor = int(input("Digite o valor a ser buscado: "))

inicio = 0
fim = len(array) - 1


while encontrado!=1 and fim>=inicio:
    meio = int((fim + inicio) / 2)

    if valor == array[meio]:
        posicao = meio
        encontrado+=1
    elif valor > array[meio]:
        inicio = meio + 1
    elif valor < array[meio]:
        fim = meio - 1 

if encontrado != 0:
    print("O valor", valor,"se encontra na posicao", posicao)
else: 
    print("Valor nao encontrado no vetor")

