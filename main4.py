from source.calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        calculator = Calculator(10, 2)

        self.assertEqual(calculator.multiply(), 20, 'Must be 20!')
        # self.assertEqual(calculator.multiply(), 10, 'Must be 10!')  # - wrong variant

        calculator2 = Calculator(10, -2)
        self.assertEqual(calculator2.multiply(), -20, 'Must be -20!')

    def test_plus(self):
        calculator = Calculator(10, 2)

        self.assertEqual(calculator.plus(), 12, 'Must be 12!')
        # self.assertEqual(calculator.plus(), 11, 'Must be 11!')  # - wrong variant

        calculator2 = Calculator(-10, -1)

        self.assertEqual(calculator2.plus(), -11, 'Must be -11!')

    def test_minus(self):
        calculator = Calculator(10, 2)

        self.assertEqual(calculator.minus(), 8, 'Must be 8!')
        # self.assertEqual(calculator.minus(), 11, 'Must be 11!')  # - wrong variant

        calculator2 = Calculator(-10, -1)

        self.assertEqual(calculator2.minus(), -9, 'Must be -9!')

    def test_division(self):
        calculator = Calculator(10, 2)

        self.assertEqual(calculator.division(), 5, 'Must be 5!')
        # self.assertEqual(calculator.division(), 6, 'Must be 6 !')  # - wrong variant

        calculator2 = Calculator(10, 0)

        with self.assertRaises(ZeroDivisionError) as context:
            calculator2.division()
        self.assertTrue('Division by zero!' in str(context.exception))

        calculator3 = Calculator(10, -2)

        self.assertEqual(calculator3.division(), -5, 'Must be -5!')


