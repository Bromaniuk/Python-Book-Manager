from unittest import TestCase
from books import search_by_shelf
from books import Book
from unittest.mock import patch
import io


class TestSearchByShelf(TestCase):

    def setUp(self):
        self.test_book_one = Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')
        self.test_book_two = Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')
        self.test_book_three = Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')

    @patch('builtins.input', side_effect=['1', '1'])
    def test_search_by_shelf_returns_none(self, mock_input):
        self.assertIsNone(search_by_shelf([self.test_book_one, self.test_book_two]))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '1'])
    def test_search_by_shelf_displays_correct_multiple_results(self, mock_input, mock_stdout):
        search_by_shelf([self.test_book_one, self.test_book_two, self.test_book_three])
        expected = "We found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n2 - Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2', '1'])
    def test_search_by_shelf_displays_correct_result(self, mock_input, mock_stdout):
        search_by_shelf([self.test_book_one, self.test_book_two, self.test_book_three])
        expected = "We found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['one', '1'])
    def test_search_by_shelf_displays_correct_zero_results(self, mock_input, mock_stdout):
        search_by_shelf([self.test_book_one, self.test_book_two, self.test_book_three])
        expected = "We found 0 book(s) that matched this search in your library.\n" \
                   "\n"
        self.assertEqual(expected, mock_stdout.getvalue())
