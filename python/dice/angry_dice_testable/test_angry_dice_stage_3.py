__author__ = 'mw'

import unittest
from angry_dice import AngryDice


class test_stage_3(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

    def test_stage3_a5_b6(self):
        """ [5, 6] win, game over """
        self.game.finalCheck = False
        self.game.stage_3("5", "6")
        self.assertEqual(True, self.game.finalCheck, "[5, 6], win, game over")
        self.assertMultiLineEqual("\n-------------------------------" \
                           "\n-------------------------------" \
                           "\nYou've won! Calm down!\n", self.game.outcome,
                                  "win, game over")

    def test_stage3_a5_b1(self):
        """ [5, 1] finalCheck stays False """
        self.game.finalCheck = False
        self.game.stage_3("5", "1")
        self.assertNotEqual(True, self.game.finalCheck, "[5, 1], "
                                                        "stays at stage 3")
        self.assertEqual("", self.game.outcome, "stays at stage 3")

    def test_stage3_a6_b5(self):
        """ [5, 6] win, game over """
        self.game.finalCheck = False
        self.game.stage_3("6", "5")
        self.assertEqual(True, self.game.finalCheck, "[6, 5], win, game over")
        self.assertMultiLineEqual("\n-------------------------------" \
                           "\n-------------------------------" \
                           "\nYou've won! Calm down!\n", self.game.outcome,
                                  "win, game over")

    def test_stage3_a1_b1(self):
        """ [1, 1] finalCheck stays False """
        self.game.finalCheck = False
        self.game.stage_3("1", "1")
        self.assertNotEqual(True, self.game.finalCheck, "[1, 1], "
                                                        "stays at stage 3")
        self.assertEqual("", self.game.outcome, "stays at stage 3")


if __name__ == '__main__':
    unittest.main()
