#-------1------------
#caderno = {}

#nome = input("Digite seu nome: ")
#caderno[nome] = 1

#-------2-----------
#caderno = {}

#nome = input("Digite seu nome: ")
#tam_string = len(nome)

#caderno[nome] = tam_string

#-------3-----------

#caderno = {}

#for i in range(2):
#    nome = input("Digite seu nome: ")
#    primeira_letra = nome[0]
#    caderno[nome] = primeira_letra

#print(caderno)

#-------4-----------
import string


def gerar_primos(qtd):
    primos = []  
    num = 2 
    while len(primos) < qtd:
        # Verifica se 'num' é primo, não sendo divisível por nenhum número já presente em 'primos'
        if all(num % i != 0 for i in primos):
            primos.append(num) 
        num += 1  
    return primos  

# Cria uma lista de letras minúsculas do alfabeto usando a função 'ascii_lowercase'
letras = list(string.ascii_lowercase)

# Chama a função 'gerar_primos' passando o número de letras como argumento e armazena o resultado
numeros_primos = gerar_primos(len(letras))

# Cria um dicionário associando cada letra ao seu respectivo número primo usando a função 'zip'
caderno = dict(zip(letras, numeros_primos))

# Imprime o dicionário resultante
print(caderno)
