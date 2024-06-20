from functools import cache
from typing import List


# It is possible to make it faster by avoiding the negative number checkage!
@cache
def prime_factors_cache(number: int) -> List[int]:

    result = []

    negative = False
    if number < 0:
        number = -number
        negative = True

    for n in range(2, number):

        if number % n == 0:
            result = [n, *prime_factors(int(number / n))]
            break

    result = result if result else [number]

    if negative:
        result[0] = -result[0]

    return result


def prime_factors(number: int) -> List[int]:

    result = []

    negative = False
    if number < 0:
        number = -number
        negative = True

    for n in range(2, number):

        if number % n == 0:
            result = [n, *prime_factors(int(number / n))]
            break

    result = result if result else [number]

    if negative:
        result[0] = -result[0]

    return result
