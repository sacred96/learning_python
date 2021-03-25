import unittest
import src.check_date_exists as check


class CheckDateExistsTestCase(unittest.TestCase):
    def test_leap_years(self):
        for year in (2028, 1964, 2000, 1932):
            with self.subTest(year=year):
                self.assertTrue(check.check_date_exists(29, 2, year))

    def test_valid_dates(self):
        self.assertTrue(check.check_date_exists(1, 1, 2000))
        self.assertTrue(check.check_date_exists(28, 2, 123))
        self.assertTrue(check.check_date_exists(1, 9, 2))
        self.assertTrue(check.check_date_exists(31, 12, 1000))
        self.assertTrue(check.check_date_exists(30, 11, 456))

    def test_invalid_month(self):
        self.assertFalse(check.check_date_exists(1, 13, 2005))
        self.assertFalse(check.check_date_exists(2, -3, 5))

    def test_invalid_day(self):
        self.assertFalse(check.check_date_exists(67, 1, 2010))
        self.assertFalse(check.check_date_exists(-50, 3, 2010))
        self.assertRaises(ValueError, check.check_date_exists, **{'day': 3.5, 'month': 5, 'year': 2010})

    def test_invalid_date(self):
        self.assertFalse(check.check_date_exists(32, 13, -100))


if __name__ == "__main__":
    unittest.main()
