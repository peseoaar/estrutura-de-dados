# recursao fatorial 

### nao esquece o  caso base

#5!= 5 * 4 * 3 * 2 * 1

print ("CALCULO DE FATORIAL")
print ("=+=+=+=+=+=+=+=+=+=")
n = int(input("Digite um numero:"))


def fatorial(n):
    if n == 1: ##caso base
        return 1
    else:
        return n * fatorial(n-1)
    
print(n,"! =",fatorial(n))


