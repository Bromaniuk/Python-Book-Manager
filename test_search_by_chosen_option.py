from unittest import TestCase
from books import search_by_chosen_option
from books import Book
from unittest.mock import patch
import io


class TestSearchByChosenOption(TestCase):

    def setUp(self):
        self.test_book_one = Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')
        self.test_book_two = Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')
        self.test_book_three = Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')

    @patch('builtins.input', side_effect=['auth', '1'])
    def test_search_by_chosen_option_returns_none(self, mock_input):
        self.assertIsNone(search_by_chosen_option([self.test_book_one], 'Author'))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['authort', '1'])
    def test_search_by_chosen_option_author_displays_correct_multiple_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Author')
        expected = "We found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n2 - Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['authorone', '1'])
    def test_search_by_chosen_option_author_displays_correct_result(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Author')
        expected = "We found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['lewis', '1'])
    def test_search_by_chosen_option_author_displays_correct_zero_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Author')
        expected = "We found 0 book(s) that matched this search in your library.\n" \
                   "\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['bookt', '1'])
    def test_search_by_chosen_option_title_displays_correct_multiple_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Title')
        expected = "We found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n2 - Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['bookone', '1'])
    def test_search_by_chosen_option_title_displays_correct_result(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Title')
        expected = "We found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['l33t', '1'])
    def test_search_by_chosen_option_title_displays_correct_zero_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Title')
        expected = "We found 0 book(s) that matched this search in your library.\n" \
                   "\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['publishert', '1'])
    def test_search_by_chosen_option_publisher_displays_correct_multiple_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Publisher')
        expected = "We found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n2 - Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['publisherone', '1'])
    def test_search_by_chosen_option_publisher_displays_correct_result(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Publisher')
        expected = "We found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['l33t publishing', '1'])
    def test_search_by_chosen_option_publisher_displays_correct_zero_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Publisher')
        expected = "We found 0 book(s) that matched this search in your library.\n" \
                   "\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['categoryt', '1'])
    def test_search_by_chosen_option_category_displays_correct_multiple_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Category')
        expected = "We found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n2 - Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['categoryone', '1'])
    def test_search_by_chosen_option_category_displays_correct_result(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Category')
        expected = "We found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['l33t category', '1'])
    def test_search_by_chosen_option_category_displays_correct_zero_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Category')
        expected = "We found 0 book(s) that matched this search in your library.\n" \
                   "\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['subjectt', '1'])
    def test_search_by_chosen_option_subject_displays_correct_multiple_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Subject')
        expected = "We found 2 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')" \
                   "\n2 - Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['subjectone', '1'])
    def test_search_by_chosen_option_subject_displays_correct_result(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Subject')
        expected = "We found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['l33t subject', '1'])
    def test_search_by_chosen_option_subject_displays_correct_zero_results(self, mock_input, mock_stdout):
        search_by_chosen_option([self.test_book_one, self.test_book_two, self.test_book_three], 'Subject')
        expected = "We found 0 book(s) that matched this search in your library.\n" \
                   "\n"
        self.assertEqual(expected, mock_stdout.getvalue())
