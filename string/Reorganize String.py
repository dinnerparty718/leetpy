'''
1041 · Reorganize String
先统计每个字母出现的数,如果有一个超过一半了,直接返回空;不然进行交错排列即可

[['a', 'b'], ['a']]
https://www.youtube.com/watch?v=2g_b1aYTHeg
'''

from collections import Counter


class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def reorganize_string(self, s: str) -> str:
        # write your code here
        if len(s) < 2:
            return s

        n = len(s)
        counter = Counter(s).most_common()
        _, max_freq = counter[0]
        if max_freq > (len(s) + 1) // 2:
            return ''
        else:
            buckets = [[] for i in range(max_freq)]
            begin = 0
            for letter, count in counter:
                for i in range(count):
                    buckets[(i + begin) % max_freq].append(letter)
                begin += count

        print(buckets)

        return ''.join(''.join(bucket) for bucket in buckets)


so = Solution()

s = 'aab'
res = so.reorganize_string(s)
print(res)
