from unittest import TestCase
from books import return_to_main_menu
from unittest.mock import patch


class TestReturnToMainMenu(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_return_to_main_menu_returns_true(self, mock_input):
        self.assertTrue(return_to_main_menu())

    @patch('builtins.input', side_effect=['2'])
    def test_return_to_main_menu_returns_false(self, mock_input):
        self.assertFalse(return_to_main_menu())

    @patch('builtins.input', side_effect=['one', 'two', '3', '1'])
    def test_return_to_main_menu_repeats_until_valid_choice(self, mock_input):
        self.assertTrue(return_to_main_menu())
