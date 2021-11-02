# exception
# error handlings

try:
    a = 2/0
except ZeroDivisionError:
    print('divide by zero')
else:
    print('thank you')
finally:  # runs regardless  for logs
    print('finally done')


def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'{err}')


print(sum(3, 0))


# rasie own error
# finally

#raise ValueError('raising my own error')
