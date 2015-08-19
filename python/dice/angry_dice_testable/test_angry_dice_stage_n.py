__author__ = 'mw'

import unittest
from angry_dice import AngryDice


class test_stage_n(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

    #
    # TESTS method stage_1
    #
    def test_stage1_a1_b2(self):
        """ [1, 2] stage becomes 2 """
        self.game.stage = 1
        self.game.stage_1("1", "2")
        self.assertEqual(2, self.game.stage, "[1, 2], changes to stage 2")
        self.assertIn("Stage 1 completed", self.game.outcome, "now stage 2")

    def test_stage1_a1_b3(self):
        """ [1, 2] stage stays 1 """
        self.game.stage = 1
        self.game.stage_1("1", "3")
        self.assertNotEqual(2, self.game.stage, "[1, 3], stays at stage 1")
        self.assertNotIn("Stage 1 completed", self.game.outcome,
                         "stay stage 1")

    def test_stage1_a2_b1(self):
        """ [2, 1] stage becomes 2 """
        self.game.stage = 1
        self.game.stage_1("2", "1")
        self.assertEqual(2, self.game.stage, "[2, 1], changes to stage 2")
        self.assertIn("Stage 1 completed", self.game.outcome, "now stage 2")

    def test_stage1_a3_b3(self):
        """ [3, 3] stage stays 1 """
        self.game.stage = 1
        self.game.stage_1("3", "3")
        self.assertNotEqual(2, self.game.stage, "[3, 3], stays at stage 1")
        self.assertNotIn("Stage 1 completed", self.game.outcome,
                         "stay stage 2")

    #
    # TESTS method stage_2
    #
    def test_stage2_aAngry_b4(self):
        """ [1, 2] stage becomes 2 """
        self.game.stage = 2
        self.game.stage_2("ANGRY", "4")
        self.assertEqual(3, self.game.stage, "[Angry, 4], changes to stage 3")
        self.assertIn("Stage 2 completed", self.game.outcome, "now stage 3")

    def test_stage2_aAngry_b1(self):
        """ [1, 2] stage stays 1 """
        self.game.stage = 2
        self.game.stage_2("ANGRY", "1")
        self.assertNotEqual(3, self.game.stage, "[Angry, 1], stays at stage 2")
        self.assertNotIn("Stage 2 completed", self.game.outcome,
                         "stay stage 2")


    def test_stage2_a4_bAngry(self):
        """ [2, 1] stage becomes 2 """
        self.game.stage = 2
        self.game.stage_2("4", "ANGRY")
        self.assertEqual(3, self.game.stage, "[4, Angry], changes to stage 3")
        self.assertIn("Stage 2 completed", self.game.outcome, "now stage 3")

    def test_stage2_a1_b1(self):
        """ [3, 3] stage stays 1 """
        self.game.stage = 2
        self.game.stage_2("1", "1")
        self.assertNotEqual(3, self.game.stage, "[1, 1], stays at stage 2")
        self.assertNotIn("Stage 2 completed", self.game.outcome,
                         "stay stage 2")

    #
    # TESTS method stage_3
    #
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
