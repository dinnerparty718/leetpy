'''
in virtu test

total weight <=5000

A = [ 4650,  ]

#todo

'''


def solution(A: list[int]) -> int:
    max_weight = 5000
    target = max_weight - A[0]
    weights = A[1:]

    return 0


A = [4650, 150, 150, 150]
# A = [4850, 100, 30, 30, 100, 50, 100]

res = solution(A)
