import unittest
import src.season as s


class SeasonTestCase(unittest.TestCase):
    def test_winter(self):
        self.assertEqual(s.season_1(1), 'winter')
        self.assertEqual(s.season_1(2), 'winter')
        self.assertEqual(s.season_1(12), 'winter')

        self.assertEqual(s.season_2(1), 'winter')
        self.assertEqual(s.season_2(2), 'winter')
        self.assertEqual(s.season_2(12), 'winter')

    def test_spring(self):
        self.assertEqual(s.season_1(3), 'spring')
        self.assertEqual(s.season_1(4), 'spring')
        self.assertEqual(s.season_1(5), 'spring')

        self.assertEqual(s.season_2(3), 'spring')
        self.assertEqual(s.season_2(4), 'spring')
        self.assertEqual(s.season_2(5), 'spring')

    def test_summer(self):
        self.assertEqual(s.season_1(6), 'summer')
        self.assertEqual(s.season_1(7), 'summer')
        self.assertEqual(s.season_1(8), 'summer')

        self.assertEqual(s.season_1(6), 'summer')
        self.assertEqual(s.season_1(7), 'summer')
        self.assertEqual(s.season_1(8), 'summer')

    def test_autumn(self):
        self.assertEqual(s.season_1(9), 'autumn')
        self.assertEqual(s.season_1(10), 'autumn')
        self.assertEqual(s.season_1(11), 'autumn')

        self.assertEqual(s.season_1(9), 'autumn')
        self.assertEqual(s.season_1(10), 'autumn')
        self.assertEqual(s.season_1(11), 'autumn')

    def test_not_correct_month(self):
        self.assertEqual(s.season_1(13), 'not correct month')
        self.assertEqual(s.season_1('vfv'), 'not correct month')
        self.assertEqual(s.season_1('4.5'), 'not correct month')

        self.assertRaises(ValueError, s.season_2, **{'month': 13})
        self.assertRaises(ValueError, s.season_2, **{'month': 'fake'})
        with self.assertRaises(ValueError) as context:
            s.season_2(4.5)
        self.assertEqual(
            'not correct month', str(context.exception))


if __name__ == "__main__":
    unittest.main()
