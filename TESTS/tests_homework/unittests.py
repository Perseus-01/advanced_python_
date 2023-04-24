
from unittest import TestCase
from main import *

class TestMain(TestCase):
    def test_russia_visits(self):
        result = show_russia_visits(geo_logs)
        expected = russia
        self.assertEqual(result, expected)

    def test_unique_ids(self):
        result = unique_ids(ids)
        expected = unique_ids_list
        self.assertEqual(result, expected)

    def test_max_sales(self):
        result = max_sales(stats)
        expected = expected_stats
        self.assertEqual(result, expected)

# Запуск тестов
# python -m unittest tests_homework/unittests.py



