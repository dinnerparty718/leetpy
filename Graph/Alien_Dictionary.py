from typing import List


# https://leetcode.com/problems/alien-dictionary/solution/


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        reverse_adj_list = {c: [] for word in words for c in word}

        for index in range(1, len(words)):
            prev = words[index-1]
            cur = words[index]
            i, j = 0, 0

            while prev[i] == cur[j]:
                i += 1
                j += 1
                if i == len(prev) or j == len(cur):
                    #! abc -> ab  invalid input
                    if len(prev) > len(cur):
                        return ''
                    else:
                        break  # else won't execute

            else:
                reverse_adj_list[cur[j]].append(prev[i])

        print(reverse_adj_list)

        # Step 1: Find all edges and put them in reverse_adj_list.
        # for first_word, second_word in zip(words, words[1:]):
        #     for c, d in zip(first_word, second_word):
        #         if c != d:
        #             reverse_adj_list[d].append(c)
        #             break
        #     else:  # Check that second word isn't a prefix of first word.
        #         if len(second_word) < len(first_word):
        #             return ""

        # {'w': [], 'r': ['e'], 't': ['r'], 'f': ['t'], 'e': ['w']}

        # Step 2: Depth-first search.
        seen = {}  # False = grey, True = black.  white = not in seen
        output = []

        # !import detect cycle for all end point

        def visit(node):
            if node in seen:
                return seen[node]

            seen[node] = False

            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False

            seen[node] = True
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)


so = Solution()
words = ["wrt", "wrf", "er", "ett", "rftt"]
#words = ["abc", "ab"]

#words = ["wrt", "wrtkj"]

res = so.alienOrder(words)

print(res)
