'''
1372 · Ambiguous Coordinates

枚举 enumerate

首先分成两部分还好办,直接用字符串切片即可。其次,难点在于判断分成合理的整数和小数。

1.看能否组成合理整数: 长度为1或者没有前导0
2.看能否组成合理小数：把数字再次分割成整数部分和小数部分

    2.1整数部分可以只有1位并且为0,否则不能有前导0
    2.2小数部分结尾不能为0


'''

from typing import (
    List,
)


class Solution:
    """
    @param s: An string
    @return: An string
             we will sort your return value in output
    """

    def ambiguous_coordinates(self, s: str) -> List[str]:
        s = s[1:-1]  # ! remove ()
        res = []

        for i in range(1, len(s)):  # !从 i = 1 切割
            left, right = s[:i], s[i:]
            left_list = self.get_number(left)
            right_list = self.get_number(right)

            if left and right_list:
                for left_number in left_list:
                    for right_number in right_list:
                        res.append(f'({left_number}, {right_number})')
        return res

    # 0001
    def get_number(self, num: str):
        decimal_list = []
        #! 整数
        if len(num) == 1 or num[0] != '0':
            decimal_list.append(num)
        #! 小数
        for i in range(1, len(num)):
            integer, fractor = num[:i], num[i:]
            if(len(integer) > 1 and integer[0] == '0') or fractor[-1] == '0':
                continue  # !leading and trailing 0 are invalid
            decimal_list.append(integer + '.' + fractor)
        return decimal_list


so = Solution()

s = '(00011)'


res = so.ambiguous_coordinates(s)
print(res)
