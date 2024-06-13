# Algumas pequenas sugestões.
# Para alcançar números maiores seria interessante usar numpy.


# the simplest way to speedup this is to use make this  function a lookup table
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# By using recursion it is possible to calculate them in a faster way. Check my Prime decomposition.
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


# Heheh, o ideal é não usar os prints, talvez guardar o histórico com a
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
