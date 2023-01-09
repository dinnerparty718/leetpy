from typing import List


'''
attentive: most top 4 common word streaming


build counter hashmap
buiod hashset for banned word

for loop
    - append to buffer when encounter alpha, 
    - not alpha, if buffer not in banned word hashset add to conter
    - update global max count 



'''

# building work until it hit space or .,
# move to the map if not banned
from collections import Counter, defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)

        buffer = []
        counter = defaultdict(int)
        most_common = None

        max_count = 0

        for i in range(len(paragraph)):
            char = paragraph[i]

            if char.isalnum():
                buffer.append(char.lower())

                #! taking care end of loop buffer
                if i != len(paragraph) - 1:
                    continue

            if buffer:
                word = ''.join(buffer)
                if word not in banned_words:
                    counter[word] += 1

                    if counter[word] > max_count:
                        max_count = counter[word]
                        most_common = word

                buffer = []

        return most_common


# time O(M + N)
# space O (M + N)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if not paragraph:
            return ''
        buffer = ''

        right = 0

        count = Counter()

        while right < len(paragraph):
            char = paragraph[right]

            if char.isalpha():
                buffer += char.lower()

            else:

                #! slow here, should've add baneed to set
                if buffer and buffer not in banned:
                    count[buffer] += 1

                buffer = ''

            right += 1

        # when reach the end
        # add current buff
        if buffer:
            count[buffer] += 1
        #! most_common return a tupple (word, count)

        print(count)
        return count.most_common()[0][0]


# leetcode


so = Solution()

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = "a."
banned = []

paragraph = "Bob"
banned = []

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]


res = so.mostCommonWord(paragraph, banned)


print(res)
