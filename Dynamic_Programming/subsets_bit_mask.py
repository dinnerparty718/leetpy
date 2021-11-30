def generateBitMask(n: int):
    res = []
    # avoid left padding
    for i in range(2**n, 2**(n + 1)):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i)[3:]
        res.append(bitmask)

    return res


nums = [1, 2, 3]

a = generateBitMask(len(nums))

res = []

for s in a:
    item = []
    for idx, _bit in enumerate(s):
        if _bit == '1':
            item += [nums[idx]]

    res.append(item)


print(res)
