from typing import List


# one time
# monotonic stack  small at the bottom

#
#
#
#
# 72 , 5
# 75 , 2


# Time O(n)
# space O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                output[idx] = i - idx

            stack.append(i)

        return output


so = Solution()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

res = so.dailyTemperatures(temperatures)

print(res)
