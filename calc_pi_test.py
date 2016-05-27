#!/usr/bin/env python

import unittest
import calc_pi
from decimal import *

class TestCalculatePi(unittest.TestCase):
    pi = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923)

    # the 0th digit of pi is 0, believe it or not
    def test_zero(self):
        self.assertEquals(0, calc_pi.basic_iterative(0))

    # calculate accuracy up to 100 digits
    def test_nonzero(self):
        getcontext().prec = 100
        # account for 3. in the string
        offset = 2
        for k in range(1, 99):
            print "k: ", k
            print "expected"
            print round(TestCalculatePi.pi, k)
            print "actual"
            print round(calc_pi.basic_iterative(k), k)
            self.assertEquals(round(TestCalculatePi.pi, k), round(calc_pi.basic_iterative(k), k))

if __name__ == '__main__':
    unittest.main()

