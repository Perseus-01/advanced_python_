from unittest import TestCase
from main import *

# Test Yandex Api

class TestYandex(TestCase):
    def test_create_folder(self):
        result = yandex_user.create_folder(folder_path='test_folder')
        expected = 201
        assert result == expected

    def test_wrong_data(self):
        result = yandex_user.create_folder(folder_path=None)
        expected = 400
        self.assertEqual(result, expected)

    def test_no_found_folder(self):
        result = yandex_user.delete_folder(folder_path='unexisted_folder')
        expected = 404
        self.assertEqual(result, expected)

# Запуск тестов
# $ python -m unittest tests_homework/test_yandex_api.py