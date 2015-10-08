from __future__ import print_function
__author__ = 'ragomez'


class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg


try:
    raise CustomException('something went wrong')
except CustomException, (exp):
    print("catching the raised exception:", exp.msg)