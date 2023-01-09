import random

# todo

# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/


class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.h_list = []

    def insert(self, val: int) -> bool:
        if val not in self.h:
            self.h[val] = len(self.h_list)
            self.h_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False
        else:

            last_element = self.h_list[-1]
            idx = self.h[val]

            self.h_list[idx] = last_element

            self.h[last_element] = idx

            self.h_list.pop()
            del self.h[val]

            return True

    def getRandom(self) -> int:

        return random.choice(self.h_list)

    # obj = RandomizedSet()
    # param_1 = obj.insert(val)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()
