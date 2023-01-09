
# build dictionary


from typing import List


trie = {}
words = ["oath", "pea", "eat", "rain"]
endOfWord = '$'

for word in words:
    curr = trie
    for c in word:
        if c not in curr:
            curr[c] = {}
        curr = curr[c]
    curr[endOfWord] = word


# for k, v in trie.items():
#     print(k, v)

#! keep track of word index in each node
#! for easy searc
#! autocomplete and word square


words = ["area", "lead", "wall", "lady", "ball"]


def buildTrie(words: List[str]):
    trie = {}
    for idx, word in enumerate(words):
        curr = trie
        for c in word:
            if c not in curr:
                newNode = {}
                newNode['#'] = []
                curr[c] = newNode

            curr = curr[c]
            curr['#'].append(idx)
    return trie


trie = buildTrie(words)


def search_word(trie: dict, words: List[str], prefix: str):
    node = trie

    for c in prefix:
        if c not in node:
            return []
        node = node[c]

    return [words[idx] for idx in node['#']]


print(search_word(trie, words, 'l'))
