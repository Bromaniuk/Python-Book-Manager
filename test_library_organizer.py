from unittest import TestCase
from books import library_organizer
from unittest.mock import patch
import io


class TestLibraryOrganizer(TestCase):

    @patch('builtins.input', side_effect=['3'])
    def test_library_organizer_returns_none(self, mock_input):
        self.assertIsNone(library_organizer())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3'])
    def test_library_organizer_saves_and_exits_correctly(self, mock_input, mock_stdout):
        library_organizer()
        expected = "Hidey-ho, book lover! Welcome to Brian's Totally Tubular Library Organizer!" \
                   "\nPlease wait while we load your book library..." \
                   "\nLibrary is ready to load." \
                   "\nYour Library has been loaded." \
                   "\n\nWhat would you like to do within your library?" \
                   "\n1 - Search for a book" \
                   "\n2 - Move a book to another shelf" \
                   "\n3 - Save and Exit" \
                   "\n\nYour library has been saved successfully." \
                   "\nThank you for using Brian's Totally Tubular Library Organizer! Come again soon!\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '2', 'thunder', '1', '3'])
    def test_library_organizer_searches_for_book_correctly(self, mock_input, mock_stdout):
        library_organizer()
        expected = "Hidey-ho, book lover! Welcome to Brian's Totally Tubular Library Organizer!" \
                   "\nPlease wait while we load your book library..." \
                   "\nLibrary is ready to load." \
                   "\nYour Library has been loaded." \
                   "\n\nWhat would you like to do within your library?" \
                   "\n1 - Search for a book" \
                   "\n2 - Move a book to another shelf" \
                   "\n3 - Save and Exit" \
                   "\n\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('Zimmer Bradley', 'Thunderlord', 'Daw', '3', 'Fiction', 'Fantasy')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf" \
                   "\n\nWhat would you like to do within your library?" \
                   "\n1 - Search for a book" \
                   "\n2 - Move a book to another shelf" \
                   "\n3 - Save and Exit" \
                   "\n\nYour library has been saved successfully." \
                   "\nThank you for using Brian's Totally Tubular Library Organizer! Come again soon!\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2', '2', 'the lion', '1', '3'])
    def test_library_organizer_moves_book_correctly(self, mock_input, mock_stdout):
        library_organizer()
        expected = "Hidey-ho, book lover! Welcome to Brian's Totally Tubular Library Organizer!" \
                   "\nPlease wait while we load your book library..." \
                   "\nLibrary is ready to load." \
                   "\nYour Library has been loaded." \
                   "\n\nWhat would you like to do within your library?" \
                   "\n1 - Search for a book" \
                   "\n2 - Move a book to another shelf" \
                   "\n3 - Save and Exit" \
                   "\nLet's find you a book to move!" \
                   "\n\nWhat option would you like to search by?" \
                   "\n1 - Author" \
                   "\n2 - Title" \
                   "\n3 - Publisher" \
                   "\n4 - Shelf" \
                   "\n5 - Category" \
                   "\n6 - Subject" \
                   "\nWe found 1 book(s) that matched this search in your library." \
                   "\n\n1 - Book('Lewis', 'The Lion, the Witch & the Wardrobe', 'Puffin', '45', 'Fiction', 'Fantasy')" \
                   "\n\nWould you like to return to the main menu or move a book?" \
                   "\n1 - Return to main menu" \
                   "\n2 - Move a book to another shelf" \
                   "\n\nWhat would you like to do within your library?" \
                   "\n1 - Search for a book" \
                   "\n2 - Move a book to another shelf" \
                   "\n3 - Save and Exit" \
                   "\n\nYour library has been saved successfully." \
                   "\nThank you for using Brian's Totally Tubular Library Organizer! Come again soon!\n"
        self.assertEqual(expected, mock_stdout.getvalue())
