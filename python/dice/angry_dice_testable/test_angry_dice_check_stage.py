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


    def test_check_user_input_holdDieA_rollB(self):
        """ [6, 4], user holds A6 and rolls B4 """
        self.game.userInput = "b"

        self.game.die_b.currentValue=8
        self.game.check_user_input()

        self.assertNotEqual(8, self.game.die_b.currentValue)


    # def test_cheating_status_holdDieB_rollA(self):
    #     """ [4, 6], user holds A4 and rolls B6 """
    #     self.game.stage = 3
    #     self.game.userInput = "A"
    #     self.assertFalse(self.game.cheating_status("4", "6"),
    #                      "[4, 6], stage 3, hold b, roll A")









if __name__ == '__main__':
    unittest.main()
