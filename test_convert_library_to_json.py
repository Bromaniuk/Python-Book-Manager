from unittest import TestCase
from books import convert_library_to_json
from books import Book


class TestConvertLibraryToJson(TestCase):

    def setUp(self):
        self.test_book_one = Book('AuthorOne', 'BookOne', 'PublisherOne', '1', 'CategoryOne', 'SubjectOne')
        self.test_book_two = Book('AuthorTwo', 'BookTwo', 'PublisherTwo', '2', 'CategoryTwo', 'SubjectTwo')
        self.test_book_three = Book('AuthorThree', 'BookThree', 'PublisherThree', '1', 'CategoryThree', 'SubjectThree')

    def test_convert_library_to_json_returns_list(self):
        library = [self.test_book_one, self.test_book_two, self.test_book_three]
        actual = convert_library_to_json(library)
        self.assertEqual(list, type(actual))

    def test_convert_library_to_json_returns_list_in_correct_json_format(self):
        library = [self.test_book_one, self.test_book_two, self.test_book_three]
        actual = convert_library_to_json(library)
        expected = [{'Author': 'AuthorOne', 'Category': 'CategoryOne', 'Publisher': 'PublisherOne',
                     'Shelf': '1', 'Subject': 'SubjectOne', 'Title': 'BookOne'},
                    {'Author': 'AuthorTwo', 'Category': 'CategoryTwo', 'Publisher': 'PublisherTwo',
                     'Shelf': '2', 'Subject': 'SubjectTwo', 'Title': 'BookTwo'},
                    {'Author': 'AuthorThree', 'Category': 'CategoryThree', 'Publisher': 'PublisherThree',
                     'Shelf': '1', 'Subject': 'SubjectThree', 'Title': 'BookThree'}]
        self.assertEqual(expected, actual)
