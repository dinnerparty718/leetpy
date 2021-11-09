from typing import List
from collections import deque


# own approach
# improvement is to just store the idx in the stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            if not stack or temp < stack[-1][0]:
                stack.append((temp, idx))
            else:
                # pop multiple
                while stack and temp > stack[-1][0]:
                    t, i = stack.pop()
                    res[i] = idx - i

                stack.append((temp, idx))

        return res

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = idx - i
            stack.append(idx)

        return res


solution = Solution()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#temperatures = [30, 40, 50, 60]
#temperatures = [30, 60, 90]
res = solution.dailyTemperatures2(temperatures)


print(res)
