from unittest import TestCase
from books import get_json_data
from books import Book
import pathlib
from unittest.mock import patch
import io


class TestGetJsonData(TestCase):

    def test_get_json_data_json_file_exists(self):
        get_json_data()
        path = pathlib.Path("somebooks.json")
        self.assertTrue(path.is_file())
        self.assertTrue(path.parent.is_dir())

    def test_get_json_data_returns_list(self):
        actual = get_json_data()
        self.assertEqual(list, type(actual))

    def test_get_json_data_returns_list_of_book_objects(self):
        actual = get_json_data()
        first_entry = actual[0]
        last_entry = actual[-1]
        self.assertEqual(Book, type(first_entry))
        self.assertEqual(Book, type(last_entry))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_json_data_prints_correct_messages(self, mock_stdout):
        get_json_data()
        expected = 'Library is ready to load.\nYour Library has been loaded.\n'
        self.assertEqual(expected, mock_stdout.getvalue())
