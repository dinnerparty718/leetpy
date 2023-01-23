# https://www.youtube.com/watch?v=j2_JW3In9PE&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=4


# two rules
# 1. reduce range for each iteration or recursion, otherwise infite loop
# 2. do not exclude potential answer, template 2

# template 1
# find exact val, return -1 if not exist
# 找2
# while l <= r
# l > r after while loop, no value need to be checked
# mid = l + (r-l)/2
# l = mid + 1
# r = mid - 1


# template 2
# find first occurrence, or last occurrence
# 模糊值 第一个2,最后一个2
# first occurence
# while l < r
# need to check l(r) value l = r after the while loop
# mid = l + (r-l)/2
# l = mid + 1
# r = mid
# last occurence
# mid = l +  (r-l+1)/2  so mid stay on the right side
# l = mid
# r = mid -1


# template 3
# find closest vale to 2
# 找最接近2
# while l < r -1
# need to check both l and r value after while loop, l + 1 = r
# mid = l + (r-l)/2
# l = mid
# r = mid
# 34 if nums[l] > 2 return nums[l]
# 01 if nums[r] <2 return nums[r]
# 14 nums[l] if 2-num[l] < num[r] -2 else nums[r]   2 is between both l and r position
