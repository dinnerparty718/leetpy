'''
if N == 1 or 0 return N
first = 0
second = 1

third = first + second

first = second
second  = third

constant memory
'''


def nearestFibonacchi(num):
    # base case

    if num == 0:
        return 0

    first = 0
    second = 1

    third = first + second

    while third <= num:
        first = second
        second = third

        third = first + second

    # print(third, second)

    return second if (third - num) >= (num - second) else third


def main():
    N = 17

    print(nearestFibonacchi(N))


if __name__ == '__main__':
    main()
