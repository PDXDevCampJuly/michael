__author__ = 'Chelsea'

import unittest
from angry_dice import Angry_Dice


class AngrydiceRollDiceTest(unittest, TestCase):


    def roll_empty_list(self):
        angry_game = Angry_Dice()
        exception = False
        try:
            angry_game.roll_the_dice
        except:
            exception = True

        self.assertFalse(exception)

    def test_roll_invalid_input(self):
        angry_game = Angry_Dice()
    
        try:
            angry_game.roll_the_dice(2)
        except TypeError:
            self.assertTrue(False, "Invalid type passed and not handled.")

    def test_roll_one_die(selfself):
        # angry_game = Angry_Dice()
        #
        # signle_dice = Dice([1, 2, 3,"Dog"])
        # signle_dice.currentValue = 7
        # signle_dice_list = an
        pass





if __name__ == '__main__':
    unittest.main()
