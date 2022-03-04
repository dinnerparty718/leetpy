from typing import List

'''

152 Maximum Product Subarray

https://leetcode.com/problems/maximum-product-subarray/




https://www.youtube.com/watch?v=FqpfLr76a1k

[1, -2, -3, 4]

DP
    pos_cnt = 0
    neg_cnt = 0
    global_max = 0

#! recurrence
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            pos_cnt = neg_cnt = 0
            
        elif nums[i] > 0:
            pos_cnt+=1
            
            if neg_cnt !=0:
                neg_cnt+=1
            
            update global_max
            
        else:
            #! number < 0
            pos_cnt, neg_cnt = neg_cnt , pos_nct
            neg_cnt+=1
            if pos_cnt !=0:
                pos_cnt +=1
            
            update global_max

#! return global_max

'''

# hard to understand but more efficient
#
# Time O(n)
# Space O(1)


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)

        positive_cnt = 0
        negative_cnt = 0

        res = 0

        for i in range(n):
            if nums[i] == 0:
                # reset
                positive_cnt = negative_cnt = 0

            elif nums[i] > 0:
                positive_cnt += 1

                if negative_cnt != 0:
                    negative_cnt += 1

                res = max(res, positive_cnt)

            else:
                positive_cnt, negative_cnt = negative_cnt, positive_cnt

                negative_cnt += 1

                if positive_cnt != 0:
                    positive_cnt += 1

                res = max(res, positive_cnt)

        return res


# Time  O(n)
# Space O(n)
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)

        pos = [0] * n
        neg = [0] * n

        if nums[0] > 0:
            pos[0] = 1

        if nums[0] < 0:
            neg[0] = 1

        res = pos[0]

        for i in range(1, n):
            cur = nums[i]

            if cur > 0:
                pos[i] = pos[i-1] + 1
                neg[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0

            # !?? 负风得正
            if cur < 0:
                pos[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
                neg[i] = 1 + pos[i-1]

            res = max(res, pos[i])

        return res


so = Solution()

nums = [1, -2, -3, 4]
# nums = [0, 1, -2, -3, -4]

res = so.getMaxLen(nums)


print(res)
