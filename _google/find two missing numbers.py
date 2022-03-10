'''
method 1 O(n) with O(n) space. can be used for multiple missing number
method 2 O(n) O(1) 
    use Gaus formula twice  n * (n + 1) // 2



'''

# method1


def findTwoMissingNumbers(arr, n):
    flags = [False] * (n+1)

    for i in range(len(arr)):
        flags[arr[i]] = True

    return [idx for idx, flag in enumerate(flags) if not flag and idx != 0]


# method2
def findTwoMissingNumbers(arr, n):
    arr_sum = sum(arr)
    expected_sum = n * (n + 1) // 2

    missing_sum = expected_sum - arr_sum

    # Find average of two elements
    avg = missing_sum / 2

    sumSmallerHalf = 0
    sumGreaterHalf = 0

    for num in arr:
        if num <= avg:
            sumSmallerHalf += num
        else:
            sumGreaterHalf += num

    totalSmallerHalf = int((avg * (avg + 1)) / 2)

    smaller = totalSmallerHalf - sumSmallerHalf

    return [smaller,  missing_sum - smaller]


arr = [1, 3, 5, 6]
n = len(arr) + 2


print(findTwoMissingNumbers(arr, n))
