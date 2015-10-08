from __future__ import print_function
__author__ = 'ragomez'


def fibonacci(n):
    x = 0
    y = 1

    while x <= n:
        yield x
        x, y = y, x + y


number = int(raw_input('Enter limit of fibonacci sequence:'))

for i in fibonacci(number):
    print(i)
