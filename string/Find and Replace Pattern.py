'''
1592 · Find and Replace Pattern

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

use 2 hash

我们可以用两个映射表（map）存储字母到字母的映射关系，第一个映射表保证一个字母不会映射到两个字母，第二个映射表保证不会有两个字母映射到同一个字母。例如 word 为 a，pattern 为 x，那么第一个映射表存储 a -> x，第二个映射表存储 x -> a。

Time O(N*K) N 其中 NN 是数组 words 的长度，KK 是每个单词的长度。
Space O(N*K)



'''


from typing import (
    List,
)


class Solution:
    """
    @param words: word list
    @param pattern: pattern string
    @return: list of matching words
             we will sort your return value in output
    """

    def find_and_replace_pattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1:
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if(m1[w], m2[p]) != (p, w):
                    return False
            return True

        return list(filter(match, words))


so = Solution()

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
res = so.find_and_replace_pattern(words, pattern)
print(res)
