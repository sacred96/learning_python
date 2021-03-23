import unittest
import src.arithmetic as ar


class ArithmeticTestCase(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(ar.arithmetic(2, 4, '+'), 6)
        self.assertEqual(ar.arithmetic_dict(0.3, 0.4, '+'), 0.7)
        self.assertEqual(ar.arithmetic_lambda(-7, 7.5, '+'), 0.5)

    def test_minus(self):
        self.assertEqual(ar.arithmetic(2, 4, '-'), -2)
        self.assertEqual(round(ar.arithmetic_dict(0.5, 0.4, '-'), 1), 0.1)  # problem with float. it's normal :)
        self.assertEqual(ar.arithmetic_lambda(-7, 7.5, '-'), -14.5)

    def test_multiply(self):
        self.assertEqual(ar.arithmetic(2, 4, '*'), 8)
        self.assertEqual(ar.arithmetic_dict(0.3, 0.4, '*'), 0.12)
        self.assertEqual(ar.arithmetic_lambda(-7, 7.5, '*'), -52.5)

    def test_divide(self):
        self.assertEqual(ar.arithmetic(4, 2, '/'), 2)
        self.assertEqual(round(ar.arithmetic_dict(0.3, 0.4, '/'), 2), 0.75)
        self.assertEqual(ar.arithmetic_lambda(-7, 7, '/'), -1)

    def test_unknown(self):
        self.assertEqual(ar.arithmetic(4, 2, 'fg'), 'Unknown operator')
        self.assertEqual(ar.arithmetic_dict(0.3, 0.4, '%%'), 'Unknown operator')
        self.assertEqual(ar.arithmetic_lambda(-7, 7, '.'), 'Unknown operator')


if __name__ == "__main__":
    unittest.main()
