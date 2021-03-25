import unittest
import src.compound_interest as ci


class CompoundInterestTestCase(unittest.TestCase):
    def test_zero_year(self):
        self.assertAlmostEqual(ci.compound_interest(400, 0), 400)

    def test_zero_percent(self):
        self.assertAlmostEqual(ci.compound_interest(100, 1, 0), 100)

    def test_zero_money(self):
        self.assertAlmostEqual(ci.compound_interest(0, 1), 0)

    def test_correct_data(self):
        self.assertAlmostEqual(ci.compound_interest(400, 5), 644.204)
        self.assertAlmostEqual(ci.compound_interest(35.5, 2, 4.5), round(38.7668875, 4))


if __name__ == "__main__":
    unittest.main()
