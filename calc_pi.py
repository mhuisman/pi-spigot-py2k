#!/usr/bin/env python

# https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula

# py3k-style floating-point division by default
from __future__ import division

import argparse

__author__ = 'https://github.com/mhuisman'

# basic_iterative
# derive iteratively with basic arithmetic operations only
def basic_iterative(digits):
    pi = 0
    p16 = 1
    for k in range(0, digits):
        pi += 1 / p16 * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
        p16 *= 16

    return pi

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Directly calculate the value of any given digit of pi without calculating the preceding digits.')
    parser.add_argument('digit',
                        type=int,
                        help='compute pi to the nth binary digit')
    args = parser.parse_args()
    print basic_iterative(args.digit)


