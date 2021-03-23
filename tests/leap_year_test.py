import unittest
import src.is_year_leap as y


class IsYearLeapTestCase(unittest.TestCase):
    def test_year_leap(self):
        for year in (2028, 1964, 2000, 1932):
            self.assertTrue(y.is_year_leap(year))

    def test_year_not_leap(self):
        for year in (2022, 1871, 2001, 1939):
            self.assertFalse(y.is_year_leap(year))


if __name__ == "__main__":
    unittest.main()
