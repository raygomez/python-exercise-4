from __future__ import print_function
__author__ = 'ragomez'


def f(data):
    mylist = xrange(0, data)
    for i in mylist:
        if ((i % 5) == 0) and ((i % 7) == 0):
            yield i

number = int(raw_input('Enter a number:'))

for num in f(number):
    print(num, end=',')