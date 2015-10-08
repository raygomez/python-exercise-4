from __future__ import print_function
__author__ = 'ragomez'

from datetime import datetime
class Logger(object):

    def __init__(self,f):
        self.f = f

    def __call__(self, *args, **kwargs):
        arguments = ','.join([str(x) for x in args])

        print('<{}> {}({}, {})'.format(datetime.now(), self.f.func_name, arguments, kwargs))
        # print('<', ctime(time()), '>', self.f.func_name, '(',args, kwargs, ')')
        i = self.f(*args, **kwargs);
        return i


@Logger
def f1():
    print('hello!')

@Logger
def f2(foo):
    print('hello!', foo)

@Logger
def f3(foo, bar):
    print('hello!', foo, bar)

f1()
f2('abc')
f3('abc', bar='def')
