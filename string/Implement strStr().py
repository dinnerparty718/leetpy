'''
13 · Implement strStr()
因为本题的时间复杂度比较宽限,不需要更为复杂的KMP算法,可以直接模拟,逐一比对每个字符

1. 先进行特判,若target长度为0,则返回0;若target的长度大于source,则表示不可能匹配,返回-1

2. 枚举匹配source的起始位置,从0到sourceLen-targetLen

3. 对于一个起始位置,比对之后的targetLen位是否相同,若遇到不相同直接退出判断,尝试下一个起始位置

4. 当成功比对完targetLen位后,说明全部相同,则返回起始位置



Time O(M * N)  -> M len of source N len of target
Space O (M + N)

'''


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def str_str(self, source: str, target: str) -> int:
        # 获取两个字符串的长度
        sourceLen = len(source)
        targetLen = len(target)

        # 注意特判，若target长度为0则答案为0
        if targetLen == 0:
            return 0

        # 若target长度大于source，则不可能匹配
        if targetLen > sourceLen:
            return -1

        for i in range(sourceLen - targetLen + 1):
            # k表示比对时source中所指向的字符
            k = i
            for j in range(targetLen):
                if source[k] == target[j]:
                    # 最后一个字符匹配完成，输出答案
                    if j == targetLen - 1:
                        return i
                    k += 1
                # 其中一个字符无法匹配，直接退出做下一次循环
                else:
                    break

        return -1
