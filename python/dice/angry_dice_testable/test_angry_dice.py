__author__ = 'mw'

import unittest
from angry_dice import AngryDice
from unittest.mock import patch
from io import StringIO


class AngryDiceTest(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

    #
    # TESTS cheating_status
    #
    def test_cheating_status_hold_a6_roll_b4(self):
        """ [6, 4], user holds A6 and rolls B4, is cheating """
        self.game.stage = 3
        self.game.userInput = "b"
        self.assertTrue(self.game.cheating_status("6", "4"),
                        "[6, 4], hold a, roll b, cheating")

    def test_cheating_status_roll_a4_hold_b6(self):
        """ [4, 6], user holds A4 and rolls B6, is cheating """
        self.game.stage = 3
        self.game.userInput = "a"
        self.assertTrue(self.game.cheating_status("4", "6"),
                         "[4, 6], roll a, hold b, cheating")

    def test_cheating_status_hold_a6_hold_b6(self):
        """ [6, 6], user holds A6 and holds B6, is cheating """
        self.game.stage = 3
        self.game.userInput = ""
        self.assertTrue(self.game.cheating_status("6", "6"),
                         "[6, 6], hold a, hold b, cheating")

    def test_cheating_status_roll_a6_hold_b6(self):
        """ [6, 6], user rolls A6 and holds B6, is cheating """
        self.game.stage = 3
        self.game.userInput = "b"
        self.assertTrue(self.game.cheating_status("6", "6"),
                         "[6, 6], hold a, roll b, cheating")

    def test_cheating_status_roll_a6_roll_b6(self):
        """ [6, 6], user rolls A6 and rolls B6, not cheating """
        self.game.stage = 3
        self.game.userInput = "ab"
        self.assertFalse(self.game.cheating_status("6", "6"),
                         "[6, 6], roll a, roll b, not cheating")

    def test_cheating_status_roll_a1_roll_b1(self):
        """ [6, 6], user rolls A6 and rolls B6, not cheating """
        self.game.stage = 3
        self.game.userInput = "ab"
        self.assertFalse(self.game.cheating_status("1", "1"),
                         "[1, 1], roll a, roll b, not cheating")

    #
    # TESTS check_user_input
    #
    # def test_cheating_status_holdDieA_rollB(self):
    #     """ [6, 4], user holds A6 and rolls B4 """
    #     self.game.stage = 3
    #     self.game.userInput = "B"
    #     self.assertFalse(self.game.cheating_status("6", "4"),
    #                     "[6, 6], stage 3, hold a, roll B")

    # def test_cheating_status_holdDieB_rollA(self):
    #     """ [4, 6], user holds A4 and rolls B6 """
    #     self.game.stage = 3
    #     self.game.userInput = "A"
    #     self.assertFalse(self.game.cheating_status("4", "6"),
    #                      "[4, 6], stage 3, hold b, roll A")

    #
    # TESTS method stage_1
    #
    def test_stage_1_a1_b2(self):
        """ [1, 2] stage becomes 2 """
        self.stage = 1
        self.game.stage_1("1", "2")
        self.assertEqual(2, self.game.stage, "[1, 2], changes to stage 2")

    def test_stage_1_a1_b3(self):
        """ [1, 2] stage stays 1 """
        self.stage = 1
        self.game.stage_1("1", "3")
        self.assertNotEqual(2, self.game.stage, "[1, 3], stays at stage 1")


    def test_stage_1_a2_b1(self):
        """ [2, 1] stage becomes 2 """
        self.stage = 1
        self.game.stage_1("2", "1")
        self.assertEqual(2, self.game.stage, "[2, 1], changes to stage 2")

    def test_stage_1_a3_b3(self):
        """ [3, 3] stage stays 1 """
        self.stage = 1
        self.game.stage_1("3", "3")
        self.assertNotEqual(2, self.game.stage, "[3, 3], stays at stage 1")

    #
    # TESTS method stage_2
    #
    def test_stage_2_aAngry_b4(self):
        """ [1, 2] stage becomes 2 """
        self.stage = 2
        self.game.stage_2("ANGRY", "4")
        self.assertEqual(3, self.game.stage, "[Angry, 4], changes to stage 3")

    def test_stage_2_aAngry_b1(self):
        """ [1, 2] stage stays 1 """
        self.stage = 2
        self.game.stage_2("ANGRY", "1")
        self.assertNotEqual(3, self.game.stage, "[Angry, 1], stays at stage 2")


    def test_stage_2_a4_bAngry(self):
        """ [2, 1] stage becomes 2 """
        self.stage = 2
        self.game.stage_2("4", "ANGRY")
        self.assertEqual(3, self.game.stage, "[4, Angry], changes to stage 3")

    def test_stage_2_a1_b1(self):
        """ [3, 3] stage stays 1 """
        self.stage = 2
        self.game.stage_2("1", "1")
        self.assertNotEqual(3, self.game.stage, "[1, 1], stays at stage 2")

    #
    # TESTS method stage_3
    #
    def test_stage_3_a5_b6(self):
        """ [5, 6] win, game over """
        self.finalCheck = False
        self.game.stage_2("5", "6")
        self.assertEqual(False, self.finalCheck, "[5, 6], win, game over")

    def test_stage_3_a5_b1(self):
        """ [5, 1] finalCheck stays False """
        self.finalCheck = False
        self.game.stage_2("5", "1")
        self.assertNotEqual(True, self.finalCheck, "[5, 1], stays at stage 3")


    def test_stage_3_a6_b5(self):
        """ [5, 6] win, game over """
        self.finalCheck = False
        self.game.stage_2("6", "5")
        self.assertEqual(False, self.finalCheck, "[6, 5], win, game over")

    def test_stage_3_a1_b1(self):
        """ [1, 1] finalCheck stays False """
        self.finalCheck = False
        self.game.stage_2("1", "1")
        self.assertNotEqual(True, self.finalCheck, "[1, 1], stays at stage 3")







if __name__ == '__main__':
    unittest.main()
