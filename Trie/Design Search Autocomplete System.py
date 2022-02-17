from typing import List
import heapq


'''
Use Trie
    add hot:int in to Node Class
    hot value stores at end of sentence
Store current search in array cur_input = []


steps
    build trie
    
    user input '#'
        add current search to trie
        epmty curretn search cur_input = []
    else:
        append char to cur_input
        find the last node from input
        search in the trie from that node
            recursively search
            base case
                reach 
                
            do:
                get a list of sentences (-hot, sentence) for max heap
        len of sentences > 3, heapify. 
        return


'''


# todo check youtube
# todo 2/5

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
        self.hot = 0


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):

        self.root = TrieNode()
        self.cur_input = []

        for s, t in zip(sentences, times):
            cur = self.root

            for c in s:
                if c not in cur.children:
                    cur.children[c] = TrieNode()

                cur = cur.children[c]

            cur.endOfWord = True
            cur.hot = t

        # print(
        #     self.root.children['i'].children['r'].children['o'].children['m'].children['a'].children['n'].hot)

    def input(self, c: str) -> List[str]:
        if c == '#':
            if self.cur_input:
                cur = self.root
                for ch in self.cur_input:
                    if ch not in cur.children:
                        cur.children[ch] = TrieNode()

                    cur = cur.children[ch]

                cur.endOfWord = True
                cur.hot += 1
                self.cur_input = []

            return []

        self.cur_input.append(c)

        cur = self.root

        for ch in self.cur_input:

            if ch not in cur.children:
                return []

            cur = cur.children[ch]

        res = []

        self.search(cur, res, [])

        heapq.heapify(res)

        ret = []

        n = 3
        while n > 0 and len(res):
            ret.append(''.join(self.cur_input) + heapq.heappop(res)[1])
            n -= 1

        return ret

    def search(self, node: TrieNode, res: List[tuple], path: List):
        # end condition n not node.chidren

        # print(node, path)
        if not node.children:
            if node.endOfWord == True:
                res.append((-node.hot, ''.join(path)))
                # print(res)
            return

        if node.endOfWord == True:
            res.append((-node.hot, ''.join(path)))
            # print(res)

        for c in node.children:
            self.search(node.children[c], res, path + [c])


sentences = ["i love you", "island", "iroman", "i love leetcode"]
times = [5, 3, 2, 2]

obj = AutocompleteSystem(sentences, times)


print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
