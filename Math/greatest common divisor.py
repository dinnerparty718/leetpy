'''
12   54


54 % 12 = 6

6 and 12

12 % 6 = 0


GCD  = 6


Time O(max(a,b))
Space 1

'''


def GCD(a, b):
    if b == 0:
        return a

    return GCD(b, a % b)


print(GCD(12, 54))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
