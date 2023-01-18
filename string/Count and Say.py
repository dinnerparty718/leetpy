'''
420 · Count and Say


https://leetcode.com/problems/count-and-say/
        n
1       1
11      2
21      3
1211    4
111221  5

复杂度分析

Time: O(N * M) 其中 N 为给定的正整数, M 为生成的字符串中的最大长度
Space: O(M)

'''


class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """

    def count_and_say(self, n: int) -> str:
        # write your code here
        prev = '1'
        i = 2

        while i <= n:
            curr = ''

            char = prev[0]
            cnt = 1

            # loop
            for j in range(1, len(prev)):
                if prev[j] == char:
                    cnt += 1
                else:
                    curr += (str(cnt) + char)
                    cnt = 1
                    char = prev[j]

            curr += (str(cnt) + char)
            prev = curr
            i += 1

        return prev


'''
two pointers to get the length/cnt

'''


class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """

    def count_and_say(self, n: int) -> str:
        prev = '1'
        for i in range(n-1):
            curr = ''
            j = 0
            start = 0

            while j < len(prev):
                while j < len(prev) and prev[j] == prev[start]:
                    j += 1
                curr += str(j - start) + prev[start]
                start = j
            prev = curr

        return prev


so = Solution()
n = 6
res = so.count_and_say(n)
print(f'answer is {res}')
