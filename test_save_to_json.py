from unittest import TestCase
from books import save_to_json
from books import Book
from books import convert_library_to_json
from unittest.mock import patch
import pathlib
import json
import os
import io


class TestSaveToJson(TestCase):

    def setUp(self):
        self.test_book_one = Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')
        self.test_book_two = Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')
        self.test_book_three = Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')
        self.list_of_books = [self.test_book_one, self.test_book_two, self.test_book_three]

    def test_save_to_json_somebooks_json_exists(self):
        path = pathlib.Path("somebooks.json")
        self.assertTrue(path.is_file())
        self.assertTrue(path.parent.is_dir())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_save_to_json_works_correctly(self, mock_output):
        save_to_json(self.list_of_books, 'test_books.json')
        expected = ''
        self.assertEqual(expected, mock_output.getvalue())

        try:
            with open('test_books.json') as file_object:
                content = json.load(file_object)
                converted_test_list = convert_library_to_json(self.list_of_books)
                self.assertEqual(content, converted_test_list)
        except FileNotFoundError:
            self.fail()
        finally:
            if os.path.exists('test_books.json'):
                os.remove('test_books.json')
