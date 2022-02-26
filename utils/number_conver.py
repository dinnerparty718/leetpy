from numerize import numerize


def numStr(number: int):

    return numerize.numerize(number)


def main():
    num = 300_000_000

    print(numStr(num))


if __name__ == '__main__':
    main()
