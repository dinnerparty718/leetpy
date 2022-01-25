from typing import List


# own

# build set list O(n)
# permute O(n!)

# todo https://leetcode.com/problems/palindrome-permutation-ii/solution/

# need to optimized. generate palindrome in base case

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        candidate_list = []
        unpair_set = set()

        for c in s:
            if c in unpair_set:
                unpair_set.remove(c)
                candidate_list.append(c)
            else:
                unpair_set.add(c)

        mid = None

        if len(unpair_set) > 1:
            return []
        elif len(unpair_set) == 1:
            mid = unpair_set.pop()

        # permuate candidate_set append one unpair_set if there is one in the set

        res = []

        def swap(i: int, j: int, l: List[str]):
            l[i], l[j] = l[j], l[i]

        #! permute without duplicate

        def permute(index: int, l: List[str]):

            if index == len(l):
                if not mid:
                    res.append(''.join(l[::-1] + l))
                else:
                    res.append(
                        ''.join(l[::-1] + [mid] + l))

                return

            seen = set()

            for i in range(index, len(l)):
                swap(index, i, l)

                if l[index] not in seen:
                    permute(index+1, l)
                    seen.add(l[index])
                swap(index, i, l)

        permute(0, candidate_list)

        return res


so = Solution()

s = "aaaaaa"

res = so.generatePalindromes(s)


print(res)
