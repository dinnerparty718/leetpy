'''
421 · Simplify Path
https://leetcode.com/problems/simplify-path/description/

#! python splits has empty spaces
#! to remove empty space use filter

my_list = list(filter(None, my_str.split(',')))

['', 'home', '', 'foo', '']


use stack
将原字符串以 '/' 分隔, 然后遍历:
    - 遇到正常的目录名, 入栈
    - 遇到 '.' 或 空名称 (对应 "//") 则忽略
    - 遇到 ".." 则从栈顶弹出一个元素 (如果栈为空则不弹栈, 对应 "/../")

最后将栈中的元素以 '/' 连接得到结果.


'''


class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """

    def simplify_path(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for i in path:
            if i == '..':
                if len(stack):
                    stack.pop()
            elif i != '.' and i != '':
                stack.append(i)
        return '/' + '/'.join(stack)


so = Solution()

path = "/home/"
path = '/a/./../../c/'
path = "/home//foo/"


res = so.simplify_path(path)
print(res)
