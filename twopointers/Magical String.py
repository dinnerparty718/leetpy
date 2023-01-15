'''
1215 · Magical String
      r
1, 2, 2 ...
   l
'''


class Solution:
    """
    @param n: an integer 
    @return: the number of '1's in the first N number in the magical string S
    """

    def magical_string(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        # 初始化从第index=2开始，并初始化s = '122'，i记录的是出现的次数，j永远是元素的末尾
        i, j = 2, 2
        s = '122'
        count = 1

        while j < n - 1:
            # 分两种情况，i是1或者2
            if s[i] == '1':
                # 这里说明下一个出现1次，如果上一个末尾是1，则+'2'
                if s[j] == '1':
                    s += '2'
                else:
                    s += '1'
                    count += 1
                # 同时移动下标
                i += 1
                j += 1
            else:
                # 如果i是2，说明j后面要一次加2个一样的数
                if s[j] == '2':
                    s += '11'
                    count += 2
                else:
                    s += '22'
                i += 1
                j += 2

        # 最后会停在n或者n+1的位置。判断一下得到答案
        if len(s) == n:
            return count
        return count - 1 if s[-1] == '1' else count

    #! wow  3 - 1 = 2 , 3 - 2 = 1
    def magical_string(self, n):
        # 魔法数据可以当成原始数据看，也可以当成统计数据看
        # index表示统计数据中的游标
        s, index = [1, 2, 2], 2
        while len(s) < n:
            s += [3 - s[-1]] * s[index]
            index += 1

        return s[:n].count(1)  # ! count value in array


so = Solution()

n = 6

res = so.magical_string(n)
print(res)
