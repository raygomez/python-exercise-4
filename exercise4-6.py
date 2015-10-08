from __future__ import print_function
__author__ = 'ragomez'


def fibonacci(n):
    i = 0
    j = 1

    while j < n:
        i, j = i, i + j
        yield i


number = int(raw_input('Enter limit of fibonacci sequence:'))

for i in fibonacci(number):
    print(i)
