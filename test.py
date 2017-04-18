import unittest
import os
import re
from script import Abstract, Weather, Football


class AbstractTestCase(unittest.TestCase):

    def test_checkint_behaviour_with_numbers(self):
        result = Abstract.checkint('123')
        self.assertEqual(True, result)

    def test_checkint_behaviour_with_non_numbers(self):
        result = Abstract.checkint('test')
        self.assertEqual(False, result)

    def test_removespecial_removes_letters(self):
        num = '1a2b3c'
        result = Abstract.removespecial(num)
        self.assertEqual('123', result)

    def test_removespecial_removes_special_characters(self):
        num = '1+2*3^'
        result = Abstract.removespecial(num)
        self.assertEqual('123', result)

    def test_removespecial_leaves_numbers_unchanged(self):
        num = '123'
        result = Abstract.removespecial(num)
        self.assertEqual(num, result)


class WeatherTestCase(unittest.TestCase):
    def setUp(self):
        self.weather = Weather()

    def tearDown(self):
        if self.weather.fname in os.listdir():
            os.remove(self.weather.fname)
        self.weather = None

    def test_file_is_absent_before_download(self):
        files = os.listdir()
        self.assertNotIn(self.weather.fname, files)

    def test_file_is_present_after_download(self):
        Abstract.downloadfile(self.weather.url, self.weather.fname)
        files = os.listdir()
        self.assertIn(self.weather.fname, files)

    def test_url_starts_with_http(self):
        regexp = re.compile(r'^http://')
        result = regexp.search(self.weather.url)
        self.assertTrue(result)

    def test_data_cols_contains_correct_values(self):
        self.assertEqual([0, 1, 2], self.weather.data_cols)


class FootballTestCase(unittest.TestCase):
    def setUp(self):
        self.football = Football()

    def tearDown(self):
        if self.football.fname in os.listdir():
            os.remove(self.football.fname)
        self.football = None

    def test_file_is_absent_before_download(self):
        files = os.listdir()
        self.assertNotIn(self.football.fname, files)

    def test_file_is_present_after_download(self):
        Abstract.downloadfile(self.football.url, self.football.fname)
        files = os.listdir()
        self.assertIn(self.football.fname, files)

    def test_url_starts_with_http(self):
        regexp = re.compile(r'^http://')
        result = regexp.search(self.football.url)
        self.assertTrue(result)

    def test_data_cols_contains_correct_values(self):
        self.assertEqual([1, 6, 8], self.football.data_cols)

if __name__ == '__main__':
    unittest.main()
