'''
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')


'''

'''

0 
word1 = ''
word2 = ''

0 
word1 = 'abc'
word2 = 'abc'


3 = len(word1)
word1 = 'abc'
word2 = ''


3 = len(word2)
word1 =  ''
word2 = 'abc'

https://www.youtube.com/watch?v=XYi2-LPrwm4


w1[i] = w2[j] - > (i+1, j+1)

else + 1

insert (i, j+1)
delete (i+1, j)
replace (i+1, j+1)

        w2   j
i    w
     1


DP
dp = [[float('inf')] * (n+1) for _ in range(m+1)] 
hint: minDistance

#! basecase

    +++3
    +++2
    +++1
    3210

#! recurrence

    if matched, look for diagonal
    
    if w1[i] == w2[j]:
        dp[i][j] = dp[i+1][j+1]
    else
        one change  min(insert, delete replace)
        dp[i][j] = 1 + min(dp[i][j+1],dp[i+1][j], dp[i+1][j+1]  )



#! return dp[0][0]

'''


# bottom up

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # extra column
        # extra row
        dp = [[float('inf')] * (n + 1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][n] = m - i

        for j in range(n+1):
            dp[m][j] = n - j

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1],  dp[i+1][j], dp[i+1][j+1])

        # for row in dp:
        #     print(row)

        return dp[0][0]


so = Solution()

word1 = 'abd'
word2 = 'acd'

res = so.minDistance(word1, word2)

print(res)
