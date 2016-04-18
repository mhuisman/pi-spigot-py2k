# https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
# implemented iteratively with sole use of basic arithmetic operations

# get py3k-style floating-point division by default
from __future__ import division

__author__ = 'https://github.com/mhuisman'

def derive_pi(digits):
    pi = 0
    p16 = 1
    for k in range(0, digits):
        pi += 1/p16 * (4 / (8*k + 1) - 2 / (8*k + 4) - 1 / (8*k + 5) - 1 / (8*k + 6))
        p16 *= 16

    return pi

for i in range(0, 9):
    print derive_pi(i)


