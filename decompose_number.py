from typing import List


def decompose(number: int) -> List[int]:

    result = []

    negative = False
    if number < 0:
        number = -number
        negative = True

    for n in range(2, number):

        if number % n == 0:
            result = [n, *decompose(int(number / n))]
            break

    result = result if result else [number]

    if negative:
        result[0] = -result[0]

    return result
