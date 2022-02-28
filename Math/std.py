import statistics


nums = [4, 5, 8, 9, 10]
print(statistics.pstdev(nums))


def standardDiv(nums: list[int]) -> float:
    mean = sum(nums)/len(nums)
    variance = sum([abs(num - mean) ** 2 for num in nums]) / len(nums)
    return variance ** 0.5


print(standardDiv(nums))
print(standardDiv([2, 3, 4]))  # standard div smaller

print(standardDiv([1, 3, 4]))
