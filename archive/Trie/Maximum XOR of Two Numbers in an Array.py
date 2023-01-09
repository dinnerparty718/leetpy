from typing import List


# (1 << k) | n

# Tire without extra class
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        binaries = [bin(n)[2:] for n in nums]
        maxLen = max(len(b) for b in binaries)
        tmp = [b_s.zfill(maxLen) for b_s in binaries]

        # bin returns 'ob0101'
        # L = len(bin(max(nums))) - 2

        # nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]

        # print(nums)

        trie = {}
        max_xor = 0  # 10 base

        for num in tmp:
            node = trie
            xor_node = trie
            curr_xor = 0  # '00000'

            # bit is char
            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node = node[bit]

                toggled_bit = str(1 - int(bit))
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    # no choice here
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, curr_xor)

            # to compute max xor of that new number

        return max_xor
        # for k, v in trie.items():
        #     print(k, v)


so = Solution()
nums = [3, 10, 5, 25, 2, 8]


res = so.findMaximumXOR(nums)

print(res)


# int('11100', 2)
