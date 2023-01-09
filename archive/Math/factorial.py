import math

# recursion


def factorial(n):
    return 1 if (n == 0 or n == 1) else n * factorial(n-1)


def factorial_i(n):
    if n <= 1:
        return 1

    fact = 1

    while n > 1:
        fact *= n
        n = n - 1
    return fact


print(factorial(3))
print(factorial_i(3))


print(math.factorial(3))
