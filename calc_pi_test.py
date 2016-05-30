#!/usr/bin/env python

import unittest
import calc_pi
from decimal import *

class TestCalculatePi(unittest.TestCase):
    pi = "3.1415926535897932384626433832795028841971693993751058209749445923"

    # the 0th digit of pi is 0, believe it or not
    def test_zero(self):
        self.assertEquals(0, calc_pi.basic_iterative(0))

    # calculate accuracy up to 100 digits
    def test_nonzero(self):
        getcontext().prec = 200
        # account for 3. in the string
        offset = 2
        exponent_operand = '1.'
        for k in range(1, 99):
            exponent_operand += '0'
            #print "k: ", k
            #print "exp", exponent_operand
            #print "expected"
            #print Decimal(TestCalculatePi.pi[:offset+k])
            #print "computed"
            #print Decimal(calc_pi.basic_iterative(k)).quantize(Decimal(exponent_operand), rounding=ROUND_DOWN)
            self.assertEquals(
                Decimal(TestCalculatePi.pi[:offset+k]),
                Decimal(calc_pi.basic_iterative(k)).quantize(Decimal(exponent_operand), rounding=ROUND_DOWN))

if __name__ == '__main__':
    unittest.main()

