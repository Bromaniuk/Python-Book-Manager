from unittest import TestCase
from books import move_book
from books import Book
from unittest.mock import patch
import io


class TestMoveBook(TestCase):

    def setUp(self):
        self.test_book_one = Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')
        self.test_book_two = Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')
        self.test_book_three = Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')

    @patch('builtins.input', side_effect=['1', '2'])
    def test_move_book_returns_none(self, mock_input):
        library = [self.test_book_one, self.test_book_two, self.test_book_three]
        found_books = [self.test_book_one]
        self.assertIsNone(move_book(library, found_books))

    @patch('builtins.input', side_effect=['1', '2'])
    def test_move_book_edits_book_shelf_value_correctly(self, mock_input):
        library = [self.test_book_one, self.test_book_two, self.test_book_three]
        found_books = [self.test_book_one]
        move_book(library, found_books)
        self.assertEqual('2', self.test_book_one.shelf)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '2'])
    def test_move_book_prints_correct_messages(self, mock_input, mock_stdout):
        library = [self.test_book_one, self.test_book_two, self.test_book_three]
        found_books = [self.test_book_one]
        move_book(library, found_books)
        expected = """\nWhich book would you like to move?\
\n1 - This book is named 'BookOne', written by 'AuthorOne', published by 'PublisherOne', \
category of 'CategoryOne', subject of 'SubjectOne', and currently sits on shelf: 1.\n\
Success! BookOne has been moved to shelf '2'.\n"""
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2', 'one', '1', '3'])
    def test_move_book_repeats_if_invalid_book_selection(self, mock_input, mock_stdout):
        library = [self.test_book_one, self.test_book_two, self.test_book_three]
        found_books = [self.test_book_one]
        move_book(library, found_books)
        expected = "\nWhich book would you like to move?" \
                   "\n1 - This book is named 'BookOne', written by 'AuthorOne', published by 'PublisherOne', " \
                   "category of 'CategoryOne', subject of 'SubjectOne', and currently sits on shelf: 1." \
                   "\n\nWhich book would you like to move?" \
                   "\n1 - This book is named 'BookOne', written by 'AuthorOne', published by 'PublisherOne', " \
                   "category of 'CategoryOne', subject of 'SubjectOne', and currently sits on shelf: 1." \
                   "\n\nWhich book would you like to move?" \
                   "\n1 - This book is named 'BookOne', written by 'AuthorOne', published by 'PublisherOne', " \
                   "category of 'CategoryOne', subject of 'SubjectOne', and currently sits on shelf: 1.\n" \
                   "Success! BookOne has been moved to shelf '3'.\n"
        self.assertEqual(expected, mock_stdout.getvalue())
