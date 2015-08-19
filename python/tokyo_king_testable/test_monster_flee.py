__author__ = 'mw'

import unittest
from monster_class import Monster


class TestMonsterFlee(unittest.TestCase):

    def setUp(self):
        """ Initializes the monster for the following testing functions. """
        self.monster = Monster("Cereal Killer")

    def tearDown(self):
        """ Delete the instance of monster after running tests. """
        del self.monster

    def test_monster_user_input_yes(self):
        """ Determine if userInput is yes or y """
        # self.userInput = "yes"
        # self.monster.flee()
        # self.assertIn("y", self.userInput,
        #               "keyboard key y exists in userInput")


if __name__ == '__main__':
    unittest.main()
