from typing import List

# easier to understand from turing planet

# https://www.youtube.com/watch?v=D_MHAZGtByY&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=5


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                # here a < 0 already
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()

                if stack and stack[-1] == abs(a):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(a)

        return stack

# leet code solution
# !important is use break in while loop. else wont trigger


class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and a < 0 < s[-1]:

                if -a > s[-1]:
                    s.pop()
                    continue
                elif -a == s[-1]:
                    s.pop()
                    # break
                # once   -a < s[-1] disard a
                break
                # break  # break here and else wont trigger
            else:

                s.append(a)

        return s


asteroids = [11, 8, 2, -5, -8, 3]


so = Solution2()

res = so.asteroidCollision(asteroids)

print(res)
