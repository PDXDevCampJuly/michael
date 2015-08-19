__author__ = 'mw'

import unittest
from angry_dice import AngryDice


class test_check_user_input(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

    def test_check_user_input_change_currentValue_a9_roll_a(self):
        """ [9, x], does currentValue a9 change after roll a """
        self.game.die_a.currentValue = 9
        self.game.userInput = "a"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_a.currentValue,
                            "[9, x], die_a currentValue not 9")

    def test_check_user_input_change_currentValue_b9_roll_b(self):
        """ [x, 9], does currentValue b9 change after roll b """

        self.game.die_b.currentValue = 9
        self.game.userInput = "b"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_b.currentValue,
                            "[9, x], die_b currentValue not 9")

    def test_check_user_input_change_currentValue_a9_b9_roll_ab(self):
        """ [9, 9], does currentValue a9, b9 change after roll ab """
        self.game.die_a.currentValue = 9
        self.game.die_b.currentValue = 9
        self.game.userInput = "ab"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_a.currentValue,
                            "[9, 9], die_a currentValue not 9")
        self.assertNotEqual(9, self.game.die_b.currentValue,
                            "[9, 9], die_b currentValue not 9")

    def test_check_user_input_change_currentValue_a9_roll_x(self):
        """ [9, x], does currentValue a9 remain for invalid input """
        self.game.die_a.currentValue = 9
        self.game.userInput = "x"
        self.game.check_user_input()
        self.assertEqual(9, self.game.die_a.currentValue,
                            "[9, x], die_a currentValue is still 9")

    def test_check_user_input_change_currentValue_b9_roll_x(self):
        """ [x, 9], does currentValue b9 remain for invalid input """
        self.game.die_b.currentValue = 9
        self.game.userInput = "x"
        self.game.check_user_input()
        self.assertEqual(9, self.game.die_b.currentValue,
                            "[x, 9], die_b currentValue is still 9")

    def test_check_user_input_change_currentValue_a9_b9_roll_xx(self):
        """ [9, 9], does currentValue a9, b9 remain for invalid input """
        self.game.die_a.currentValue = 9
        self.game.die_b.currentValue = 9
        self.game.userInput = "xx"
        self.game.check_user_input()
        self.assertEqual(9, self.game.die_a.currentValue,
                            "[9, 9], die_a currentValue is 9")
        self.assertEqual(9, self.game.die_b.currentValue,
                            "[9, 9], die_b currentValue is 9")

    def test_check_user_input_change_currentValue_a9_roll_ax(self):
        """ [9, x], does currentValue a9 change for mix input """
        self.game.die_a.currentValue = 9
        self.game.userInput = "xax"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_a.currentValue,
                            "[9, x], die_a currentValue not 9")

    def test_check_user_input_change_currentValue_b9_roll_bx(self):
        """ [x, 9], does currentValue b9 change for mix input """
        self.game.die_b.currentValue = 9
        self.game.userInput = "xbx"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_b.currentValue,
                            "[x, 9], die_b currentValue not 9")

    def test_check_user_input_change_currentValue_a9_b9_roll_xabx(self):
        """ [9, 9], does currentValue a9, b9 change for mix input """
        self.game.die_a.currentValue = 9
        self.game.die_b.currentValue = 9
        self.game.userInput = "xabx"
        self.game.check_user_input()
        self.assertNotEqual(9, self.game.die_a.currentValue,
                            "[9, 9], die_a currentValue not 9")
        self.assertNotEqual(9, self.game.die_b.currentValue,
                            "[9, 9], die_b currentValue not 9")



if __name__ == '__main__':
    unittest.main()
