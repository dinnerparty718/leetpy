from sortedcontainers import SortedList
from collections import defaultdict


# if we want to check existance, do not use defaultdict

# hash
# own naive, very slow
class TwoSum:

    def __init__(self):
        self.sum_set = set()
        self.nums = []

    # slow store all possible value
    def add(self, number: int) -> None:
        if len(self.nums) != 0:
            for num in self.nums:
                self.sum_set.add(num + number)

        self.nums.append(number)

    def find(self, value: int) -> bool:
        return value in self.sum_set


class TwoSum:

    def __init__(self):
        self.count = defaultdict(int)

    # O(1)

    def add(self, number: int) -> None:

        self.count[number] += 1

    # O(1)

    def find(self, value: int) -> bool:
        # find all possbile
        for key in self.count.keys():
            complement = value - key
            # !important default dict will add an entry
            # if complement != key and complement in self.count:

            if complement != key:
                if complement in self.count:
                    return True
            elif self.count[key] > 1:
                return True

        return False


# two pointer with sorted container

class TwoSum:

    def __init__(self):
        self.nums = SortedList()

    def add(self, number: int) -> None:
        self.nums.add(number)

    def find(self, value: int) -> bool:
        l, r = 0, len(self.nums)-1
        while l < r:
            cur_sum = self.nums[l] + self.nums[r]

            if cur_sum > value:
                r -= 1
            elif cur_sum < value:
                l += 1
            else:
                return True

        return False


# two pointer with sort on demand


obj = TwoSum()

obj.add(0)
obj.add(-1)
obj.add(-1)
obj.add(0)

print(obj.nums)

print(obj.find(-2))

print(obj.find(0))
print(obj.find(-1))
print(obj.find(1))
