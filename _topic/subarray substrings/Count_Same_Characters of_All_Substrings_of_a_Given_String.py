

'''
Given a string. The task is to find out the numbers of substrings consisting of the same characters.

nput: abba 
Output: 5 
The desired substrings are {a}, {b}, {b}, {a}, {bb}

Input: bbbcbb 
Output: 10 

#! number of substring
n*(n+1)/2
 
O(n)
loop throught the list
find consecutive string 'aaa' and genereate the result


'''


def count_number(input: str) -> int:
    res = 0
    cnt = 1

    n = len(input)
    l, r = 0, 1

    while r < n:
        if input[l] == input[r]:
            cnt += 1
        else:
            res += cnt * (cnt + 1) // 2

            l = r
            cnt = 1
        r += 1

    res += cnt * (cnt + 1) // 2

    return res


s = "zzzyz"


res = count_number(s)

print(res)
