import unittest

from calculate import multiply, divide


class MultiplyUnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(2,2), 4)
        self.assertEqual(multiply(1,3), 3)
        self.assertEqual(multiply(2,4), 6)


class DivideUnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual(divide(4,2), 2)
        self.assertEqual(divide(5,2), 2)


if __name__ == '__main__':
    unittest.main()
