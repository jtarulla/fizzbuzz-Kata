import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)
    
    def test_1_does_not_raise_error(self):
        self.assertEqual(FizzBuzz(1).value, 1)

    def test_minus_1_raise_error(self):
        self.assertRaises(ValueError, FizzBuzz, -1)
    
    def test_value_over_100_raise_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(105)

    def test_1_returns_1(self):
        self.assertEqual(FizzBuzz(1).value, 1)

    def test_value_divisible_by_3_returns_fizz(self):
        self.assertEqual(FizzBuzz(3).result, 'Fizz')
        self.assertEqual(FizzBuzz(12).result, 'Fizz')
        self.assertEqual(FizzBuzz(18).result, 'Fizz')

    def test_value_divisible_by_5_returns_buzz(self):
        self.assertEqual(FizzBuzz(5).result, 'Buzz')
        self.assertEqual(FizzBuzz(10).result, 'Buzz')
        self.assertEqual(FizzBuzz(50).result, 'Buzz')
    
    def test_value_divisible_by_3_5_returns_fizzbuzz(self):
        self.assertEqual(FizzBuzz(15).result, 'FizzBuzz')
        self.assertEqual(FizzBuzz(30).result, 'FizzBuzz')
        self.assertEqual(FizzBuzz(60).result, 'FizzBuzz')

