'''

'''


def catalan_dp(n):
    if n == 0 or n == 1:
        return 1

    catalan = [0] * (n+1)

    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]

    return catalan[n]


# recursive  find nth catalan number

def catalan(n):
    # base case

    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)
    return res


def main():
    print(catalan_dp(9))


if __name__ == '__main__':
    main()
