'''
1715 · Three Equal Parts

边界条件
首先计算数组中1的数量，如果1的数量为0， 则返回数组的收尾。如果1的数量不能被3整除，则返回[-1, -1]。

算法
第一步：需要把每个1的在数组中的位置记录下来，可以用数组或者哈希表
第二步：计算数组中最后1个1后面的0的数量，按照这个长度把数组分位3个子区间
第三步：从后往前比较划分的区间，以区间长度最短的为基准，依次比较每个位置的数是否一致

复杂度分析
时间复杂度O(n), 空间复杂度O(n)




'''


from typing import (
    List,
)


class Solution:
    """
    @param a: an array
    @return: divide the array into 3 non-empty parts
    """

    def three_equal_parts(self, a: List[int]) -> List[int]:
        # pass
        n = len(a)
        if n < 3:
            return [-1, -1]

        # 计算每个1在a数组中的位置，以及1的数量
        pos, cnt_ones = [0] * (n + 1), 0

        for i, x in enumerate(a):
            if x == 0:
                continue
            cnt_ones += 1
            pos[cnt_ones] = i

        if cnt_ones == 0:
            return [0, n-1]

        if cnt_ones % 3:
            return [-1, -1]

        # 最后一个1后面0的数量, 分组中1的个数
