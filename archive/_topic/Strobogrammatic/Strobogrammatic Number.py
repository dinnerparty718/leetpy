

# single 8 0 1


# 6 -> 9
# 9 -> 6


'''
matching 

8:8
0:0
1:1
6:9
9:6


two pointer

l, r = 0, len(s)

#! if odd   only 8,0,1 allow in the middle

while l <=r:
    check s[l] in mirror 
        and
    compare mirror[s[l]] == s[r]
    
    l+=1
    r-=1

'''


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirror = {
            '8': '8',
            '0': '0',
            '6': '9',
            '9': '6',
            '1': '1'
        }

        l, r = 0, len(num)-1

        while l <= r:
            if num[l] not in mirror or mirror[num[l]] != num[r]:
                return False
            l += 1
            r -= 1

        return True


so = Solution()
num = "868"

res = so.isStrobogrammatic(num)

print(res)
