import math


def is_prime(num: int):
    if num < 1:
        return False
    for i in range(2, 2, int(num/2)+1):
        if num % i == 0:
            return False

    return True


def is_prime_fast(num: int):
    if num < 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True


print(is_prime_fast(6))
