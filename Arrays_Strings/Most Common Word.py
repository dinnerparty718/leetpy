import enum
import heapq
import operator
from typing import List
from collections import defaultdict


# own
# no replacement one pass if the paragraph can't fit to memeory!! on-the-fly
# time O(M + N)
# space O(1)


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = [ban.lower() for ban in banned]
        stop_words = {'!', '?', '\'', ',', '.', ';', ' '}

        common_list = defaultdict(int)

        left = right = 0

        while right < len(paragraph):
            while right < len(paragraph) and paragraph[right] not in stop_words:
                right += 1

            word = paragraph[left: right].lower()

            if word not in banned_set:
                common_list[word] += 1

            # move left,right cursor

            while right < len(paragraph) and paragraph[right] in stop_words:
                right += 1

            left = right
        #! trick to get max from a list of tuple
        #! python min max O(n)
        return max(common_list.items(), key=operator.itemgetter(1))[0]

# leetcode 1 in pipeline


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1 repalce the puncturations with spaces , conver to lower case
        normalized_str = ''.join(
            [c.lower() if c.isalnum() else ' ' for c in paragraph])

        # 2 split
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        # 3.count

        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        # 4 return max  python min max are O(N)

        return max(word_count.items(), key=operator.itemgetter(1))[0]

# leetcode 2 on the fly, build words in buffer


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)
        ans = ''
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        for p, char in enumerate(paragraph):
            # 1 comsue the charatctors in a word

            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    #! trick
                    continue

            # 2 at the end of on word or at the end of paragraph
                # buidling ans on the fly ! good for streaming

            if len(word_buffer) > 0:
                word = ''.join(word_buffer)
                if word not in banned_words:
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word

                word_buffer = []

        return ans


# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# paragraph = "a."
# banned = []
paragraph = "L, P! X! C; u! P? w! P. G, S? l? X? D. w? m? f? v, x? i. z; x' m! U' M! j? V; l. S! j? r, K. O? k? p? p, H! t! z' X! v. u; F, h; s? X? K. y, Y! L; q! y? j, o? D' y? F' Z; E? W; W' W! n! p' U. N; w? V' y! Q; J, o! T? g? o! N' M? X? w! V. w? o' k. W. y, k; o' m! r; i, n. k, w; U? S? t; O' g' z. V. N? z, W? j! m? W! h; t! V' T! Z? R' w, w? y? y; O' w; r? q. G, V. x? n, Y; Q. s? S. G. f, s! U? l. o! i. L; Z' X! u. y, Q. q; Q, D; V. m. q. s? Y, U; p? u! q? h? O. W' y? Z! x! r. E, R, r' X' V, b. z, x! Q; y, g' j; j. q; W; v' X! J' H? i' o? n, Y. X! x? h? u; T? l! o? z. K' z' s; L? p? V' r. L? Y; V! V' S. t? Z' T' Y. s? i? Y! G? r; Y; T! h! K; M. k. U; A! V? R? C' x! X. M; z' V! w. N. T? Y' w? n, Z, Z? Y' R; V' f; V' I; t? X? Z; l? R, Q! Z. R. R, O. S! w; p' T. u? U! n, V, M. p? Q, O? q' t. B, k. u. H' T; T? S; Y! S! i? q! K' z' S! v; L. x; q; W? m? y, Z! x. y. j? N' R' I? r? V! Z; s, O? s; V, I, e? U' w! T? T! u; U! e? w? z; t! C! z? U, p' p! r. x; U! Z; u! j; T! X! N' F? n! P' t, X. s; q'"

banned = ["m", "i", "s", "w", "y", "d", "q", "l", "a", "p",
          "n", "t", "u", "b", "o", "e", "f", "g", "c", "x"]
so = Solution()
res = so.mostCommonWord(paragraph, banned)

print(res)
