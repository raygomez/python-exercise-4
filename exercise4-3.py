from __future__ import print_function
__author__ = 'ragomez'


def f(data):
    mylist = xrange(0, data,2)
    for i in mylist:
        yield i

number = int(raw_input('Enter a number:'))

for num in f(number):
    print(num, end=',')