from unittest import TestCase
from books import get_user_choice
from unittest.mock import patch
import io


class TestGetUserChoice(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["one", '1'])
    def test_get_user_choice_repeats_if_not_valid_input(self, mock_input, mock_stdout):
        get_user_choice(['Author', 'Title', 'Publisher'], '\nWhat option would you like to search by?')
        expected = '\nWhat option would you like to search by?\n1 - Author\n2 - Title\n3 - Publisher\n' \
                   '\nWhat option would you like to search by?\n1 - Author\n2 - Title\n3 - Publisher\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_returns_users_input_if_it_is_valid_option(self, mock_input):
        actual = get_user_choice(['Author', 'Title', 'Publisher'], '\nWhat option would you like to search by?')
        expected = '1'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_returns_string(self, mock_input):
        actual = get_user_choice(['Author', 'Title', 'Publisher'], '\nWhat option would you like to search by?')
        self.assertEqual(str, type(actual))
