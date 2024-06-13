import sys

# Algumas pequenas sugestões.

# Para alcançar números maiores seria interessante usar numpy.
# Mas isso é a última coisa a se fazer.


# the simplest way to speedup this is to use make this  function a lookup table
# from functools import lru_cache
# @lru_cache(max_size=10*3)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# By using recursion it is possible to calculate them in a faster way.
# Check number_decomposition.py
# Note que aqui não é necessário criar uma tabela pq o número não se repete em collatz,
# mas se usar uma função recursiva, ele pode se repetir nele mesmo, aí vale a pena.
def prime_factors(num):
    factors = []
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        else:
            divisor += 1
    return factors


# Vc está buscando duas informações aqui: a decomposição de primos e o collatz.abs
# O ideal é a função fazer apenas uma tarefa, sem os prints. A parte de exibição do resultado
# pode ser feita na função main, que irei introduzir logo abaixo.
def collatz(n):
    numeros = []
    ind = []
    i = 1
    numeros.append(n)
    ind.append(i)
    nu_impar = 0
    nu_par = 0
    print("Número:", n)
    print("Fatores primos:", prime_factors(n))
    print()
    while n != 1:
        if n % 2 == 0:  # Se o número é par
            n = n // 2
            nu_par = nu_par + 1
        else:  # Se o número é ímpar
            n = 3 * n + 1
            nu_impar = nu_impar + 1
        print("Número:", n)
        print("Fatores primos:", prime_factors(n))
        print()
        i = i + 1
        numeros.append(n)
        ind.append(i)

    print("Total impares ", nu_impar)
    print("Total pares ", nu_par)
    print(" Total operacoes ", nu_par + nu_impar)
    print(" Indice ", ind)
    print(" Numeros ", numeros)


if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Evolua um numero usando as regras de Collatz:")
        n = input("Digite um número inteiro: ")
    else:
        n = sys.argv[1]

    try:
        n = int(n)
        collatz(n)
    except ValueError:
        print("Digite um número inteiro")
