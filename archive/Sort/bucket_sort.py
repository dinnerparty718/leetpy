def bucket_sort(l):
    bucket = []

    for i in range(len(l)):
        bucket.append(i)

    print(bucket)


nums = [5, 4, 3, 2, 7, 1]


bucket_sort(nums)


print(nums[1])
