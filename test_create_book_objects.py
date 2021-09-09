from unittest import TestCase
from books import create_book_objects
from books import Book
from unittest.mock import patch
import io


class TestCreateBookObjects(TestCase):

    def test_create_book_objects_returns_list(self):
        actual = create_book_objects([{'Author': 'Auth1', 'Title': 'Book1', 'Publisher': 'Publish1',
                                       'Shelf': '1', 'Category': 'Category1', 'Subject': 'Subject1'},
                                      {'Author': 'Auth2', 'Title': 'Book2', 'Publisher': 'Publish2',
                                       'Shelf': '2', 'Category': 'Category2', 'Subject': 'Subject2'}])
        self.assertEqual(list, type(actual))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_book_objects_prints_correct_message(self, mock_stdout):
        create_book_objects([{'Author': 'AuthOne', 'Title': 'Book1', 'Publisher': 'Publish1',
                              'Shelf': '1', 'Category': 'Category1', 'Subject': 'Subject1'},
                             {'Author': 'Auth2', 'Title': 'Book2', 'Publisher': 'Publish2',
                              'Shelf': '2', 'Category': 'Category2', 'Subject': 'Subject2'}])
        expected = 'Your Library has been loaded.\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_create_book_objects_correctly_creates_books(self):
        actual = create_book_objects([{'Author': 'AuthUno', 'Title': 'Book1', 'Publisher': 'Publish1',
                                       'Shelf': '1', 'Category': 'Category1', 'Subject': 'Subject1'},
                                      {'Author': 'Auth2', 'Title': 'Book2', 'Publisher': 'Publish2',
                                       'Shelf': '2', 'Category': 'Category2', 'Subject': 'Subject2'}])
        book_one = actual[0]
        book_two = actual[1]
        self.assertEqual(Book, type(book_one))
        self.assertEqual(Book, type(book_two))
