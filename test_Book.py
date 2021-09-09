from unittest import TestCase
from books import Book


class TestBook(TestCase):

    def setUp(self):
        self.test_book_one = Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')
        self.test_book_two = Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')

    def test_Book_init_self_author_is_correct(self):
        actual = self.test_book_one.author
        expected = 'AuthorOne'
        self.assertEqual(expected, actual)

    def test_Book_init_self_title_is_correct(self):
        actual = self.test_book_one.title
        expected = 'BookOne'
        self.assertEqual(expected, actual)

    def test_Book_init_self_publisher_is_correct(self):
        actual = self.test_book_one.author
        expected = 'AuthorOne'
        self.assertEqual(expected, actual)

    def test_Book_init_self_shelf_is_correct(self):
        actual = self.test_book_one.author
        expected = 'AuthorOne'
        self.assertEqual(expected, actual)

    def test_Book_init_self_category_is_correct(self):
        actual = self.test_book_one.author
        expected = 'AuthorOne'
        self.assertEqual(expected, actual)

    def test_Book_init_self_subject_is_correct(self):
        actual = self.test_book_one.author
        expected = 'AuthorOne'
        self.assertEqual(expected, actual)

    def test_Book_str_returns_string(self):
        actual = self.test_book_one.__str__()
        self.assertEqual(str, type(actual))

    def test_Book_repr_returns_string(self):
        actual = self.test_book_one.__repr__()
        self.assertEqual(str, type(actual))

    def test_Book_str_returns_correct_information(self):
        actual = self.test_book_one.__str__()
        expected = "This book is named 'BookOne', written by 'AuthorOne', published by 'PublisherOne', " \
                   "category of 'CategoryOne', subject of 'SubjectOne', and currently sits on shelf: 1."
        self.assertEqual(expected, actual)

    def test_Book_repr_returns_correct_information(self):
        actual = self.test_book_one.__repr__()
        expected = "Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')"
        self.assertEqual(expected, actual)