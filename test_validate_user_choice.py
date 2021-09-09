from unittest import TestCase
from books import validate_user_choice


class TestValidateUserChoice(TestCase):

    def test_validate_user_choice_return_true(self):
        actual = validate_user_choice('1', ['Author', 'Title'])
        self.assertTrue(actual)

    def test_validate_user_choice_return_false(self):
        actual = validate_user_choice('one', ['Author', 'Title'])
        self.assertFalse(actual)
