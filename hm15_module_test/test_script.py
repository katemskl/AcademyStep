from script import Numbers, Number
from unittest import TestCase


class TestNumbers(TestCase):
    def test_sum(self):
        numbers = Numbers(1, 2, 3, 4, 5)

        self.assertEqual(numbers.sum(), 15, 'Must be 15')

    def test_arithmetic_mean(self):
        numbers = Numbers(1, 2, 3, 4, 5)

        self.assertEqual(numbers.arithmetic_mean(), 3, 'Must be 3')

    def test_max(self):
        numbers = Numbers(1, 2, 3, 4, 5)

        self.assertEqual(numbers.max(), 5, 'Must be 5')

    def test_min(self):
        numbers = Numbers(1, 2, 3, 4, 5)

        self.assertEqual(numbers.min(), 1, 'Must be 1')


class TestNumber(TestCase):
    def test_octal_system(self):
        number = Number(20)

        self.assertEqual(number.octal_system(), 24, 'Must be 24')

    def test_hexadecimal_system(self):
        number = Number(20)

        self.assertEqual(number.hexadecimal_system(), 14, 'Must be 14')

    def test_binary_system(self):
        number = Number(20)

        self.assertEqual(number.hexadecimal_system(), 10100, 'Must be 10100')
