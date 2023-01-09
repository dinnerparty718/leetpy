# https://www.geeksforgeeks.org/applications-of-catalan-numbers/

# recursive
# n number
def catalan(n):
    if n <= 1:
        return 1

    res = 0

    for i in range(1, n+1):
        res += catalan(i-1) * catalan(n-i)

    return res


# print(catalan(3))


# dp
# time O(n^2)

def catalan_dp(n):
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j]

    return dp[n]


print(catalan_dp(3))

# using formula   O(n)
# C(n)  = (2n)! / ( n! * (n+1)! )
