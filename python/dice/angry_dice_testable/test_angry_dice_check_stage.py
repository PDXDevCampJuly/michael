__author__ = 'mw'

import unittest
from angry_dice import AngryDice
from unittest.mock import patch
from io import StringIO


class test_check_stage(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

    def test_check_user_input_change_currentValue_a9(self):
        """ [9, x], does currentValue a9 change after roll a """
        self.game.die_a.currentValue = 9
        self.game.userInput = "a"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_a.currentValue,
                            "[9, x], die_a currentValue not 9")

    def test_check_user_input_change_currentValue_b9(self):
        """ [x, 9], does currentValue b9 change after roll b """

        self.game.die_b.currentValue = 9
        self.game.userInput = "b"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_b.currentValue,
                            "[9, x], die_b currentValue not 9")

    def test_check_user_input_change_currentValue_a9_b9(self):
        """ [9, 9], does currentValue a9, b9 change after roll ab """
        self.game.die_a.currentValue = 9
        self.game.die_b.currentValue = 9
        self.game.userInput = "ab"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_b.currentValue,
                            "[9, 9], die_a, die_b currentValue(s) not 9")










if __name__ == '__main__':
    unittest.main()
