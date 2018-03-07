import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_adds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)
    def test_subtract(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 +')
    def test_multiplication(self):
        result = rpn.calculate('2 3 *')
        self.assertEqual(6, result)
    def test_division(self):
        result = rpn.calculate('6 2 /')
        self.assertEqual(3, result)
    def test_exponent(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)
    def test_bitwiseAND(self):
        result = rpn.calculate('15 11 &')
        self.assertEqual(11, result)
    def test_bitwiseOR(self):
        result = rpn.calculate('15 22 |')
        self.assertEqual(31, result)
        result = rpn.calculate('22 0 |')
        self.assertEqual(22, result)
    def test_bitwiseNOT(self):
        result = rpn.calculate('1 ~')
        self.assertEqual((-2), result)
        result = rpn.calculate('0 ~')
        self.assertEqual(-1, result)
        result = rpn.calculate('3 ~')
        self.assertEqual((-4), result)
    def test_factorial(self):
        result = rpn.calculate('4 !')
        self.assertEqual(24, result)
        result = rpn.calculate('0 !')
        self.assertEqual(1, result)
    def test_divisionZero(self):
        result = rpn.calculate('1 0 /')
        self.assertEqual(3, result)