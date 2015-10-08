from __future__ import print_function
__author__ = 'ragomez'


def prepend_this_is(f):
    def _(args):
        args = 'This is {}'.format(args)
        return f(args)
    return _


def append_exclamation(f):
    def _(args):
        args = '{}!'.format(args)
        return f(args)
    return _


@prepend_this_is
@append_exclamation
def sparta(name):
    print(name)

sparta('Sparta')