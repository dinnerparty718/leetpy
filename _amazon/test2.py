from typing import List

# i j

# sum(  min() * sum())

# https://www.youtube.com/watch?v=TZyBPy7iOAw


class Soloution:

    def getPower(self, powers: List[int]):

        n = len(powers)

        cum_sum = [0] * n

        for idx, val in enumerate(powers):
            if idx == 0:
                cum_sum[idx] = val
            else:
                cum_sum[idx] = cum_sum[idx-1] + val

        for i in range(n):
            for j in range(i, n):
                sub = powers[i:j+1]

                sub_sum = cum_sum[j] - (cum_sum[i-1] if i != 0 else i)

                print(i, j, ' SUM ', sub, min(sub))

        res = 0
        return res % (10**9 + 7)


so = Soloution()

powers = [2, 3, 2, 1]

res = so.getPower(powers)


print(res)


# [1 2,3,4,5,6]
# [6,5,4,3,2,1]
