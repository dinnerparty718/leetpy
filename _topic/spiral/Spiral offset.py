'''
seen in rocketreach hackerrank


def spiral(m,n):

6 * 6

######
     #
#### #
#  # #
#    #
######


2 * 2

##
 #


3 * 1

# 
#
#
'''


def spiral(m: int, n: int) -> list[list[str]]:
    res = [[' '] * n for _ in range(m)]

    left = 0
    right = n-1
    top = 0
    bottom = m-1

    while left <= right and top <= bottom:
        # top
        for col in range(left-1, right+1):
            res[top][col] = 'R'

        top += 2

        # right

        for row in range(top-1, bottom+1):
            res[row][right] = 'D'
        right -= 2

        if top <= bottom:
            for col in reversed(range(left, right+2)):
                res[bottom][col] = 'L'
        bottom -= 2

        if left <= right:
            for row in reversed(range(top, bottom+2)):
                res[row][left] = 'U'
        left += 2

    return res


res = spiral(1, 3)

for row in res:
    print(row)
