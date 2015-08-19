__author__ = 'mw'

import unittest
from angry_dice import AngryDice


class TestAngryDiceCheatingStatus(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """
        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """

        del self.game

    def test_cheating_status_hold_a6_roll_b4(self):
        """ [6, 4], user holds a6 and rolls b4, is cheating """
        self.game.stage = 3
        self.game.userInput = "b"
        self.assertTrue(self.game.cheating_status("6", "4"),
                        "[6, 4], hold a, roll b, cheating")
        self.assertIn("You're cheating!", self.game.outcome, "cheating")

    def test_cheating_status_roll_a4_hold_b6(self):
        """ [4, 6], user holds a4 and rolls b6, is cheating """
        self.game.stage = 3
        self.game.userInput = "a"
        self.assertTrue(self.game.cheating_status("4", "6"),
                        "[4, 6], roll a, hold b, cheating")
        self.assertIn("You're cheating!", self.game.outcome, "cheating")

    def test_cheating_status_hold_a6_hold_b6(self):
        """ [6, 6], user holds a6 and holds b6, is cheating """
        self.game.stage = 3
        self.game.userInput = ""
        self.assertTrue(self.game.cheating_status("6", "6"),
                         "[6, 6], hold a, hold b, cheating")
        self.assertIn("You're cheating!", self.game.outcome, "cheating")

    def test_cheating_status_roll_a6_hold_b6(self):
        """ [6, 6], user rolls a6 and holds b6, is cheating """
        self.game.stage = 3
        self.game.userInput = "b"
        self.assertTrue(self.game.cheating_status("6", "6"),
                         "[6, 6], hold a, roll b, cheating")
        self.assertIn("You're cheating!", self.game.outcome, "cheating")

    def test_cheating_status_roll_a6_roll_b6(self):
        """ [6, 6], user rolls a6 and rolls b6, not cheating """
        self.game.stage = 3
        self.game.userInput = "ab"
        self.assertFalse(self.game.cheating_status("6", "6"),
                         "[6, 6], roll a, roll b, not cheating")
        self.assertNotIn("You're cheating!", self.game.outcome, "notcheating")

    def test_cheating_status_roll_a1_roll_b1(self):
        """ [6, 6], user rolls a6 and rolls b6, not cheating """
        self.game.stage = 3
        self.game.userInput = "ab"
        self.assertFalse(self.game.cheating_status("1", "1"),
                         "[1, 1], roll a, roll b, not cheating")
        self.assertNotIn("You're cheating!", self.game.outcome, "not cheating")
