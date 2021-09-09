from unittest import TestCase
from books import book_search
from books import Book
from unittest.mock import patch
import io


class TestBookSearch(TestCase):

    def setUp(self):
        self.test_book_one = Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')
        self.test_book_two = Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')

    @patch('builtins.input', side_effect=['1', '1', '1'])
    def test_book_search_returns_none(self, mock_input):
        self.assertIsNone(book_search([self.test_book_one, self.test_book_two]))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', 'auth', '1'])
    def test_book_search_searches_by_author_and_displays_correct_multiple_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n2 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', 'michael', '1'])
    def test_book_search_searches_by_author_and_displays_correct_zero_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 0 book(s) that matched this search in your library." \
                   "\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2', 'book', '1'])
    def test_book_search_searches_by_title_and_displays_correct_multiple_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n2 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2', 'narnia', '1'])
    def test_book_search_searches_by_title_and_displays_correct_zero_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 0 book(s) that matched this search in your library." \
                   "\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3', 'publisher', '1'])
    def test_book_search_searches_by_publisher_and_displays_correct_multiple_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n2 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3', 'l33t', '1'])
    def test_book_search_searches_by_publisher_and_displays_correct_zero_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 0 book(s) that matched this search in your library." \
                   "\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['4', '1', '1'])
    def test_book_search_searches_by_shelf_and_displays_correct_result(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['4', 'shelf-one', '1'])
    def test_book_search_searches_by_shelf_and_displays_correct_zero_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 0 book(s) that matched this search in your library." \
                   "\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['5', 'category', '1'])
    def test_book_search_searches_by_category_and_displays_correct_multiple_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n2 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['5', 'fantasy', '1'])
    def test_book_search_searches_by_category_and_displays_correct_zero_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 0 book(s) that matched this search in your library." \
                   "\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['6', 'subject', '1'])
    def test_book_search_searches_by_subject_and_displays_correct_multiple_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n2 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['6', 'academia', '1'])
    def test_book_search_searches_by_subject_and_displays_correct_zero_results(self, mock_input, mock_stdout):
        book_search([self.test_book_one, self.test_book_two])
        expected = "\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 0 book(s) that matched this search in your library." \
                   "\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
