from math import sqrt
import unittest
import src.custom_square as s


class SquareTestCase(unittest.TestCase):

    def test_square(self):
        for a in range(5, 10):
            with self.subTest(a=a):
                self.assertCountEqual(s.square(a), (4 * a, a ** 2, a * sqrt(2)))


if __name__ == "__main__":
    unittest.main()
