import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_calc_fizz_buzz(self):
        self.assertEqual(fizzbuzz.calc_fizz_buzz(3), 'fizz')

if __name__ == "__main__":
    unittest.main()
