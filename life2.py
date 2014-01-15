#!/usr/bin/env python

import sys
from life import Board


if __name__ == '__main__':

    try:
        script, size = sys.argv
    except ValueError:
        print 'Usage: {0} <size>'.format(__file__)
        sys.exit(1)

    b = Board.make_board(int(size))
    print b

    b.generate()
    print b
