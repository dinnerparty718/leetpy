def generate_combination(input: str):
    res = [[]]

    for char in input:
        if char != '?':
            for i in range(len(res)):
                res[i] = res[i] + [int(char)]

        else:
            res = res * 2

            for i in range(len(res)):
                if i < len(res)/2:
                    res[i] = res[i] + [0]
                else:
                    res[i] = res[i] + [1]

    return res


print(generate_combination('1??0'))
