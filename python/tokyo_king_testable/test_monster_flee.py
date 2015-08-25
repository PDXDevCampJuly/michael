__author__ = 'mw'

import unittest
from monster_class import Monster
from unittest.mock import patch
from io import StringIO


class TestMonsterFlee(unittest.TestCase):

    def setUp(self):
        """ Initializes the monster for the following testing functions. """
        self.monster = Monster("Cereal Killer")

    def tearDown(self):
        """ Delete the instance of monster after running tests. """
        del self.monster

    # @patch('builtins.input', return_value=True)
    # def test_monster_user_input_yes(self, input_value):
    #     """ Determine if userInput is yes or y """
    #     self.userInput = "y"
    #     self.monster.flee()
    #     self.assertEqual(True, "y")

    # def test_monster_user_input_yes(self):
    #     """ Determine if userInput is yes or y """
    #     self.userInput = "no"
    #     self.monster.flee()
    #     self.assertIn("n", self.userInput,
    #                   "keyboard key n exists in userInput")
    #
    # def test_monster_user_input_yes_return_True(self):
    #     """ Determine if userInput is yes, method returns True """
    #     self.userInput = "yes"
    #     self.monster.flee()
    #     self.assertTrue(True, self.monster.userInput)
    #
    # def test_monster_user_input_no_return_False(self):
    #     """ Determine if userInput is no, method returns False """
    #     self.userInput = "no"
    #     self.monster.flee()
        self.assertFalse(False, self.monster.userInput)

if __name__ == '__main__':
    unittest.main()
