import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()

