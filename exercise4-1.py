from __future__ import print_function
__author__ = 'ragomez'

try:
    raise RuntimeError('something went wrong')
except RuntimeError, (exp):
    print("catching the raised exception:", exp.message)