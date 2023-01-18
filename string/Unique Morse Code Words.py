from typing import (
    List,
)


class Solution:
    """
    @param words: the given list of words
    @return: the number of different transformations among all words we have
    """

    def unique_morse_representations(self, words: List[str]) -> int:
        # Write your code here
        mor = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        codeSet = set()

        for word in words:
            code = ''
            for char in word:
                code += mor[ord(char) - ord('a')]
            codeSet.add(code)

        return len(codeSet)


so = Solution()


words = ["gin", "zen", "gig", "msg"]
words = ["a", "b"]
res = so.unique_morse_representations(words)
print(res)
