from __future__ import print_function
__author__ = 'ragomez'


class MultiplesOf7(object):

    def __init__(self, n):
        self.n = n
        self.num = 0

    def next(self):
        self.num += 7
        if self.num < self.n:
            return self.num
        else:
            raise StopIteration

    def __iter__(self):
        return self

limit = 100

for number in MultiplesOf7(limit):
    print(number)
