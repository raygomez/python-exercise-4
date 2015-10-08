from __future__ import print_function
__author__ = 'ragomez'

try:
    raise RuntimeError()
except RuntimeError:
    print("catching the raised exception")