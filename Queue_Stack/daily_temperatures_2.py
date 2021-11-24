from typing import List

# monotonic descresing (or equal) stack


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = idx - i
            stack.append(idx)

        # print(stack)   6, 7 is left since iteration done

        return res


# time O(n)
# space O(n) with stack


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in reversed(range(len(temperatures))):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack.pop()

            if not stack:
                res[i] = 0
                stack.append(i)
            else:
                res[i] = stack[-1] - i
                stack.append(i)

        return res


so = Solution()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

res = so.dailyTemperatures(temperatures)
print(res)
