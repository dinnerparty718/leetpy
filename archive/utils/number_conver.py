from numerize import numerize


def numStr(number: int):

    return numerize.numerize(number)


def main():
    num = 2**32

    print(numStr(num))


if __name__ == '__main__':
    main()
