__author__ = 'mw'

import unittest
from angry_dice import AngryDice


class test_stage_1(unittest.TestCase):

    def setUp(self):
        """ Initializes the die for the following testing functions """

        self.game = AngryDice()
        # print(self.shortDescription())

    def tearDown(self):
        """ delete the instance of game after running tests """
        del self.game

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


if __name__ == '__main__':
    unittest.main()
